
f = open('3.txt', encoding="utf-8")
l = f.readlines()
#print('строк - ', len(l))
i = 1
sum = 0
while i <= len(l):
    str = l[i - 1].split()
    sum = sum + float(str[1])
    if float(str[1]) < 20000:
        print(str[0])

    i = i + 1
f.close()
mid = round(sum / len(l), 2)
print('средняя зарплата: ', mid)
