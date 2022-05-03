import datetime

print("Data for first date")
year1 = int(input("Enter Year:"))
month1 = int(input("Enter Month:"))
day1 = int(input("Enter Day:"))
first_date = datetime.date(year1, month1, day1)
print("Data for second date")
year2 = int(input("Enter Year:"))
month2 = int(input("Enter Month:"))
day2 = int(input("Enter Day:"))
second_date = datetime.date(year2, month2, day2)

# For Date and Time both
# f= datetime.datetime(2023,12,5,16,45)
# s= datetime.datetime(2024,12,7,12,4)
diff = second_date - first_date
print(diff)
