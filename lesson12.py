#data  name,gender,amount
#account
#deposit/withdrawal/check balance
#oop
#matatu --->number,driver,conductor,route
class Account:
    def __init__(self, full_name, acc_num, phone, balance):#method/function constructor
        self.full_name = full_name
        self.acc_num = acc_num
        self.phone = phone
        self.balance = balance

    def deposit(self ,amount):
        self.balance=self.balance+ amount
        print(f"Amount {amount} deposited successfully to account {self.acc_num}")

    def withdraw (self,amount):
        if self.balance>amount:
            print(f"Amount {amount}withdrawn successfully from account {self.acc_num}")
        else:
            print(f"Insufficient funds.The balance is: {self.balance}")

    def check_balance(self):
        print(f"Account balance  for {self.acc_num} is: {self.balance}")


baha_acc=Account("Iona Bahati","001","0102609452",1000)
willy_acc=Account("William Fondo","002","0721170376",2000)
baha_acc.deposit(200)
baha_acc.check_balance()
willy_acc.withdraw(20000)
willy_acc.check_balance()
willy_acc.deposit(3000)
willy_acc.check_balance()



