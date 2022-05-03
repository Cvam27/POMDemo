li1 = []
li2 = []
li3 = []
for i in range(0, 100):
    li1.append(i)
# print(li1)
for i in li1:
    for j in li1:
        if i ** 2 == j ** 3:
            print(f"Square of {i, i ** 2} == cube of {j, j ** 3}")
            li2.append(i)
            li2.append(j)

# for k in range(len(li2)):
#     for m in range(0,2):
#         li3.append(li2[m])
#
#         print(tuple(li3))
#
# # print(tuple(li3))


print(tuple(li2))
