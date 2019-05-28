# Bank Account - https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/05-Object%20Oriented%20Programming/04-OOP%20Challenge.ipynb

class Account():
    '''Basic Bank account operations'''
    owner = ''
    balance = 0

    def __init__(self, name, balance):
        '''Init with account owner and balance'''
        self.owner = name
        self.balance = balance

    def deposit(self, deposit):
        '''Put money in'''
        print('Money deposited.')
        self.balance += deposit

    def withdraw(self, withdrawal):
        '''Take money out'''
        if withdrawal > self.balance:
            print('Funds Unavailable!')
        else:
            print('Withdrawal accepted.')
            self.balance -= withdrawal

    def __str__(self):
        '''Print out the owner and balance'''
        return f'Account Owner: {self.owner.lower().capitalize()}\nAccount Balance: {self.balance}'

# print(help(Account))

jose = Account('jose', 0)
print(f'Initial State:\n{jose}\n---------------')
jose.deposit(100)
print(f'Deposit 100:\n{jose}\n---------------')
jose.withdraw(101)
print(f'Withdraw 101:\n{jose}\n---------------')
jose.withdraw(50)
print(f'Withdraw 50:\n{jose}\n---------------')