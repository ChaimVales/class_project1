class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
   
    
    def withdraw(self,amount):
        if self.balance - amount < 0:
            print("Not enough to pull")
        else:
            self.balance -= amount  
  
    
    def get_balance(self):
        return self.balance
    




