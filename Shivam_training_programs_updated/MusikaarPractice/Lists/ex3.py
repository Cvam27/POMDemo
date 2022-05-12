li1 = [22, 3, 554, 15, 23, 11, 1010, 12, 4, 26, 80, 121, 2020]
n = 0
len = len(li1)
for i in range(0, len):
    for j in range(i + 1, len):
        if li1[i] < li1[j]:
            n = li1[i]
            li1[i] = li1[j]
            li1[j] = n
print(li1)


'''Output
[2020, 1010, 554, 121, 80, 26, 23, 22, 15, 12, 11, 4, 3]
'''