class Error(Exception):
    pass
class InvalidInputType(Error):
    pass

try:
    sal = int(input("Enter salary : "))
    if sal < 500:
        print("pass")
    # else:
    #     raise InvalidInputType
except InvalidInputType as ie:
    print("DOne")
