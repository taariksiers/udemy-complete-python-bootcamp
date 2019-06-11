# tic tac toe
# display num pad
# ask x or o
# ask position
# confirm winner or bust

# Accept input for 1) symbol 2) move --- while loop if game is not concluded
# print board after every move
# confirm winner loser

# pip3 install IPython
import os

# var declaration section
player1 = ''
moves = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
remaining_moves = list(moves.keys())
player_move = None
player_turn = 1
game_concluded = False

# method section
def display_board(moves):
    os.system('clear')
    print(f'''
    Board\n--------------------\n
    {moves[7]} | {moves[8]} | {moves[9]}
    ----------
    {moves[4]} | {moves[5]} | {moves[6]}
    ----------
    {moves[1]} | {moves[2]} | {moves[3]}
    \n--------------------
    ''')


def check_winner(moves):
    x_combos = [key for key, mover in moves.items() if mover == 'X']
    o_combos = [key for key, mover in moves.items() if mover == 'O']
    winning_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [3,5,7], [1,5,9]]
    winner = '-'

    for winning_combo in winning_combinations:
        x_matches = [num for num in x_combos if num in winning_combo]
        if len(x_matches) >= 3:
            winner = 'X'
            break
        o_matches = [num for num in o_combos if num in winning_combo]
        if len(o_matches) >= 3:
            winner = 'O'
            break

        # print(f'Winning combo {winning_combo} x_matches {x_matches} o_matches {o_matches}')

    return winner

    pass
    # course solution


# Begin
print('Welcome to Tic Tac Toe.')
display_board({1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'})
while player1 not in ['X', 'O']:
    player1 = input('Player 1: choose [X] or [O] ... ').upper()

player2 = 'X' if player1 == 'O' else 'O'
print(f'Player 1: {player1} | Player 2: {player2}')
print('--------------------')


while game_concluded is False:

    while player_move not in remaining_moves:
        try:
            player_move = int(input(f'Player {player_turn}, please enter your move position between 1 and 9:   ... '))
        except ValueError:
            print(f'Please enter a valid number in the allowed range {remaining_moves}')
        except:
            print(f'Please enter a position in the allowed range {remaining_moves}')
        # finally:
        #     os.system('clear')

    moves[player_move] = player1 if player_turn == 1 else player2

    remaining_moves = [key for key,mover in moves.items() if mover not in ['X', 'O']]

    display_board(moves)

    # print(f'player move {player_move}')
    # print(f'Remaining {remaining_moves}')
    # print(f'Player_turn {player_turn}')

    winner = check_winner(moves)
    if (winner in ['X', 'O']):
        print(f'Player {player_turn} is the Winner!')
        game_concluded = True
    else:
        player_turn = 1 if player_turn == 2 else 2
        player_move = player1 if player_turn == 2 else player2

    if not remaining_moves:
        print('Stalemate: Game over! Try Again?')
        game_concluded = True

