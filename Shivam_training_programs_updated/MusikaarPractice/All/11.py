

set1 = {i for i in range(1, 100) if i % 3 == 0}
set2 = {i for i in range(1, 100) if i % 7 == 0}
print("Set 1 : ", sorted(set1), "\n" "Set 2: ", sorted(set2))


set3 = {i for i in set1 if i in set2}
print("Final Set", sorted(set3))


'''
output
Set 1 :  [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99] 
Set 2:  [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
Final Set [21, 42, 63, 84]
'''