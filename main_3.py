Percent = list(range(1,101))
print(Percent)

for i in Percent:
    temp = i
    if (temp % 10 == 1) and temp != 11:
        print( temp, 'процент')
    elif  (1 < temp % 10 < 5) and ((temp < 12) or (temp > 14)):
        print ( temp, 'процента')
    else:
        print ( temp, 'процентов')
print ('end')