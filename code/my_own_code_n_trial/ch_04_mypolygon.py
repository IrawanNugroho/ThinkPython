"""
It means that swampy is installed as a package.
Package is a collection of modules.
"""
from swampy.TurtleWorld import *



world = TurtleWorld()
bob = Turtle()
print(bob)

# draw a square by using for
for i in range(4):
	fd(bob, 100)
	lt(bob)

for i in range(4):
	print('Hello')

wait_for_user()