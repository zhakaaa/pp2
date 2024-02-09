class bankAccount :
    def __init__(self,owner, balance) :
        self.owner = owner
        self.balance = balance
    
    def deposit(self,money) :
        self.balance+=money
        print(f"Money was credited to the balance in the amount of {money}tg\nCurrent balance: {self.balance}tg")
        
    def withdraw(self,money) :
        if money <= self.balance :
            self.balance-=money
            print(f"Money was withdrawn from the balance in the amount of {money}\nCurrent balance {self.balance}")
        else :
            print(f"Not enough money")

owner = input("Enter name: ")
balance = int(input("Enter balance: "))

bank_account = bankAccount(owner,balance)

money_to_deposit = int(input("Enter money to deposit: "))
bank_account.deposit(money_to_deposit)

money_to_withdraw = int(input("Enter money to withdraw: "))
bank_account.withdraw(money_to_withdraw)