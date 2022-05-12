'''5.	Write a program to generate the Fibonacci sequence starting from 0. The function accepts any number as an argument (length of the output sequence) and generates the list of Fibonacci sequence.
Note: Two versions of program should be written, 1) using recursion and 2) using generators.
'''

# Fibonacci with Recursion
a = 0
b = 1


def gen(n):
    global a, b
    yield print(a)
    yield print(b)

    if n <= 1:
        yield n
        n - 1
    else:
        for i in range(n):
            fib = a + b
            a = b
            b = fib
            yield print(fib)


list(gen(10))


'''
output

0
1
1
2
3
5
8
13
21
34
55
89
'''