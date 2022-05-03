li1 = ['abcd', 11, 'ff', 'pp', 50, 13, 19, 'hh']
new_li = []


def value(n):
    for i in li1:
        if type(i) == str:
            new_li.append(i)

        else:
            mul = int(i) * int(n)
            new_li.append(mul)


n = input("Enter a number for product : ")
value(n)
print(new_li)
