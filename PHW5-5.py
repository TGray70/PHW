
f = open('5.txt', 'w+')

str = '3 3 4 55 78 3 90 14'
f.write(str)
f.seek(0)
str1 = f.read()
print(str1)
sm = 0
for i in str1.split():
   sm = sm + int(i)

f.close()
print(sm)

