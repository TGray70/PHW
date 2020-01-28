a = [[1, 2],[3, 4]]
print(a[1][1])

class Matrix:
    def __init__(self, s):
        self.s = s
    def __repr__(self):
        return 'Matrix{}'.format(self.s)
    def __str__(self):
        return '{}'.format(self.s)

    def __add__(self, other):
        return Matrix(self.s[0][0] + other.s[0][0], self.s[0][1] + other.s[0][1], self.s[1][0] + other.s[1][0], self.s[1][1] + other.s[1][1])


m = Matrix([[1, 2], [1, 2]])
m1 = Matrix([[1, 2], [1, 2]])
print(m)
print(m[0][1])
print(m1 + m)
