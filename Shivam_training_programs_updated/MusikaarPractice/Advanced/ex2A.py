def deco(func):
    def identifier(usinput):
        uitype = str(usinput)
        if uitype != int | float:
            uitype = "'" + uitype + "'"
            return print(f"{uitype} type is {type(usinput)}")
        else:
            return print(f"{uitype} type is {type(usinput)}")

    return identifier


@deco
def summ(uinput):
    return type(uinput)


uinp = eval(input("Enter something"))
summ(uinp)

# summ(1000.10)
# summ(10)
# summ('ABC')
# summ(True)
