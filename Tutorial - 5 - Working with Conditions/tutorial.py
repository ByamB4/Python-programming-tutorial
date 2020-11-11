age = 20
university = False

if age >= 20 or university:
    print('Age is greater than 20 also in university')

elif age > 18 and not university:
    print('Age is greater than 18 also not going university')

else:
    print('Something is wrong')
