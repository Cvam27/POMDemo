a = 0
b = 1

for i in range(10):
    fib = a + b
    a = b
    b = fib
    print(fib)
