def sum(a, b):
    x = a + b
    return print("Sum is : ", x)


def sub(a, b):
    x = a - b
    return print("Sub is : ", x)


def mul(a, b):
    x = a * b
    return print("Mul is : ", x)


def div(a, b):
    x = a / b
    return print("Div is : ", x)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum(a, b)
sub(a, b)
mul(a, b)
div(a, b)
