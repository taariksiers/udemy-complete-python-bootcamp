import pydealer

class PlayingDeck():
    """
    Operating with pydealer library
    """
    player_deck = None
    player_hand = list()
    dealer_hand = list()

    def __init__(self):
        self.player_deck = pydealer.Deck()
        self.player_deck.shuffle()


    def deal_player(self, num_cards = 1):
        """
        dealer the player cards and keep track
        :param num_cards: int
        :return: list
        """
        cards = self.player_deck.deal(num_cards)
        self.player_hand = [card for card in cards]
        return self.player_hand

    def deal_dealer(self, num_cards = 1):
        """
        dealer the dealer cards and keep track
        :param num_cards: int
        :return: list
        """
        cards = self.player_deck.deal(num_cards)
        self.dealer_hand = [card for card in cards]
        return self.dealer_hand


    def print_cards(self, cards):
        """
        Display card list
        :param cards: list
        :return: null
        """
        if len(cards) == 0:
            return ''

        return [print(elem) for elem in cards]


    def get_card_values(self, cards):
        """
        Calculate the score of all cards. Tally ho old chap
        :param cards: list
        :return:
        """
        tally = 0
        for card in cards:
            card_value = 10
            try:
                card_value = int(card.value)
            except ValueError:
                if card.name == 'Ace':
                    card_value = 11
            finally:
                tally += card_value

        return tally

    def __str__(self):
        """
        Print Player and Dealer cards
        :return: string
        """
        return f'Player cards: {[card.name for card in self.player_hand]}\nDealer Cards: {[card.name for card in self.dealer_hand]}'
        pass