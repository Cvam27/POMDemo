li1 = [55, 22, 77, 44, 58, 90, 30, 72]
len1 = len(li1)


for i in range(0, len1):
    if li1[i] % 2 != 0:
        print(li1[i])
    else:
        print(li1[i] * 3)



'''Output
55
66
77
132
174
270
90
216
'''