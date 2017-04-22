class Vector:
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
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
        return Vector([scalar * x for x in self.coordinates])

    def get_magnitude(self):
        return sum([x ** 2 for x in self.coordinates]) ** 0.5

    def get_unit_vector(self):
        try:
            magnitude = self.get_magnitude()
            return self * (1.0 / magnitude)
        except ZeroDivisionError:
            raise ZeroDivisionError("Zero vector has no unit vector")
