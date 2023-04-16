class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        if isinstance(other, Vector):
            # Vector-vector addition
            return Vector([a + b for a, b in zip(self.values, other.values)])
        if type(other) in (int, float):
            # Vector-scalar addition
            return Vector([a + other for a in self.values])
        return NotImplemented

    def __radd__(self, other):
        if type(other) in (int, float):
            return Vector([a + other for a in self.values])
        return NotImplemented


v1 = Vector([1, 2, 3])
v2 = v1 + 2  # Creates the vector [3, 4, 5]
v3 = Vector([1, 2, 3])
v4 = 2 + v1