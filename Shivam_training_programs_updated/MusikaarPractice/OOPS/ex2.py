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


'''Output
Balance is 10000
Deposit OR Withdraw? Type D for Deposit OR W for Withdraw OR E for Exit: d
Enter amount for deposit: 10000
Deposited 10000 and Total balance is 20000 
Balance is 20000
Deposit OR Withdraw? Type D for Deposit OR W for Withdraw OR E for Exit: w
Enter amount for withdraw: 25000
Not enough balance
Balance is 20000
Deposit OR Withdraw? Type D for Deposit OR W for Withdraw OR E for Exit: w
Enter amount for withdraw: 15000
Withdrew 15000 and Total balance is 5000 
Balance is 5000
'''