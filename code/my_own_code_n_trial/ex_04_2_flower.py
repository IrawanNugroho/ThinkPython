"""
Exercise 4.2. Write an appropriately general set of functions that can draw flowers as in Figure 4.1.
Solution: http: // thinkpython. com/ code/ flower. py , also requires http: // thinkpython. com/ code/ polygon. py .
"""

from ch_04_case_study_interface_design import polyline, arc
from swampy.TurtleWorld import *

def star(t, length):
    """
    Accidentally I just create a star
    """
    polyline(t, length, 5, 145)


def flower(t, r, n):
    """
    It isn't completed yet
    But it is a good start!

    if n = 8 then the angle is 45
    if n = 9 then the angle is 50
    if n = 10 then best angle is 55
    if n = 12 then best angle is 60

    How is the formula?
    """
    angle = 360 / n
    for i in range(n):
        # always arc 90 degree and lt 90 degree to close quarter circle
        arc(t, r, 90)
        lt(t, 90)
        arc(t, r, 90)

        lt(t, 55)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

print(bob)

# star(bob, 50)
flower(bob, 50, 10)

die(bob)
wait_for_user()