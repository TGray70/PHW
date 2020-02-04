class EquipWarehouse:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Name is: {self.name}"
    def to_give(self, name, *firms):
        print(name)
        for firm in firms:
            firm.to_take(name)

class Printer(EquipWarehouse):
    def __init__(self, name):
        super().__init__(name)
        self.speed = 5
    def __str__(self):
        return f"Name is: {self.name}"
    def my_list(self):
        return self.name

class Scaner(EquipWarehouse):
    def __init__(self, name):
        super().__init__(name)
        self.color = True
    def __str__(self):
        return f"Name is: {self.name}"

class xerox(EquipWarehouse):
    def __init__(self, name):
        super().__init__(name)
        self.speed = 10

class Firm:
    def __init__(self):
        self.having = []
    def to_take(self, name):
        self.having.append(name)

f1 = Firm
f2 = Firm
ew = EquipWarehouse
p = Printer('printer-A1010')
print(p.name)
s = Scaner('scaner-P78')
ew.to_give(p.name, f1, f2)
print(f1.having)