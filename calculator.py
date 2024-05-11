def sum(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def product(x, y):
    return x * y


def division(x, y):
    return x / y


def power(x, y):
    return pow(x, y)


def remainder(x, y):
    return x % y


while True:
    a = input()
    if a == "break":
        print("calculated is done")
        break
    b = input()

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("type correct number")
        a = input()
        b = input()

        a = int(a)
        b = int(b)

    c = input("choose +, -, *, /, ^ or % ")

    if c == "+":
        print(sum(a, b))

    if c == "-":
        print(subtraction(a, b))

    if c == "*":
        print(product(a, b))

    if c == "/":
        print(division(a, b))

    if c == "^":
        print(power(a, b))

    if c == "%":
        print(remainder(a, b))
