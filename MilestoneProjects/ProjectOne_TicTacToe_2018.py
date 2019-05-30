# inputs & capture
# number position mapping
# print new spacer
# print board
# print detect 3 in a row as winner
# from iPython.display import clear_output()
# record turn based
print('Welcome to Tic Tac Toe.')

while True:
    player1 = input('Please pick a marker X or O: ').upper()
    if player1 in ('X','O'):
        player2 = 'O' if player1 == 'X' else 'X'
        break

# a if condition else b
print(f'Player one has chosen {player1}. Player two is therefore {player2}.')

def displayBoard(positions):
    print('\n' * 100)
    splitter = '\t---|---|---'

    print('')
    print("\t {} | {} | {} " . format(positions[1],positions[2],positions[3]))
    print(splitter)
    print("\t {} | {} | {} " . format(positions[4],positions[5],positions[6]))
    print(splitter)
    print("\t {} | {} | {} " . format(positions[7],positions[8],positions[9]))
    print('')
    pass

def checkWinner(positions, player):
    if (len(positions) < 3):
        return False

    combos = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
    plays = [key for (key,value) in positions.items() if value == player]

    for combo in combos:
        S1 = set(plays)
        S2 = set(combo)
        inter = S1.intersection(S2)
        if (len(inter) >= 3):
            return True

    return False

defaultBoard = dict(enumerate(list(range(1,10)), start=1))
displayBoard(defaultBoard)

expectedMove = player1
possibleMoves = list(range(1,10))
moves = []
spacer = "   "
spacerList = list(spacer * 3) 
positions = dict(enumerate(spacerList, start=1))

while True:
    currentPlayer = '1' if expectedMove == player1 else '2'
    move = input(f'Player {currentPlayer}, please Choose a position 1 through 9: ')
    haveAWinner = False

    try:
        move = int(move)
    except ValueError:
        continue

    if move in moves:
        print('Move already assigned. Choose another')
        continue

    if move in possibleMoves:
        moves.append(move)
        positions[move] = expectedMove
        displayBoard(positions)
        haveAWinner = checkWinner(positions, expectedMove)
        expectedMove = 'O' if expectedMove == 'X' else 'X'

    if haveAWinner:
        print(f'The winner is Player {currentPlayer}!.')
        break

    if (len(moves) == 9):
        print('Stalemate. Try again.')
        break