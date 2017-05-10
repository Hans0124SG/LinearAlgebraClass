from Vector import *

# a = Vector([3.039, 1.879])
# b = Vector([0.825, 2.036])
#
# print(Vector.decompose(a, b)[0])

c = Vector([8.462, 7.893, -8.187])
d = Vector([6.984, -5.975, 4.778])

print(c.cross_product(d))

e = Vector([-8.987, -9.838, 5.031])
f = Vector([-4.268, -1.861, -8.866])

print(e.cross_product(f).get_magnitude())

g = Vector([1.5, 9.547, 3.691])
h= Vector([-6.007, 0.124, 5.772])

print(g.cross_product(h).get_magnitude() / 2)
