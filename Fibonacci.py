n = int(input("Enter number "))
a = 0
b = 1
print(a)
print(b)
while b <= n:
    c = a+b
    if c <= n:
        print(c)
    a = b
    b = c
