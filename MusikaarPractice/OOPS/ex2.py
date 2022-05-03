class Bank:
    @staticmethod
    def deposit(balance, amount):
        return balance + amount

    @staticmethod
    def withdraw(balance, amount):
        return balance - amount

    @staticmethod
    def view_balance(balance):
        return balance


bal = 10000
piggy_bank = Bank()
while True:

    print("Balance is", piggy_bank.view_balance(bal))

    # ask for deposit/withdraw
    operation_type = input("Deposit OR Withdraw? Type D for Deposit OR W for Withdraw OR E for Exit: ").upper()

    if operation_type == "d" or operation_type == "D":
        try:
            amount_deposit = int(input("Enter amount for deposit: "))
            bal = piggy_bank.deposit(bal, amount_deposit)
            print(f"Deposited {amount_deposit} and Total balance is {bal} ")
        except:
            print("String is not allowed, Please enter numbers only")
    elif operation_type == "w" or operation_type == "W":
        if bal <= 0:
            print("Zero Balance")
        else:
            try:
                amount_withdraw = int(input("Enter amount for withdraw: "))
                if amount_withdraw > bal:
                    print("Not enough balance")
                else:
                    bal = piggy_bank.withdraw(bal, amount_withdraw)
                    print(f"Withdrew {amount_withdraw} and Total balance is {bal} ")
            except:
                print("String is not allowed, Please enter numbers only")
    elif operation_type == "e" or operation_type == "E":
        break
    else:
        print("Invalid operation type")
