class OwnErr(Exception):
    def __init__(self,txt):
        self.txt = txt

indata = input("Введите пооожительное число: ")
try:
    indata = int(indata)
    if indata < 0:
        raise OwnErr('Число отрицательное!')
except ValueError:
    print('Это не число!')
except OwnErr as err:
    print(err)
else:
    print('Все хорошо')