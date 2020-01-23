
class Road:
    th = 5
    mass = 50
    
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self):
        #self.length = length
        #self.width = width
        return round(self._length * self._width * self.mass * self.th / 1000)

n_road1 = Road(1000, 10)
print(n_road1._length)
print(n_road1.calc_weight(), 'тонн, нужно асфальта на первую дорогу.')
