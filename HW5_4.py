
r = {1: "один", 2: 'два', 3: 'три', 4: 'четыре'}
print(r[1])
a = []
ff = open('n4.txt', 'w', encoding="utf-8")
with open('4.txt') as f:
    l = f.readlines()
    print('строк - ', len(l))
    i = 1
    while i <= len(l):
        str = l[i - 1].split()
        print(str)
        str.remove(str[0])
        r1 = r[i]
        print(r1)

        str.insert(0, r1)

        print(str)
        str1 = ' '.join(str)
        ff.write(str1)

        i = i + 1
ff.close()
