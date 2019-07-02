class Account():
    """
    Basic Bank account operations.
    """
    owner = ''
    balance = 0

    def __init__(self, **kwargs):
        """
        Init with account owner and balance.
        :param name: string
        :param balance: float
        """
        self.owner = kwargs.get('owner').capitalize()
        self.balance = kwargs.get('balance')

    def deposit(self, deposit):
        """
        Deposit money into account.
        :param deposit: float
        :return: float
        """
        self.balance += deposit
        return self.balance

    def withdraw(self, withdrawal):
        """
        Withdraw money from account.
        :param withdrawal: float
        :return: mixed float|bool - False if withdrawal exceeds available balance else return depleted balance.
        """
        if withdrawal <= self.balance:
            self.balance -= withdrawal
            return self.balance
        else:
            return False

    def __str__(self):
        """
        Print account owner and balance.
        :return: string
        """
        return f'{self.owner.lower().capitalize()} Account Balance: {self.balance}'
