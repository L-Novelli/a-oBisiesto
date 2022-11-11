year = int(input('ingrese un año: '))


def bisiesto(year):
    
    if year % 4 != 0 or year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return False
    
    elif year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0:
        return True

if bisiesto(year):
    print(year, 'es bisiesto')
else:
    print(year, 'no es bisiesto')