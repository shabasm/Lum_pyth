a = int(input("Enter a number "))


def fac(f):
    fact = 1
    if a < 0:
        print("Enter a positive number")
    elif a == 0:
        print("You've entered Zero")
    else:
        for i in range(1, a + 1):
            fact = fact * i
    print("Factorial of", a, "is", fact)


fac(a)
