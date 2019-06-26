import sys, unittest
sys.path.append('../')

from Bank import Bank


class TestBank(unittest.TestCase):
    """
    Unit tests for Bank Account
    """
    account = None
    owner = 'john'
    starting_balance = 100
    deposit = 100
    withdraw = 50
    withdraw_fail = 1000

    def setUp(self):
        self.account = Bank.Account(self.owner, self.starting_balance)

    def test_init(self):
        """
        Test initialisation
        :return:
        """

        self.assertEqual(str(self.account), f'{self.owner.capitalize()} Account Balance: {self.starting_balance}')
        self.assertEqual(self.owner.capitalize(), self.account.owner)
        self.assertEqual(self.starting_balance, self.account.balance)

    def test_deposit(self):
        """
        Test deposit functionality
        :return:
        """

        updated_balance = self.account.deposit(self.deposit)
        self.assertEqual(self.starting_balance + self.deposit, updated_balance)

    def test_withdraw(self):
        """
        Test withdraw positive flow
        :return:
        """

        updated_balance = self.account.withdraw(self.withdraw)
        self.assertEqual(self.starting_balance - self.withdraw, updated_balance)

    def test_failed_withdraw(self):
        """
        Test withdraw negative flow
        :return:
        """

        updated_balance = self.account.withdraw(self.withdraw_fail)
        self.assertEqual(self.starting_balance, self.account.balance)
        self.assertFalse(updated_balance)


if __name__ == '__main__':
    unittest.main()
