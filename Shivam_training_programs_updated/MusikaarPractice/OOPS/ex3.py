class Salary:
    @staticmethod
    def chef(hwage, hours, days, basic):
        return print("Chef's salary is ", hwage * hours * days + basic)

    @staticmethod
    def waiter(mwage, tip, basic):
        return print("Waiter's salary is ",int(mwage + (tip * 0.05) + basic))

    @staticmethod
    def cleaner(mwage, exhours, exsalary, basic):
        return print("Cleaner's salary is ",mwage + (exhours * exsalary) + basic)


hotel = Salary()

hotel.chef(50, 8, 22, 14000)
hotel.waiter(7000, 1500, 12000)
hotel.cleaner(5000, 13, 200, 7000)


'''
Output
Chef's salary is  22800
Waiter's salary is  19075
Cleaner's salary is  14600


'''