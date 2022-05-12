# Using generator to print value


def div(n):
    for i in range(1, n):
        if i % 7 == 0:
            yield i
            yield i * 2


print(list(div(100)))


'''Output
[7, 14, 14, 28, 21, 42, 28, 56, 35, 70, 42, 84, 49, 98, 56, 112, 63, 126, 70, 140, 77, 154, 84, 168, 91, 182, 98, 196]
'''