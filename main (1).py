class BankAccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self._account_number=account_number
    self._account_holdername=account_holder_name
    self._balance=initial_balance
  def deposit(self,amount):
    if amount>0:
      self._balance+=amount
      print("Deposit ₹ {}.New Balance:₹{}".format(amount,self._balance))
    else:
      print("Invalid deposit number or insufficient amount.")
  def withdraw(self,amount):
    if amount>0 and amount<=self._balance:
      self._balance-=amount
      print("Withdraw ₹{}.New balance: ₹{}".format(amount,self._balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")
  def display_balance(self):
    print("Account balance for {}(Account#{}): ₹{}".format(self._account_holdername,self._account_number,self._balance))
account=BankAccount(account_holder_name="Kumaresan",
account_number="12345678",
initial_balance=500)

account.display_balance()
account.deposit(500)
account.withdraw(100)
account.display_balance()
