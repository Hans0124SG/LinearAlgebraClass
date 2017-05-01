from Vector import *

a = Vector([-7.579, -7.88])
b = Vector([22.737, 23.64])

print(a.is_parallel(b))

c = Vector([2.029, 9.97, 4.172])
d = Vector([-9.231, -6.639, -7.245])

print(c.is_parallel(d))

e = Vector([-2.328, -7.284, -1.214])
f = Vector([-1.821, 1.072, -2.94])

print(e.is_orthogonal(f))

g = Vector([2.118, 4.827])
h= Vector([0, 0])

print(g.is_parallel(h))