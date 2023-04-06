"""
It means that swampy is installed as a package.
Package is a collection of modules.
"""
from swampy.TurtleWorld import *
from math import pi

def square(t, length):
	"""
	t 		: turtle object
	length	: the length of square side
	"""
	
	for i in range(4):
		fd(t, length)
		lt(t)


def polygon(t, length, n):
	"""
	t 		: turtle object
	length	: the length of side
	n 		: n-sided of regular polygon
	"""

	for i in range(n):
		fd(t, length)
		lt(t, 360/n)


def polygon(t, length, n):
	"""
	An overwrite polygon by using polyline.

	t 		: turtle object
	length	: the length of side
	n 		: n-sided of regular polygon
	"""

	angle = 360 / n
	polyline(t, length, n, angle)


def polyline(t, length, n, angle):
	"""
	t 		: turtle object
	length	: the length of side
	n 		: n-sided of regular polygon
	angle 	: a custom degree of node

	Actually I don't understand the concepts of polyline.
	Since I can create an open polygon with random degree.
	While polygon is always completely close.
	"""

	for i in range(n):
		fd(t, length)
		lt(t, angle)


def my_circle(t, r):
	"""
	t 		: turtle object
	r 		: radius
	"""
	circumference = 2*pi*r
	length = circumference / 360
	
	polygon(t, length, 360)


def circle(t, r):
	"""
	t 		: turtle object
	r 		: radius
	
	n 		: line segment to draw a circle. it's not common to put it as a argument.
	
	Rather than clutter up the interface, 
	it is better to choose an appropriate value of n depending on circumference.
	Just a little bit faster than my own circle.
	"""
	circumference = 2*pi*r
	n = int(circumference / 3) + 1
	length = circumference / n
	
	polygon(t, length, n)


def circle(t, r):
	"""
	Overwrite circle by using arc
	arc is written by using polyline

	t 		: turtle object
	r 		: radius
	"""
	arc(t, r, 360)

	# I just want to know which circle I call!
	print('This is arc circle')



def arc(t, r, angle):
	"""
	t 		: turtle object
	r 		: radius
	angle 	: the degree of circle fraction
	"""

	circumference = 2*pi*r
	arc_length = circumference * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	
	for i in range(n):
		fd(t, step_length)
		lt(t, step_angle)


def arc(t, r, angle):
	"""
	An overwrite arc by using polyline.
	Is it correct to call it overwrite?

	t 		: turtle object
	r 		: radius
	angle 	: the degree of circle fraction
	"""

	circumference = 2*pi*r
	arc_length = circumference * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	
	polyline(t, step_length, n, step_angle)

	# I just want to know which arc I call
	print('This is polyline arc')


if __name__ == '__main__' :
	world = TurtleWorld()
	bob = Turtle()
	print(bob)
	# square(bob, length = 150)
	# polygon(bob, length = 100, n = 5)
	# polyline(bob, length = 100, n = 5, angle = 360/5)
	circle(bob, 100)
	# arc(bob, 100, 180)
	# my_arc(bob, 100, 180)


	for i in range(4):
		print('Hello')

	wait_for_user()