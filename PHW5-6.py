
def rs(s):
    sn = []
    for i in s:
        if s == '(':
            break
        else:
            sn.append(i)
    return sn

f = open('6.txt', encoding="utf-8")
l = f.readlines()
print('строк - ', len(l))
i = 1
while i <= len(l):
    str = l[i - 1].split()
    print(str)
    i1 = 1
    while i1 < len(str):
        str1 = str[i1]
        print(str1)
        i1 = i1 + 1
        a = rs(str1)
        print(a)
        #i2 = 1
        #while i2 <= len(str1):
            #if int(str[i2 - 1] != False:
                #c = str[i2-1]
                #i2 = 1

        #for c in str[i1].split():

                #print(c)

    i = i + 1
f.close()
r = dict([(1, 1), (2, 4)])
print(r)


