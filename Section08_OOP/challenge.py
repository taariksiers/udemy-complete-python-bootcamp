class Account():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        # self.balance += amount
        return 'Deposit Accepted'

    def withdrawal(self, amount):
        if (amount <= self.balance):
            self.balance = self.balance - amount
            # self.balance -= amount
            return 'Withdrawal Accepted'
        else:
            return 'Funds Unavailable!'

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'

acct1 = Account('Jose', 100)
# print(acct1)

print(f'Account owner is: {acct1.owner}')
print(f'Balance is: ${acct1.balance}')

dep = acct1.deposit(50)
print(dep)

withdraw = acct1.withdrawal(150)
print(withdraw)
print(f'New Balance is: ${acct1.balance}')

withdraw = acct1.withdrawal(1)
print(withdraw)

print(f'New Balance is: ${acct1.balance}')
