#import

f = open('2.txt')
l = f.readlines()
print('строк - ', len(l))
i = 1
while i <= len(l):
    str = l[i - 1].split()
    n = len(str)
    print('строка ', i, ' в ней слов ', n)
    i = i + 1
f.close()
