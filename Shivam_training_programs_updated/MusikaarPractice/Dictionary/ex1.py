li1 = [2, 3, 44, 55, 33, 111, 1010, 1, 4, 66, 8080, 121, 2020]
d = dict()
for i in range(len(li1)):
    d[li1[i]] = len(str(li1[i]))
    print(f"{len(str(li1[i]))} digit number = {li1[i]}")

# print(d)



'''
Output
1 digit number = 2
1 digit number = 3
2 digit number = 44
2 digit number = 55
2 digit number = 33
3 digit number = 111
4 digit number = 1010
1 digit number = 1
1 digit number = 4
2 digit number = 66
4 digit number = 8080
3 digit number = 121
4 digit number = 2020

'''