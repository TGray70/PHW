class Cell:
    def __init__(self, num):
        self.num = num
    def __repr__(self):
        return 'Cell{}'.format(self.num)
    def __str__(self):
        return '{}'.format(self.num)
    def __add__(self, other):
        return Cell(self.num + other.num)
    def __sub__(self, other):
        return Cell(self.num - other.num)
    def __mul__(self, other):
        return Cell(self.num * other.num)
    def __floordiv__(self, other):
        return Cell(self.num // other.num)

cell1 = Cell(7)
cell2 = Cell(3)

print(cell1)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 // cell2)