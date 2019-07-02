class Player():
    '''
    Player class designed to hold balance and player name
    '''
    def __init__(self, name, balance, dealer=False):
        self.name = str(name)
        self.balance = int(balance)
        self.dealer = bool(dealer)

    def increment(self, amount):
        '''
        Increment the balance. On bet won or start game
        :return: float
        '''
        self.balance += abs(amount)
        return True

    def decrement(self, amount):
        '''
        Decrement the balance. On bet lost
        :return: float
        '''
        if not self.canDecrement(amount):
            return False

        self.balance -= abs(amount)
        return True

    def canDecrement(self, amount):
        '''
        Can we decrement? Useful for can you bet
        :param amount: int
        :return: boolean
        '''
        return abs(amount) <= self.balance
    
    def get(self):
        '''
        Dict represenation of class with pertinent gaming vars
        :return: dict
        '''
        return {'name': self.name, 'balance': self.balance, 'dealer': self.dealer}

    def __str__(self):
        '''
        Simply return dictionary with name and balance
        :return: string
        '''
        return f'Player {self.name} has balance {self.balance}'



# player = Player('Jose', 101, False)
#
# print(type(player))
# print(player)
# print(player.get()['balance'])
# player.increment(55);
# print(player.get()['balance'])
