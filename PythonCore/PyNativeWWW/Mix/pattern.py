# for i in range(5):
#     for j in range(i):
#         print(i,end=" ")
#     print("\n")

# Inverted Triangle
# for i in range(5,0, -1):
#     for j in range(i,0,-1):
#         print(i, end="")
#     print("\n")

# flipped triangle

rows = 6

for row in range(1, rows):

    num = 1

    for j in range(rows, 0, -1):

        if j > row:

            print("", end=" ")

        else:

            print(num, end="")

            num += 1

    print(" ")


