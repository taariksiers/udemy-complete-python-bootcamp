# from Bank import Account # twerks in same dir
# player1 = Account('Player1', 500)
from Bank import Bank # twerks from sub dir
# from Deck import Deck # twerks from sub dir
import pydealer
import os

def getCardValue(dealer_card):
    '''Simply determine the card value'''
    cardValue = 10
    card = str(dealer_card).split()

    try:
        cardValue = int(card[0])
    except ValueError:
        if card[0].lower() == 'ace':
            cardValue = 11

    return cardValue

print(
'''
------------------------------
    Let\'s play Blackjack!
    Dealer stands at 18.
------------------------------
''')

bank_amount = 0
bet = 0
player1_account = Bank.Account('Player 1', 500)

# help(player1_account)
#exit(0)

while bank_amount == 0:
    try:
        bank_amount = int(input('Enter your bank amount: '))
    except:
        print('Please enter a valid amount greater than 0')
    else:
        player1_account = Bank.Account('Player 1', bank_amount)
        print(player1_account)

print(
'''
------------------------------
    Game on!
------------------------------
''')

# part of routine class to get access to bank
game_on = True
while game_on == True:
    try:
        bank_amount = player1_account.balance
        bet = input('Enter your bet (or type [end] to complete the game):  ')
        if bet.lower() == 'end':
            game_on = False
            break

        bet = int(bet)
    except:
        print(f'Please enter a valid amount greater than 0 and less than your bank amount R{bank_amount}')
    else:
        print()
        if bet > bank_amount or bet == 0:
            print(f'The bet must be greater than 0 and cannot be greater than what you have in the bank {bank_amount}')
        else :
            os.system('clear')
            bank_amount = player1_account.withdraw(bet)
            print(f'Bet placed {bet}. Bank Balance: {bank_amount}')

            player1_deck = pydealer.Deck()
            player1_deck.shuffle()

            player_tally = 0
            dealer_tally = 0

            allowed_moves = ['H', 'S']

            print(f'\nYour deal:\n---------------\n')
            player_cards = player1_deck.deal(2)
            dealer_cards = player1_deck.deal(2)
            for card in player_cards:
                player_tally += getCardValue(card)
                print(f'{card}')

            print(f'\nDealer Hand:\n-------------\n')
            for card in dealer_cards:
                dealer_tally += getCardValue(card)
                print(f'{card}')

            print(f'\nDEBUG 1 player_tally {player_tally} dealer_tally {dealer_tally}')

            while True:
                move = input('\n--------------------\nCurrent [H]it / [S]tand:\n').upper()

                if move not in allowed_moves:
                    print(f'This [{move}] is not a valid option. Please retry.')
                    continue

                if move == 'H':
                    card = player1_deck.deal(1)
                    # REPRINT FULL CARD LIST
                    print(f'New card {card}')
                    player_tally += getCardValue(card)

                    if player_tally > 21:
                        # BUST you lose
                        print(f'BUST! {player_tally} You lose. Current Balance: {player1_account.balance}')
                        break

                    if dealer_tally < 18:
                        print(f'Dealer card {card}')
                        dealer_card = player1_deck.deal(1)
                        dealer_tally += getCardValue(dealer_card)

                    if dealer_tally > 21:
                        bank_amount = player1_account.deposit(bet * 2)
                        print(f'Dealer BUST! You Win! Current Balance: {player1_account.balance}')
                        break

                    print(f'\nDEBUG 2 current_tally {player_tally} dealer_tally {dealer_tally}')
                    continue

                if move == 'S':
                    # calc num vs 21
                    # detect first char is int, if not, map Jack = 10, Queen 10, King = 10, Ace = 11 / 1


                    # STILL HAVE TO DEALER DEAL IF < 18

                    if dealer_tally > player_tally:
                        print('Dealer wins! You lose.')
                    elif dealer_tally == player_tally:
                        bank_amount = player1_account.deposit(bet)
                        print(f'DRAW. Restoring cash {player1_account.balance}')
                    else:
                        bank_amount = player1_account.deposit(bet * 2)
                        print(f'You Win! Current Balance: {player1_account.balance}')

                # print(f'You have selected {move}. You lost this round. Current Balance {player1_account.balance}.')
                break

        if bank_amount == 0:
            print(f'Out of cash bro')
            game_on = False

    finally:
        print('-------------------------')

print(f'Game over. Final balance: {player1_account.balance}')