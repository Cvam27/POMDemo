class calc:
    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b


try:
    a = int(input("Enter 1st value: "))
    b = int(input("Enter 2nd value: "))
    real_calc = calc()

    print("Addition is ", real_calc.sum(a, b))
    print("Subtraction is ", real_calc.sub(a, b))

except Exception:
    print("Enter integer/float value only")
