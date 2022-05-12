name = str(input("Enter name of Student : "))
standard = int(input("Enter Standard : "))
maths = int(input("Enter Maths marks : "))
science = int(input("Enter Science marks : "))
ss = int(input("Enter SS marks : "))
english = int(input("Enter English marks : "))

if (maths < 0 or maths > 50) or (ss < 0 or ss > 50) or (science < 0 or science > 50) or (english < 0 or english > 50):
    print("Marks should be below 50")
else:
    percentage = ((maths + ss + science + english) / 2)
    if (maths < 18) or (science < 18) or (ss < 18) or (english < 18):
        print("Fail")
    else:
        if percentage < 35:
            print("Fail", percentage)
        elif 35 <= percentage < 60:
            print(f"Second Class with {percentage} for {name} in standard {standard}")
        elif 60 <= percentage < 70:
            print(f"First Class with {percentage} for {name} in standard {standard}")
        else:
            print(f"Distinction with {percentage} for {name} in standard {standard}")



'''
Output
Enter name of Student : Jack
Enter Standard : 6
Enter Maths marks : 55
Enter Science marks : 44
Enter SS marks : 45
Enter English marks : 34
Marks should be below 50

Enter name of Student : Ryan
Enter Standard : 3
Enter Maths marks : 33
Enter Science marks : 34
Enter SS marks : 44
Enter English marks : 43
Distinction with 77.0 for Ryan in standard 3
'''