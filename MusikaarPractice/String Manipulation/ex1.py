word = "banana"
new = []
counter = []

for i in word:
    count = 0
    for j in word:
        if i == j:
            count = count + 1

    final = dict((zip(str(i), str(count))))
    print(final)
    # li1 = []
    # for i in final:
    #     if i not in li1:
    #         li1.append(i)
    #     else:
    #         pass
    # print(li1)

