
class Stationery:
    title = 'title'

    def draw(self):
        print('запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print('запуск отрисовки ручкой')

class Pencil(Stationery):
    
    def draw(self):
        print('запуск отрисовки карандашом')

class Handle(Stationery):
    def draw(self):
        print('запуск отрисовки маркером')

s = Stationery()
s.draw()
a = Pen()
a.draw()
p= Pencil()
p.draw()
h = Handle()
h.draw()