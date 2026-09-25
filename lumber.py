# Softwood dimensional lumber, by its nominal size.
#
# 'width' and 'height' are the nominal sizes in inches (a "2x4" is height 2,
# width 4) and 'length' is the length in inches, which is not dressed. What is
# modelled is the actual size, per ALSC PS 20: a nominal 1 in. is 3/4 in., 2 to
# 7 in. lose 1/2 in., and 8 in. and up lose 3/4 in.
#
# The width is along X, the length along Y and the height along Z, with one
# corner at the origin -- so a piece cut to length from a board is in that
# board's own coordinates.
import cadquery as cq

width = 4
height = 2
length = 120


def actual(nominal):
    """The dressed size of a nominal dimension, in millimetres."""
    if nominal == 1:
        return (nominal - 0.25) * 25.4
    if nominal >= 8:
        return (nominal - 0.75) * 25.4
    return (nominal - 0.5) * 25.4


real_width = actual(width)
real_height = actual(height)
real_length = length * 25.4

result = (
    cq.Workplane("XY")
    .box(real_width, real_length, real_height)
    .translate((real_width / 2.0, real_length / 2.0, real_height / 2.0))
    # Milled lumber has its long edges eased.
    .edges("|Y")
    .fillet(3.2)
)

show_object(result)
