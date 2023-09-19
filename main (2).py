class BankAccount:
    def __init__(self, balance):
        self.balance = balance
      
    def deposit(self, amount):
        self.balance += amount
      
    def withdraw(self, amount):
        self.balance -= amount
      
    def get_balance(self):
        return self.balance
      
class Bank:
    def __init__(self):
        self.accounts = {}
      
    def add_account(self, account_number, balance):
        self.accounts[account_number] = BankAccount(balance)
      
    def deposit(self, account_number, amount):
        self.accounts[account_number].deposit(amount)
      
    def withdraw(self, account_number, amount):
        self.accounts[account_number].withdraw(amount)
      
    def get_balance(self, account_number):
        return self.accounts[account_number].get_balance()
      
bank = Bank()

bank.add_account('1234', 500)
bank.deposit('1234', 100)
bank.withdraw('1234', 50)
print(bank.get_balance('1234'))


