li1 = []
for i in range(100, 1000):
    for j in range(100, 1000):
        mul = str(i * j)
        if mul == mul[::-1]:
            li1.append(mul)
        else:
            pass
print("Min Palindrome is :" + min(li1), "Max Palindrome is " + max(li1))

'''
output
Min Palindrome is :101101 Max Palindrome is 99999
'''
