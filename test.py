from Vector import *

a = Vector([3.039, 1.879])
b = Vector([0.825, 2.036])

print(Vector.decompose(a, b)[0])

c = Vector([-9.88, -3.264, -8.159])
d = Vector([-2.155, -9.353, -9.473])

print(Vector.decompose(c, d)[1])
#
e = Vector([3.009, -6.172, 3.692, -2.51])
f = Vector([6.404, -9.144, 2.759, 8.718])

print(Vector.decompose(e, f, output=True))

# g = Vector([2.118, 4.827])
# h= Vector([0, 0])
#
# print(g.is_parallel(h))

