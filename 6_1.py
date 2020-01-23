import time

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running():
        i = True
        while i == True:
            print('КРАСНЫЙ')
            time.sleep(7)
            print('желтый')
            time.sleep(2)
            print('ЗЕЛЁНЫЙ')
            time.sleep(10)

r = TrafficLight
r.running()
