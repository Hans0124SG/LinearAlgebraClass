import math
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector:
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    # Problem: floating point precision problem
    def __add__(self, v):
        try:
            return Vector(list(map(lambda x, y: x + y, self.coordinates, v.coordinates)))
        except IndexError:
            raise IndexError('The two vectors have different dimensions')

    def __sub__(self, v):
        try:
            return Vector(list(map(lambda x, y: x - y, self.coordinates, v.coordinates)))
        except IndexError:
            raise IndexError('The two vectors have different dimensions')

    def __mul__(self, scalar):
        return Vector([Decimal(scalar) * x for x in self.coordinates])

    def get_magnitude(self):
        return sum([x ** Decimal('2') for x in self.coordinates]) ** Decimal('0.5')

    def get_unit_vector(self):
        try:
            magnitude = self.get_magnitude()
            return self * (Decimal('1.0') / magnitude)
        except ZeroDivisionError:
            raise ZeroDivisionError("Zero vector has no unit vector")

    def dot_product(self, v):
        return sum(list(map(lambda x, y: x * y, self.coordinates, v.coordinates)))

    def get_angle(self, v):
        try:
            cos = self.dot_product(v) / (self.get_magnitude() * v.get_magnitude())
            return math.acos(cos), math.acos(cos) / math.pi * 180
        except ZeroDivisionError:
            raise ZeroDivisionError("Zero vector has no unit vector")

