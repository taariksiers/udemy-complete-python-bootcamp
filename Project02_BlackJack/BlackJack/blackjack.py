"""
The main blackjack execution
"""
import os
import sys
from Bank.Bank import Account
from Deck.Deck import PlayingDeck

try:
    debug = True if sys.argv[1] == '1' else False
except IndexError:
    debug = False

try:
    bank_amount = int(sys.argv[2]) if sys.argv[2] else None
except IndexError:
    bank_amount = None

bet = None
DEALER_STAND = 18
allowed_moves = ['H', 'S']

print('------------------------------\n')
print('Let\'s play Blackjack!\n')
print(f'Dealer stands at {DEALER_STAND}.\n')
print('------------------------------\n')

while bank_amount is None:
    try:
        bank_amount = int(input('Enter your bank amount: '))
    except ValueError:
        print('Please enter a valid amount greater than 0')

player1_account = Account(owner='Player 1', balance=bank_amount)
print(player1_account)

print(
    '''
------------------------------
    Game on!
------------------------------
''')

# part of routine class to get access to bank
game_on = True
while game_on:
    try:
        bank_amount = player1_account.balance
        bet = input('Enter your bet (or type [end] to complete the game):  ')
        if bet.lower() == 'end':
            game_on = False
            break
        bet = int(bet)
    except ValueError:
        print(f'Please enter a valid amount greater than 0 and less than your bank amount R{bank_amount}')
    else:
        print()
        if bet > bank_amount or bet == 0:
            print(f'The bet must be greater than 0 and cannot be greater than what you have in the bank {bank_amount}')
        else:
            not debug and os.system('clear')
            bank_amount = player1_account.withdraw(bet)
            print(f'Bet placed {bet}. Bank Balance: {bank_amount}')

            playing_deck = PlayingDeck(debug=debug)
            playing_deck.restart()
            playing_deck.deal_player(2)
            playing_deck.deal_dealer(2)
            playing_deck.print_hands()

            while True:
                move = input('\n--------------------\nCurrent [H]it / [S]tand:\n').upper()

                if move not in allowed_moves:
                    print(f'This [{move}] is not a valid option. Please retry.')
                    continue

                if move == 'H':
                    playing_deck.deal_player()
                    os.system('clear')
                    print(f'\nYour deal:\n---------------\n')
                    playing_deck.print_cards(playing_deck.player_hand)

                    if playing_deck.get_player_tally() > 21:
                        print(f'\nDealer hand:\n---------------\n')
                        playing_deck.print_cards(playing_deck.dealer_hand)
                        print('\n')

                        print(f'BUST! {playing_deck.get_player_tally()} You lose. Current Balance: {player1_account.balance}')
                        break

                    if playing_deck.get_dealer_tally() < DEALER_STAND:
                        dealer_hand = playing_deck.deal_dealer()

                    print(f'\nDealer hand:\n---------------\n')
                    playing_deck.print_cards(playing_deck.dealer_hand)
                    print('\n')

                    if playing_deck.get_dealer_tally() > 21:
                        bank_amount = player1_account.deposit(bet * 2)
                        print(f'Dealer BUST! You Win! Current Balance: {player1_account.balance}')
                        break

                    continue

                if move == 'S':
                    while playing_deck.get_dealer_tally() < DEALER_STAND:
                        playing_deck.deal_dealer()

                    not debug and os.system('clear')
                    playing_deck.print_hands()

                    print('\n------------------\n\t')
                    if playing_deck.get_dealer_tally() > 21:
                        print(f'Dealer BUST. You win!')
                        bank_amount = player1_account.deposit(bet * 2)
                    elif playing_deck.get_player_tally() > 21:
                        print(f'BUST. Dealer wins!')
                    elif playing_deck.get_dealer_tally() == playing_deck.get_player_tally():
                        bank_amount = player1_account.deposit(bet)
                        print(f'DRAW. Restoring cash {player1_account.balance}')
                    elif playing_deck.get_dealer_tally() > playing_deck.get_player_tally():
                        print(f'Dealer wins!')
                    else:
                        print(f'You Win!')
                        bank_amount = player1_account.deposit(bet * 2)

                    print(f'Current Balance: {player1_account.balance}\n')

                break

        if bank_amount is 0:
            print(f'Out of cash. Game over.')
            game_on = False

    finally:
        print('-------------------------')

print(f'Game over. Final balance: {player1_account.balance}')
