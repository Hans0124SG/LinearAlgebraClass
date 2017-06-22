# from Line import Line
# a = Vector([3.039, 1.879])
# b = Vector([0.825, 2.036])
#
# print(Vector.decompose(a, b)[0])
from Plane import Plane

plane1 = Plane(normal_vector=[-0.412, 3.806, 0.728], constant_term=-3.46)
plane2 = Plane(normal_vector=[1.03, -9.515, -1.82], constant_term=8.65)
print(plane1.is_parallel(plane2))
print(plane1.is_equal(plane2))

plane3 = Plane(normal_vector=[2.611, 5,528, 0.283], constant_term=4.6)
plane4 = Plane(normal_vector=[7.715, 8.306, 5.432], constant_term=3.76)
print(plane3.is_parallel(plane4))
print(plane3.is_equal(plane4))

plane5 = Plane(normal_vector=[-7.926, 8.625, -7.212], constant_term=-7.95)
plane6 = Plane(normal_vector=[-2.642, 2.875, -2.404], constant_term=-2.443)
print(plane5.is_parallel(plane6))
print(plane5.is_equal(plane6))

# line1 = Line(normal_vector=[4.046, 2.836], constant_term=1.21)
# line2 = Line(normal_vector=[10.115, 7.09], constant_term=3.025)
# print(line1.find_intersection(line2))
#
# line3 = Line(normal_vector=[7.204, 3.182], constant_term=8.68)
# line4 = Line(normal_vector=[8.172, 4.114], constant_term=9.883)
# print(line3.find_intersection(line4))
#
# line5 = Line(normal_vector=[1.182, 5.562], constant_term=6.744)
# line6 = Line(normal_vector=[1.773, 8.343], constant_term=9.525)
# print(line5.find_intersection(line6))