f = open('1.txt', 'w')
str = '1'
while str != '':
    str = input('Введите строку, закончить - "ENTER" ',)
    f.write(str)

f.close()
print('Спасибо, файл закрыт')
