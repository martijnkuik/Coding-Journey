class Bank_Account:   
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin_number = pin
        self.balance = balance

    def __str__(self):
        return f'Bank Account: {self.name}, last name: {self.last_name}, Account id: {self.account_id}, Account type: {self.pin_number}, Balance: {self.balance}'

my_city = Bank_Account('Martijn', 'Kuik', '4234237894', 'BigBucks', '3423', '32.347')

print(Bank_Account)


"""# Bank Accounts 🏦
# Codédex

class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  
  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance

  def withdraw(self, amount):
    self.balance = self.balance - amount
    return self.balance

  def display_balance(self):
    print(f"${self.balance}")

checking_account = BankAccount("Jane", "Doe", 13243546, "checking", 0000, 250.00)

checking_account.deposit(100)

checking_account.display_balance()

checking_account.withdraw(50)

checking_account.display_balance()"""
