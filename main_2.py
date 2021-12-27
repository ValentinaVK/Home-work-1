# 1 часть задания
list = [x**3 for x in range(1,1000,2)]
print(list)

a = 0
for i in list:
    summa = 0
    while i > 0:
        summa += i % 10
        i //= 10
    if summa % 7 == 0:
        a += i
print(a)

# 2 часть задания

list = [x+17 for x in list]
print(list)

a = 0
for i in list:
    temp = i
    summa = 0
    while temp > 0:
        summa += temp % 10
        temp //= 10
    if summa % 7 == 0:
        a += i
print(a)