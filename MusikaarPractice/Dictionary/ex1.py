li1 = [2, 3, 44, 55, 33, 111, 1010, 1, 4, 66, 8080, 121, 2020]
d = dict()
for i in range(len(li1)):
    d[li1[i]] = len(str(li1[i]))
    print(f"{len(str(li1[i]))} digit number = {li1[i]}")

print(d)
