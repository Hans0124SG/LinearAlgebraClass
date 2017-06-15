from Vector import *
from Line import Line
# a = Vector([3.039, 1.879])
# b = Vector([0.825, 2.036])
#
# print(Vector.decompose(a, b)[0])

line1 = Line(normal_vector=[4.046, 2.836], constant_term=1.21)
line2 = Line(normal_vector=[10.115, 7.09], constant_term=3.025)
print(line1.is_parallel(line2))
print(line1.basepoint)
print(line2.basepoint)

line3 = Line(normal_vector=[7.204, 3.182], constant_term=8.68)
line4 = Line(normal_vector=[8,172, 4.114], constant_term=9.883)
print(line3.is_parallel(line4))

line5 = Line(normal_vector=[1.182, 5.562], constant_term=6.744)
line6 = Line(normal_vector=[1.773, 8.343], constant_term=9.525)
print(line5.is_parallel(line6))