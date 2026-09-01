"""The multiplier surface -- the film's one genuinely three-dimensional object.

Dixit's multiplier depends on two things and two things only: how choppy the
revenue is, and what the money costs. Two inputs and one output is a surface,
so we draw it as one, and then walk on it. It is used in chapters 8 and 22, and
it is the same object both times.

    beta = 0.5 * (1 + sqrt(1 + 8*rho/sigma^2));  multiplier = beta/(beta-1)

Those two lines are the paper's own formulas (its equations 3 and 6). The
viewer never sees them -- only the shape they make.
"""
import numpy as np
from manim import (
    VMobject, VGroup,
    Surface, ThreeDAxes, VGroup, Text, Dot3D, Line3D, Line, Sphere,
    UP, DOWN, LEFT, RIGHT, OUT, IN, ORIGIN, DEGREES, color_gradient,
)
from lib.theme import MUTED, CHALK, WAIT, MONEY, TRIGGER, FONT, T_SMALL

SIG_LO, SIG_HI = 0.08, 0.45      # choppiness, as a fraction per year
RHO_LO, RHO_HI = 0.015, 0.09     # cost of capital, as a fraction per year
MULT_CAP = 4.2


def multiplier(sigma, rho):
    beta = 0.5 * (1.0 + np.sqrt(1.0 + 8.0 * rho / (sigma ** 2)))
    return min(beta / (beta - 1.0), MULT_CAP)


def axes():
    return ThreeDAxes(
        x_range=[0, 1, 0.25], y_range=[0, 1, 0.25], z_range=[0, 1, 0.25],
        x_length=5.2, y_length=5.2, z_length=3.2,
        axis_config={"color": MUTED, "stroke_width": 2, "include_ticks": False,
                     "include_tip": False},
    )


def _u(sigma):
    return (sigma - SIG_LO) / (SIG_HI - SIG_LO)


def _v(rho):
    return (rho - RHO_LO) / (RHO_HI - RHO_LO)


def _w(m):
    return (m - 1.0) / (MULT_CAP - 1.0)


def point(ax, sigma, rho):
    return ax.c2p(_u(sigma), _v(rho), _w(multiplier(sigma, rho)))


def sheet(ax, resolution=32):
    def f(u, v):
        sigma = SIG_LO + u * (SIG_HI - SIG_LO)
        rho = RHO_LO + v * (RHO_HI - RHO_LO)
        return ax.c2p(u, v, _w(multiplier(sigma, rho)))

    s = Surface(f, u_range=[0, 1], v_range=[0, 1],
                resolution=(resolution, resolution),
                fill_opacity=0.82, stroke_width=0.9, stroke_color=MUTED,
                checkerboard_colors=[WAIT, TRIGGER])
    s.set_fill_by_value(axes=ax, colorscale=[(WAIT, 0.0), (TRIGGER, 0.55),
                                             (MONEY, 1.0)], axis=2)
    return s


def labels(ax):
    x = Text("choppier revenue →", font=FONT, font_size=T_SMALL, color=WAIT)
    y = Text("cheaper money →", font=FONT, font_size=T_SMALL, color=MONEY)
    z = Text("higher bar", font=FONT, font_size=T_SMALL, color=TRIGGER)
    return VGroup(x, y, z)


def gridlines(ax, n=7, colour=MUTED, opacity=0.35):
    """The faint wireframe he lays over a surface so the eye can read its shape."""
    lines = VGroup()
    for i in range(n + 1):
        t = i / n
        along_u = VMobject(color=colour, stroke_width=1.6, stroke_opacity=opacity)
        along_u.set_points_smoothly([
            ax.c2p(u, t, _w(multiplier(SIG_LO + u * (SIG_HI - SIG_LO),
                                      RHO_LO + t * (RHO_HI - RHO_LO))))
            for u in np.linspace(0, 1, 24)])
        along_v = VMobject(color=colour, stroke_width=1.6, stroke_opacity=opacity)
        along_v.set_points_smoothly([
            ax.c2p(t, v, _w(multiplier(SIG_LO + t * (SIG_HI - SIG_LO),
                                       RHO_LO + v * (RHO_HI - RHO_LO))))
            for v in np.linspace(0, 1, 24)])
        lines.add(along_u, along_v)
    return lines
