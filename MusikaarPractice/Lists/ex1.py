li1 = [1, 3, 4, 5, 6, 2, 10, 12, 55, 66, 99, 111, 180]
odd = []
even = []

for i in li1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)
