"""1.	Write a program which accepts a number as an argument and prints an ascending triangle pattern containing
character ‘*’. For example output of function pattern(5) should be following, * * * * * *

"""

n = 5
k = 4

for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
