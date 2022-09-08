class Vector:
    def __init__(self, param):

        if isinstance(param, int):
            self.values = [[float(i)] for i in range(param)]
        elif isinstance(param, tuple):
            assert len(param) == 2, 'Invalid tuple'
            assert param[0] < param[1], 'Invalid tuple'
            self.values = [[float(i)] for i in range(param[0], param[1])]
        else:
            self.values = param
        self.size = len(self.values)
        self.shape = (len(self.values), len(self.values[0]))

    def __mul__(self, other):
        if isinstance(other, (int, float)) is False:
            raise NotImplementedError('Multiplication of a scalar by a Vector is not defined here.')

        return Vector([[i * other for i in j] for j in self.values])


    def T(self):
        new_vector = []
        for i in range(self.shape[1]):
            new_vector.append([])
            for j in range(self.shape[0]):
                new_vector[i].append(self.values[j][i])
        return Vector(new_vector)

    def dot(self, other):
        assert self.shape == other.shape, 'Invalid shape'
        res = 0
        if (self.shape[0] != 1):
            for i in range(self.size):
                    res += self.values[i][0] * other.values[i][0]
        else:
            for j in range(self.shape[1]):
                res += self.values[0][j] * other.values[0][j]

        return res

    def __add__(self, other):
        assert self.shape == other.shape, 'Invalid shape'
        new_vector = []
        for i in range (self.size):
            new_vector.append([self.values[i][j] + other.values[i][j] for j in range(self.shape[1])])
        return Vector(new_vector)

    def __radd__(self, other):
        return __add__(self, other)

        
    def __sub__(self, other):
        assert self.shape == other.shape, 'Invalid shape'
        new_vector = []
        for i in range (self.size):
            new_vector.append([self.values[i][j] - other.values[i][j] for j in range(self.shape[1])])
        return Vector(new_vector)

    def __rsub__(self, other):
        return __sub__(self, other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)) is False:
            raise NotImplementedError('Division of a scalar by a Vector is not defined here.')
        return Vector([[i / other for i in j] for j in self.values])

    def __repr__(self):
        return str(self.values)

    def __str__(self):
        return str(self.values)
