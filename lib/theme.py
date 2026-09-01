"""Single source of truth for colour, type, timing and layout.

The visual system is 3Blue1Brown's, taken from his own manim configuration
(`3b1b/manim`, `manimlib/default_config.yml`): a dark neutral ground at
#333333, 1920x1080 at 30 frames a second, a frame eight units high, and his
published colour table. The type is CMU Serif -- the Computer Modern face his
LaTeX text is set in.

Each colour keeps one meaning for the whole film. If money is green in chapter
one it is green in chapter forty-three.
"""
from manim import config

# ---------------------------------------------------------------- 3b1b palette
# hex values from manimlib/default_config.yml
BLUE_E, BLUE_D, BLUE_C, BLUE_B, BLUE_A = "#1C758A", "#29ABCA", "#58C4DD", "#9CDCEB", "#C7E9F1"
TEAL_E, TEAL_D, TEAL_C = "#49A88F", "#55C1A7", "#5CD0B3"
GREEN_E, GREEN_D, GREEN_C, GREEN_B = "#699C52", "#77B05D", "#83C167", "#A6CF8C"
YELLOW_E, YELLOW_D, YELLOW_C, YELLOW_B = "#E8C11C", "#F4D345", "#FFFF00", "#FFEA94"
GOLD_E, GOLD_D, GOLD_C, GOLD_B = "#C78D46", "#E1A158", "#F0AC5F", "#F9B775"
RED_E, RED_D, RED_C, RED_B = "#CF5044", "#E65A4C", "#FC6255", "#FF8080"
MAROON_D, MAROON_C, MAROON_B = "#A24D61", "#C55F73", "#EC92AB"
PURPLE_E, PURPLE_D, PURPLE_C, PURPLE_B = "#644172", "#715582", "#9A72AC", "#B189C6"
GREY_E, GREY_D, GREY_C, GREY_B, GREY_A = "#222222", "#444444", "#888888", "#BBBBBB", "#DDDDDD"
PURE_WHITE, PURE_BLACK = "#FFFFFF", "#000000"
PINK, ORANGE = "#D147BD", "#FF862F"

# ---------------------------------------------------------------- what things mean
BG      = "#1C1C1C"    # the ground: a dark, calm neutral
CHALK   = PURE_WHITE   # figures, main text
MUTED   = GREY_B       # axes, gridlines, secondary text
MONEY   = GREEN_C      # revenue, good outcomes, profit
COST    = RED_C        # costs, losses, bad outcomes
SUNK    = GOLD_C       # sunk cost, irreversibility
WAIT    = BLUE_C       # option value, waiting, uncertainty
TRIGGER = YELLOW_D     # the two trigger lines, and the bar they set

# Part Three attribution -- whose claim is on screen, readable at a glance
SRC_BR  = RED_C        # Bowdler & Radia -- the theory under examination
SRC_DX  = BLUE_D       # Dixit -- the alternative
SRC_MM  = TEAL_C       # Martin & Milas -- the evidence
SRC_KIT = YELLOW_D     # Kit's own additions -- deliberately the trigger colour

# ---------------------------------------------------------------- type
FONT = "CMU Serif"          # Computer Modern: the face LaTeX, and 3b1b, set text in
FONT_MONO = "CMU Typewriter Text"
T_HEAD  = 46
T_SUB   = 36
T_BODY  = 32
T_SMALL = 27
T_TINY  = 22   # the film's smallest text is exactly the readable minimum

# ---------------------------------------------------------------- timing
BEAT      = 1.4     # a reveal is allowed to land before the next one starts
PAD       = 0.45
CARD_HOLD = 4.0
LAG       = 0.2     # 3b1b's staggered-reveal lag

# ---------------------------------------------------------------- axes
# His axes carry arrowheads and tick marks, and he adds numbers to them.
# Three layers of attention: what is being said now, what it is being said
# against, and the structure both sit on.
OPACITY_PRIMARY = 1.00
OPACITY_CONTEXT = 0.40
OPACITY_GRID    = 0.15

# A background grid is structure, not content, and stays at 15%.
GRID = {"color": MUTED, "stroke_width": 1, "stroke_opacity": OPACITY_GRID}

AXIS = {
    "color": MUTED,
    "stroke_width": 2,
    "stroke_opacity": 0.45,
    "include_ticks": True,
    "tick_size": 0.06,
    "include_tip": True,
    "tip_width": 0.18,
    "tip_height": 0.18,
}

# his MED_SMALL_BUFF / SMALL_BUFF
BUFF_TITLE = 0.35

# ---------------------------------------------------------------- layout
SAFE_W = 12.4
SAFE_H = 6.8

TOTAL_CHAPTERS = 44   # 0..43


def apply():
    config.background_color = BG
