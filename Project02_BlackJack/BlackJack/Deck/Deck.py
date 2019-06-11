import pydealer

class Deck():
    '''
    Operating with pydealer library
    Assuming only 1 player for now
    '''

    def __init__(self, name, balance):
        '''Init with account owner and balance'''
        self.owner = name
        self.balance = balance