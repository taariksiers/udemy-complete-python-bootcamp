"""
Just a unit test class for Deck class
py.test -v test_deck.py
"""
import io
import random
import sys
import unittest
from BlackJack.Deck.Deck import PlayingDeck

class TestDeck(unittest.TestCase):
    """
    Unit tests for Deck functionality
    """
    playing_deck = None

    def setUp(self):
        self.playing_deck = PlayingDeck()

    def test_init(self):
        """
        Test the initialisation
        :return:
        """
        self.assertEqual(52, len(self.playing_deck.player_deck))
        self.assertEqual(0, len(self.playing_deck.dealer_hand))
        self.assertEqual(0, len(self.playing_deck.player_hand))

    def test_str(self):
        """
        test string - a bit of a nothing test
        :return:
        """
        player_cards = self.playing_deck.deal_player(3)
        dealer_cards = self.playing_deck.deal_dealer(3)
        test_output = f'Player Cards: {[card.name for card in player_cards]}\n' \
            f'Dealer Cards: {[card.name for card in dealer_cards]}'
        self.assertEqual(str(self.playing_deck), test_output)

    def test_deal_player(self):
        """
        Test the player deal
        :return:
        """
        num_deal = random.randint(1, len(self.playing_deck.player_deck))
        cards = self.playing_deck.deal_player(num_deal)
        self.assertEqual(num_deal, len(cards))

    def test_deal_dealer(self):
        """
        Test the dealer deal
        :return:
        """
        num_deal = random.randint(1, len(self.playing_deck.player_deck))
        cards = self.playing_deck.deal_dealer(num_deal)
        self.assertEqual(num_deal, len(cards))

    def test_print(self):
        """
        Test print of cards
        :return:
        """
        num_deal = 2
        cards = self.playing_deck.deal_player(num_deal)
        stdout = sys.stdout
        sys.stdout = io.StringIO()

        self.playing_deck.print_cards(cards)
        output = sys.stdout.getvalue().strip().split("\n")
        sys.stdout = stdout

        self.assertEqual(num_deal, len(output))
        for i in range(0, num_deal):
            self.assertEqual(output[i], str(cards[i]))

    def test_get_card_values(self):
        """
        Test the card values method
        :return:
        """
        num_deal = random.randint(1, len(self.playing_deck.player_deck))
        deal = self.playing_deck.deal_dealer(num_deal)
        card_values = self.playing_deck.get_card_values(deal)
        self.assertGreater(card_values, 0)

    def test_restart(self):
        """
        Test deck restart
        :return:
        """
        num_deal = random.randint(1, len(self.playing_deck.player_deck))
        self.playing_deck.deal_player(num_deal)
        self.assertGreater(len(self.playing_deck.player_hand), 0)

        self.playing_deck.restart()
        self.assertEqual(52, len(self.playing_deck.player_deck))
        self.assertEqual(0, len(self.playing_deck.dealer_hand))
        self.assertEqual(0, len(self.playing_deck.player_hand))

    def test_get_dealer_tally(self):
        """
        Test dealer tally
        :return:
        """
        num_deal = random.randint(1, len(self.playing_deck.player_deck))
        self.playing_deck.deal_dealer(num_deal)
        self.assertGreater(self.playing_deck.get_dealer_tally(), 0)

    def test_get_player_tally(self):
        """
        Test player tally
        :return:
        """
        num_deal = random.randint(1, len(self.playing_deck.player_deck))
        self.playing_deck.deal_player(num_deal)
        self.assertGreater(self.playing_deck.get_player_tally(), 0)

    def tearDown(self):
        self.playing_deck.player_deck.empty()
        self.playing_deck.player_hand.clear()
        self.playing_deck.dealer_hand.clear()


if __name__ == '__main__':
    unittest.main()
