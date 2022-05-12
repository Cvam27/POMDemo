li1 = []
li2 = []
li3 = []
for i in range(0, 100):
    li1.append(i)
# print(li1)
for i in li1:
    for j in li1:
        if i ** 2 == j ** 3:
            print(f"Square of {i, i ** 2} is equal to cube of {j, j ** 3}")
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


'''
output

Square of (0, 0) is equal to cube of (0, 0)
Square of (1, 1) is equal to cube of (1, 1)
Square of (8, 64) is equal to cube of (4, 64)
Square of (27, 729) is equal to cube of (9, 729)
Square of (64, 4096) is equal to cube of (16, 4096)'''