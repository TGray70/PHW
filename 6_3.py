
#name = "name"
#surname = "surname"
class Worker:
    #def __init__(self, name, surname, position, _income):
        #self.name = name
        #self.surname = surname
        #self.position = position
        #self._income = _income
        name = "name"
        surname = "surname"
        position = "position"
        _income = {'wage':0, 'bonus':0}

class Position(Worker):
    def get_full_name(self):
        self.name = input('Введите имя сотрудника: ')
        self.surname = input('Введите фамилию сотрудника: ')
    def get_total_income(self):
        self._income = {'wage': input('Введите оклад: '), 'bonus': input('Введите премию: ')}

a = Position()
a.get_full_name()
a.get_total_income()

c = Position()
print(c.name, c.surname, c._income)

b = Worker()
print(b.name, b.surname, b._income)


   #     {'wage': 0, 'bonus': 0}