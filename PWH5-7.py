

f = open('7.txt', encoding="utf-8")
l = f.readlines()
#print('строк - ', len(l))
i = 1
res = []
summ = 0
while i <= len(l):
    str = l[i - 1].split()
    #print(str)
    i1 = 2
    a = int(str[2]) - int(str[3])
    summ = summ + a
    if a > 0:
        d = {a, str[0]}
        #print(d)
        res.append(d)
    #print(res)


    #print(summ)
    i = i + 1
    d = {round(summ / len(l)), 'average_profit'}
res.append(d)
f.close()
print(res)
