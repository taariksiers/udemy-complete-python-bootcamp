import io, pydealer, random, sys, unittest

sys.path.append('../')
from Deck import Deck


class TestDeck(unittest.TestCase):
    """
    Unit tests for Deck functionality
    """
    playing_deck = None

    def setUp(self):
        self.playing_deck = Deck.PlayingDeck()

    def test_init(self):
        """
        Test the initialisation
        :return:
        """

        self.assertEqual(52, len(self.playing_deck.player_deck))
        self.assertEqual(str(self.playing_deck), 'Player cards: []\nDealer Cards: []')

    def test_str(self):
        """
        test string - a bit of a nothing test
        :return:
        """
        player_cards = self.playing_deck.deal_player(3)
        dealer_cards = self.playing_deck.deal_dealer(3)
        self.assertEqual(str(self.playing_deck), f'Player cards: {[card.name for card in player_cards]}\nDealer Cards: {[card.name for card in dealer_cards]}')

    def test_deal_player(self):
        """
        Test the player deal
        :return:
        """
        num_deal = random.randint(1,len(self.playing_deck.player_deck))
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
        num_deal = random.randint(1, len(self.playing_deck.player_deck))
        deal = self.playing_deck.deal_dealer(num_deal)
        card_values = self.playing_deck.get_card_values(deal)
        self.assertTrue('int', type(card_values))


if __name__ == '__main__':
    unittest.main()

