"""
Exercise 4.3. Write an appropriately general set of functions that can draw shapes as in Figure 4.2.
Solution: http: // thinkpython. com/ code/ pie. py .
"""

from cmath import pi
from ch_04_case_study_interface_design import polyline, polygon
from swampy.TurtleWorld import *


def pie(t, n, length):
    """
    It isn't completed yet

    n   : number or pie slices
    """
    polygon(t, n, length)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

print(bob)

# star(bob, 50)
pie(bob, 50, 10)

die(bob)
wait_for_user()
