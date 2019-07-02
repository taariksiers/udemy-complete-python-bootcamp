from Player import player

purse = 100
min_decks = 1
max_decks = 6
player_name = ''

print(f'{"=" * 60}\n\tWelcome to BlackJack. Starting purse ${purse}.\n{"=" * 60}')

while True:
    name_input = input('Please enter your name... ').strip()

    if len(name_input) > 0:
        player_name = name_input.capitalize()
        playa = player.Player(player_name, purse, False)
        break

while True:
    num_decks = input(f'Please choose a valid number of decks between {min_decks} and {max_decks}... ')

    try:
        decks = int(num_decks)
        if max_decks >= decks > min_decks:
            break
    except ValueError:
        pass


print(f'Welcome {player_name}! We are playing with {decks} decks.')


