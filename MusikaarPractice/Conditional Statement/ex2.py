num = [12, 43, 23, 67, 11, 45, 54]
maxmm = 0
for i in num:
    for j in num:
        if j > maxmm:
            maxmm = i
        else:
            continue

print(maxmm)
