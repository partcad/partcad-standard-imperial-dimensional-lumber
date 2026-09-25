# A plywood panel, by its nominal thickness.
#
# 'width' (along X) and 'length' (along Y) are in inches, and so is the nominal
# 'thickness' (along Z); the actual thickness is 1/32 in. less, which is why the
# panel sold as "3/4 in." is labelled "23/32 in.". One corner is at the origin.
import cadquery as cq

width = 48
length = 48
thickness = 0.5

real_width = width * 25.4
real_length = length * 25.4
real_thickness = (float(thickness) - 1.0 / 32.0) * 25.4

result = (
    cq.Workplane("XY")
    .box(real_width, real_length, real_thickness)
    .translate((real_width / 2.0, real_length / 2.0, real_thickness / 2.0))
)

show_object(result)
