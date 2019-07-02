"""
Deck class with convenience methods on top of pydealer
"""
import pydealer

class PlayingDeck(object):
    """
    Operating with pydealer library
    """
    player_deck = None
    debug = False
    player_hand = list()
    dealer_hand = list()

    def __init__(self, **kwargs):
        """
        Addition of kwargs
        :param kwargs:
        """
        self.player_deck = pydealer.Deck()
        self.player_deck.shuffle()
        for key, value in kwargs.items():
            self.key = value

    def deal_player(self, num_cards = 1):
        """
        dealer the player cards and keep track
        :param num_cards: int
        :return: list
        """
        self.debug and print(f'Player deal {num_cards}')
        cards = self.player_deck.deal(num_cards)
        x = [self.player_hand.append(card) for card in cards]
        return self.player_hand

    def deal_dealer(self, num_cards = 1):
        """
        dealer the dealer cards and keep track
        :param num_cards: int
        :return: list
        """
        self.debug and print(f'Dealer deal {num_cards}')
        cards = self.player_deck.deal(num_cards)
        y = [self.dealer_hand.append(card) for card in cards]
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
        aces = 0
        tally = 0
        for card in cards:
            card_value = 10
            try:
                card_value = int(card.value)
            except ValueError:
                if card.name.split()[0].lower() == 'ace':
                    aces += 1
                    card_value = 11

            tally += card_value

        self.debug and print(f'Tally {tally}')

        if tally > 21 and aces > 0:
            self.debug and print(f'Reducing tally')
            tally = tally - (10*aces)

        return tally

    def restart(self):
        """
        Restart the deck
        :return:
        """
        self.player_deck.empty()
        self.player_hand.clear()
        self.dealer_hand.clear()
        self.player_deck = pydealer.Deck()
        self.player_deck.shuffle()

    def get_player_tally(self):
        """
        Convenience method to return the player tally
        :return: int
        """
        self.debug and print(f'Player Tally {self.get_card_values(self.player_hand)}')
        return self.get_card_values(self.player_hand)

    def get_dealer_tally(self):
        """
        Convenience method to return the player tally
        :return: int
        """
        self.debug and print(f'Dealer Tally {self.get_card_values(self.dealer_hand)}')
        return self.get_card_values(self.dealer_hand)

    def print_hands(self):
        """
        Print the hands
        :return: string
        """
        print(f'\nYour deal:\n---------------\n')

        self.print_cards(self.player_hand)

        print(f'\nDealer hand:\n---------------\n')
        self.print_cards(self.dealer_hand)
        print('\n')

    def __str__(self):
        """
        Print Player and Dealer cards
        :return: string
        """
        return f'Player Cards: {[card.name for card in self.player_hand]}\nDealer Cards: {[card.name for card in self.dealer_hand]}'
        pass