"""Single source of truth for colour, type, timing and layout.

Nothing in chapters/ may define a colour literal. Colour always means the
same thing: see the table in the brief, section 5.4.
"""
from manim import config, WHITE

# ---------------------------------------------------------------- palette
BG      = "#0E1420"   # background
CHALK   = "#F2F0E9"   # figures, main text, axis labels
MUTED   = "#7A8296"   # axes, gridlines, secondary text
MONEY   = "#4CC38A"   # revenue, good outcomes, profit
COST    = "#E5484D"   # costs, losses, bad outcomes
SUNK    = "#F5A524"   # sunk cost, irreversibility
WAIT    = "#7C89F5"   # option value, waiting, uncertainty
TRIGGER = "#B44BE8"   # the two trigger lines H and L

# Part Two attribution colours -- whose claim is on screen, readable at a glance
SRC_BR  = "#E5484D"   # Bowdler & Radia -- the theory under examination
SRC_DX  = "#4A9EDA"   # Dixit -- the alternative
SRC_MM  = "#2FA37A"   # Martin & Milas -- the evidence
SRC_KIT = "#B44BE8"   # Kit's own additions and conjectures

# ---------------------------------------------------------------- type
FONT = "DejaVu Sans"
T_HEAD  = 44   # headings
T_SUB   = 34
T_BODY  = 30   # minimum body size
T_SMALL = 26   # footnotes / page refs only, never a term or a number
T_TINY  = 20   # progress indicator

# ---------------------------------------------------------------- timing
BEAT      = 0.8    # the pause after a new term or a number
PAD       = 0.45   # tail of silence after every narrated line
CARD_HOLD = 4.0    # a definition card stays up at least this long

# ---------------------------------------------------------------- layout
SAFE_W = 12.4      # usable width in manim units (screen is 14.22)
SAFE_H = 6.8

TOTAL_CHAPTERS = 39   # 0..38


def apply():
    config.background_color = BG
