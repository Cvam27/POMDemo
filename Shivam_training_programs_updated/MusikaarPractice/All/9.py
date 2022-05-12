import random

a = ["[", "]"]
li1 = []

a = ["[", "]"]
li1 = []

# for i in range(6):
#     shuffle = random.choice(a)
#     li1.append(shuffle)
#     # print(shuffle, end="")
# print(li1)


shuffle = ''.join((random.choice('[]') for x in range(4)))
print(shuffle)

for i in shuffle:
    if i == "[":
        for j in shuffle:
            if j == "]":
                pass
            else:
                pass
    print("OK")
