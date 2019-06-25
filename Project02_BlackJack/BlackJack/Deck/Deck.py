import pydealer

class DeckCalc():
    """
    Operating with pydealer library
    """

    def __init__(self, name, balance):
        pass


    def print_cards(self, cards):
        """Display the card list."""
        pass


    def get_card_value(self, card):
        """
        Calculate the current score based on the card
        :return int
        """
        cardValue = 10
        card = str(card).split()

        try:
            cardValue = int(card[0])
        except ValueError:
            if card[0].lower() == 'ace':
                cardValue = 11

        return cardValue


    def get_card_values(self, cards):
        """
        Calculate the score of all cards
        :param cards: tuple / list ? of cards
        :return: int
        """
        current_score = 0
        for card in cards:
            current_score += self.get_card_value(card)

        return current_score

    def __str__(self):
        '''Print out something not sure what yet'''
        # return f'{self.owner.lower().capitalize()} Account Balance: {self.balance}'
        pass