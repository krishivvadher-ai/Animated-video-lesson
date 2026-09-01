"""Speech service.

edge-tts is unreachable from this environment (the egress proxy returns 403 for
speech.platform.bing.com), so we fall back one step down the brief's own list to
piper -- the same neural voices, run offline through sherpa-onnx.

    narrator  : en_GB-alan-medium  (British male, warm, unhurried)
    character : en_GB-cori-high    (British female, lighter, quicker)

Every line is cached in audio/lines/ keyed by a hash of (text, voice, speed);
re-renders never regenerate audio.
"""
import hashlib
import os
import re
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOICES = ROOT / "voices"
CACHE = ROOT / "audio" / "lines"
CACHE.mkdir(parents=True, exist_ok=True)

MODELS = {
    "n": ("vits-piper-en_GB-alan-medium", "en_GB-alan-medium.onnx", 0.80),
    "c": ("vits-piper-en_GB-cori-high", "en_GB-cori-high.onnx", 0.84),
}

_engines = {}

# Words the synthesiser gets wrong, respelled phonetically.  Never read out a
# Greek letter: sigma is "the choppiness dial", rho is "the cost of capital".
SAY_AS = [
    (r"\bhysteresis\b", "hiss-tur-ee-sis"),
    (r"\bHysteresis\b", "Hiss-tur-ee-sis"),
    (r"\bDixit\b", "Dick-sit"),
    (r"\bAvinash\b", "Ah-vi-nash"),
    (r"\bMilas\b", "Mee-lass"),
    (r"\bBowdler\b", "Bowd-ler"),
    (r"\bgilt\b", "gilt"),
    (r"\bKenji\b", "Ken-jee"),
    (r"\bMarshallian\b", "Marshall-ian"),
    # No Greek letter is ever read out. Each one is spoken as the thing it
    # stands for, both as a symbol and as its transliterated name, so that a
    # line reads the same whether it was written "σ" or "sigma".
    (r"σ²", "the choppiness squared"),
    (r"\bσ\b", "the choppiness"),
    (r"\bsigma\b", "the choppiness"),
    (r"\bρ\b", "the cost of capital"),
    (r"\brho\b", "the cost of capital"),
    (r"\bμ\b", "the drift"),
    (r"\bmu\b", "the drift"),
    (r"\bβ\b", "the steepness"),
    (r"\bbeta\b", "the steepness"),
    (r"\bα\b", "the other root"),
    (r"\balpha\b", "the other root"),
    (r"£", "pounds "),
    # a substitution can leave "the the choppiness" behind; tidy that up
    (r"\b(?:the|a|an)\s+the\b", "the"),
]


def _engine(key):
    if key not in _engines:
        import sherpa_onnx
        folder, onnx, _ = MODELS[key]
        d = VOICES / folder
        cfg = sherpa_onnx.OfflineTtsConfig(
            model=sherpa_onnx.OfflineTtsModelConfig(
                vits=sherpa_onnx.OfflineTtsVitsModelConfig(
                    model=str(d / onnx),
                    lexicon="",
                    data_dir=str(d / "espeak-ng-data"),
                    tokens=str(d / "tokens.txt"),
                ),
                provider="cpu",
                num_threads=4,
            ),
            max_num_sentences=2,
        )
        _engines[key] = sherpa_onnx.OfflineTts(cfg)
    return _engines[key]


def _spoken(text):
    out = text
    for pat, rep in SAY_AS:
        out = re.sub(pat, rep, out)
    return out


def speak(text, voice="n"):
    """Return (wav_path, duration_seconds) for one narrated line."""
    folder, onnx, speed = MODELS[voice]
    key = hashlib.sha1(f"{voice}|{speed}|{text}".encode()).hexdigest()[:20]
    path = CACHE / f"{key}.wav"
    if not path.exists():
        import numpy as np
        from scipy.io import wavfile
        audio = _engine(voice).generate(_spoken(text), sid=0, speed=speed)
        s = np.asarray(audio.samples, dtype=np.float32)
        peak = float(np.max(np.abs(s))) or 1.0
        s = s / peak * 0.89                      # normalise every line alike
        tail = np.zeros(int(audio.sample_rate * 0.18), dtype=np.float32)
        s = np.concatenate([s, tail])
        # written aside then renamed, so several chapters can render at once
        # without ever seeing a half-written file
        import os
        tmp = path.with_suffix(f".{os.getpid()}.tmp")
        wavfile.write(str(tmp), audio.sample_rate, (s * 32767).astype(np.int16))
        os.replace(tmp, path)
    with wave.open(str(path)) as w:
        dur = w.getnframes() / float(w.getframerate())
    return str(path), dur


def duration(text, voice="n"):
    return speak(text, voice)[1]
