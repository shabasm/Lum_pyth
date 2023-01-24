n = int(input('Enter number:'))


def fib(f):
    a = 0
    b = 1
    print(a)
    print(b)
    while b <= n:
        c = a+b
        a = b
        b = c
        if c <= n:
            print(c)


fib(n)
