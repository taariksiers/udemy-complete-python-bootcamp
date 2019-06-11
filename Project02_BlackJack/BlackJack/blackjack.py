# from Bank import Account # twerks in same dir
# player1 = Account('Player1', 500)
from Bank import Bank # twerks from sub dir

print(
'''
------------------------------
    Let\'s play Blackjack!
    Dealer stands at 18.
------------------------------
''')

bank_amount = 0
bet = 0

# routine class?
while bank_amount == 0:
    try:
        bank_amount = int(input('Enter your bank amount: '))
    except:
        print('Please enter a valid amount greater than 0')
    else:
        player1_account = Bank.Account('Player 1', bank_amount)
        print(player1_account)

# game on should be in a loop

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
        bet = input('Enter your bet (or type [end] to complete the game):  ')
        if bet.lower() == 'end':
            game_on = False
            break

        bet = int(bet)
    except:
        print(f'Please enter a valid amount greater than 0 and less than your bank amount R{bank_amount}')
    else:
        # loop here?
        if bet > bank_amount or bet == 0:
            print(f'The bet must be greater than 0 and cannot be greater than what you have in the bank {bank_amount}')
        else :
            player1_account.withdraw(bet)
            bank_amount = player1_account.balance
            print(f'Bet placed {bet}. Bank Balance: {bank_amount}')

            allowed_moves = ['H', 'S']
            while True:
                move = input('[H]it / [S]tand: ')

                if move not in allowed_moves:
                    print(f'This [{move}] is not a valid option. Please retry.')
                    continue

                # win or miss - win ++ bank_account
                print(f'You have selected {move}. You lost this round. Current Balance {player1_account.balance}.')
                break

        if bank_amount == 0:
            print(f'Out of cash bro')
            game_on = False

    finally:
        print('-------------------------')

print(f'Game over.')