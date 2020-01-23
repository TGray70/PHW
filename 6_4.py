class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
    
    def go(self):
        print('едем')
    def stop(self):
        print('стоим')
    def turn(self):
        print('поворачиваем на лево')
    def show_speed(self, speed):
        print('скорость - ', self.speed)

class TownCar(Car):
    def show_speed(self, speed):
        if self.speed > 60:
            print('превышаете на ', self.speed  - 60)
        else:
            print('скорость', self.speed)

class SportCar(Car):
    tip = 'sport'

class WorkCar(Car):
    def show_speed(self, speed):
        if speed > 40:
            print('превышаете на ', speed - 40)
        else:
            print('скорость', self.speed)

class PoliceCar(Car):
    dep = 'sity'

c = Car(50, 'red', 'Zhiguli', False)
print(c.speed, c.name, c.is_police)
c.go()
c.stop()
c.turn()
c.show_speed(50)

s = SportCar(90, 'black', 'Ferrary', False)
print(s.speed, s.name, s.is_police)
s.go()
s.stop()
s.turn()
s.show_speed(90)

t = TownCar(80, 'brown', 'Fiat', False)
print(t.speed, t.name, t.is_police)
t.go()
t.stop()
t.turn()
t.show_speed(80)

w = WorkCar(70, 'black', 'IRobot', False)
print(w.speed, w.name, w.is_police)
w.go()
w.stop()
w.turn()
w.show_speed(70)

p = PoliceCar(50, 'black', 'Ferrary', True)
print(p.speed, p.name, p.is_police)
p.go()
p.stop()
p.turn()
p.show_speed(50)

