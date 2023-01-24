try:
    a = int(input('Enter A:'))
    b = int(input('Enter B:'))
    c = a/b
except ZeroDivisionError:
    print('ERROR, Division by "Zero"')
else:
    print('Result is ', c)

try:
    a = int(input('Enter A:'))
    b = int(input('Enter B:'))
    c = a/b
    print('Result is ', c)
finally:
    print('Division')
    print('Successful')

try:
    a = int(input('Enter A:'))
    b = int(input('Enter B:'))
    c = a/b
    print('Result is ', c)
except ZeroDivisionError:
    print('Error occured')
finally:
    print('Division')
    print('Successful')
