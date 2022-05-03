set1 = {i for i in range(1, 100) if i % 3 == 0}
set2 = {i for i in range(1, 100) if i % 7 == 0}
print("Set 1 : ", sorted(set1), "\n" "Set 2: ", sorted(set2))

set3 = {i for i in set1 if i in set2}
print("Final Set", sorted(set3))
