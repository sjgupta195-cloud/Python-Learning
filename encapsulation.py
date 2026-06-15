class BankAccount :
    def __init__(self,balance):
        self._balance = balance
        
    
    def get_balance (self):
        return self._balance
    
    def deposit(self,amount):
        self._balance += amount
Account_balance = BankAccount(1000)


Account_balance.deposit(500) 


print(Account_balance.get_balance())
