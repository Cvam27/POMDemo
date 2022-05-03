class Salary:
    @staticmethod
    def chef(hwage, hours, days, basic):
        return print(hwage * hours * days + basic)

    @staticmethod
    def waiter(mwage, tip, basic):
        return print(int(mwage + (tip * 0.05) + basic))

    @staticmethod
    def cleaner(mwage, exhours, exsalary, basic):
        return print(mwage + (exhours * exsalary) + basic)


hotel = Salary()

hotel.chef(50, 8, 22, 14000)
hotel.waiter(7000, 1500, 12000)
hotel.cleaner(5000, 13, 200, 7000)
