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
        self.balance += deposit
        return True

    def withdraw(self, withdrawal):
        '''Take money out'''
        withdrawn = False
        if withdrawal <= self.balance:
            self.balance -= withdrawal
            withdrawn = True

        return withdrawn

    def __str__(self):
        '''Print out the owner and balance'''
        return f'{self.owner.lower().capitalize()} Account Balance: {self.balance}'
