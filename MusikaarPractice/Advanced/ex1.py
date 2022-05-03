# Using generator to print value


def div(n):
    for i in range(1, n):
        if i % 7 == 0:
            yield i
            yield i * 2


print(list(div(100)))
