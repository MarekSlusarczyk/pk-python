x = int(input('Podaj x: '))

if x > 12:
    print('x jest większy niż 12')
elif x > 6 & x <= 12:
    print('x jest z przedziału (6; 12]')
elif x > 0 & x <= 6:
    print('x jest z przedziału (0; 6]')
else:
    print('x jest mniejszy lub równy 0')