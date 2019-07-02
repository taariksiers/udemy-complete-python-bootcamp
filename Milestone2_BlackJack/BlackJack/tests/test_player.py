'''
Unit testing for Player. Run from this directory
'''

import unittest
import sys
sys.path.append("..")
from Player import player

class TestPlayer(unittest.TestCase):
    '''
    Unit test Asserts
    '''
    def setUp(self):
        self.name = 'Jose'
        self.balance = 100
        self.dealer = False
        self.test_player = player.Player(self.name, self.balance, self.dealer)

    def test_get(self):
        '''
        Test get dict
        :return: None
        '''
        test_player = self.test_player
        self.assertDictEqual(test_player.get(), {'name': test_player.get()['name'],
                                                 'balance': test_player.get()['balance'],
                                                 'dealer': test_player.get()['dealer']})

    def test_setup(self):
        '''
        Test setup
        :return: None
        '''
        test_player = self.test_player

        self.assertEqual(test_player.get()['balance'], self.balance)
        self.assertEqual(test_player.get()['name'], self.name)
        self.assertNotEqual(test_player.get()['balance'], str(self.balance))

    def test_increment(self):
        '''
        Test balance increase
        :return: None
        '''
        test_player = self.test_player
        initial_balance = test_player.get()['balance']
        inc_balance = 50

        success = test_player.increment(inc_balance)
        self.assertEqual(True, success)
        self.assertEqual(test_player.get()['balance'], initial_balance + inc_balance)

    def test_decrement(self):
        '''
        Test balance increase
        :return: None
        '''
        dec_balance = 50
        test_player = self.test_player

        success = test_player.decrement(dec_balance)
        new_balance = test_player.get()['balance']
        self.assertEqual(new_balance, self.balance - dec_balance)
        self.assertEqual(True, success)

        failure = test_player.decrement(test_player.get()['balance'] + 1)
        self.assertEqual(test_player.get()['balance'], new_balance)
        self.assertEqual(False, failure)

    def test_can_decrement(self):
        '''
        Can the amount be decremented
        :return: None
        '''
        dec_balance_one = 50
        dec_balance_two = 100
        dec_balance_three = 101
        test_player = self.test_player

        self.assertEqual(test_player.canDecrement(dec_balance_one), True)
        self.assertEqual(test_player.canDecrement(dec_balance_two), True)
        self.assertEqual(test_player.canDecrement(dec_balance_three), False)


if __name__ == '__main__':
    unittest.main()
