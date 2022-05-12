class handmadeException(Exception):
    pass


try:
    user_age = int(input("Enter age : "))
    user_gender = input("Enter gender : ")
    user_family_member = int(input("Enter family member count: "))
    if user_age >= 25 and user_gender == "male" and user_family_member < 5:
        print("Offer applicable")
    else:
        raise handmadeException

except ValueError:
    print("Please enter valid info")
except handmadeException as h:
    print("Condition not matching")


'''
Output
Enter age : 25
Enter gender : Male
Enter family member count: 5
Condition not matching

Enter age : 36
Enter gender : male
Enter family member count: 3
Offer applicable
'''