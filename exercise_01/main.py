from BankAccount import BankAccount

# Instantiate a BankAccount object with a hardcoded account name and starting balance
account = BankAccount("Wally", 50.00)

# Perform some transactions
account.deposit(30.50)
account.withdraw(10.34)

# Print out the result of calling the get_balance method
print(account.get_balance())
