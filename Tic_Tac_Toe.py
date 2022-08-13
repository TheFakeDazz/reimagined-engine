# Tic Tac Toe
board = ['U', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# This will be the tic-tac-toe board
def tic_board():
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# This checks if a player has won
def pattern(num, num2, num3, player, mark):
    if board[num] == mark and board[num2] == mark and board[num3] == mark:
        print(f'{player} Wins!')
        quit()

# This checks if the game is tied
def full():
    if ' ' not in board:
        print('Board is full, game ends')
        quit()

# This is the main tic-tac-toe function
def tic():
    player_marker = 0
    player2_marker = 0
    main = 0
    second = 0
    game_on = 0
    while True:
        # 'welcome' asks the player if they want to be Player 1 or 2
        welcome = input('Welcome to the game. Would you like to be player 1 or player 2? (Type 1 or 2 or type '
                        'quit to '
                        'exit out): ').lower()
        match welcome:
            case '1':
                main = 'player 1'
                second = 'player 2'
            case '2':
                main = 'player 2'
                second = 'player 1'
            case 'quit':
                break
            case _:
                print('Please type 1 or 2')
                continue
        # This while loop asks if the player wants to be X or O and assigns it to the appropriate player
        while player_marker not in ['X', 'O']:
            marker = input(f'Hello {main}, would you like to be X or O?: ').upper()
            match marker:
                case 'X':
                    player_marker = 'X'
                    player2_marker = 'O'
                    break
                case 'O':
                    player_marker = 'O'
                    player2_marker = 'X'
                    break
        # This while loop asks if the player would like to start the game
        while True:
            start = input('Would you like to start the game? (Y/N): ').lower()
            match start:
                case 'y':
                    game_on = True
                    break
                case 'n':
                    return
        while game_on == True:
            # This is where the magic happens and the game between the players is looped until one wins or tied
            pattern(7, 8, 9, main, player_marker)
            pattern(4, 5, 6, main, player_marker)
            pattern(1, 2, 3, main, player_marker)
            pattern(7, 5, 3, main, player_marker)
            pattern(7, 4, 1, main, player_marker)
            pattern(8, 5, 2, main, player_marker)
            pattern(9, 6, 3, main, player_marker)
            pattern(9, 5, 1, main, player_marker)
            pattern(7, 8, 9, second, player2_marker)
            pattern(4, 5, 6, second, player2_marker)
            pattern(1, 2, 3, second, player2_marker)
            pattern(7, 5, 3, second, player2_marker)
            pattern(7, 4, 1, second, player2_marker)
            pattern(8, 5, 2, second, player2_marker)
            pattern(9, 6, 3, second, player2_marker)
            pattern(9, 5, 1, second, player2_marker)
            full()
            tic_board()
            try:
                search = int(input(f'{main}, where would you like to place your {player_marker}?: '))
                if board[search] != ' ':
                    print('Spot taken!')
                    continue
            except ValueError:
                print('Please enter a value')

            board[search] = player_marker
            tic_board()
            full()
            pattern(7, 8, 9, main, player_marker)
            pattern(4, 5, 6, main, player_marker)
            pattern(1, 2, 3, main, player_marker)
            pattern(7, 5, 3, main, player_marker)
            pattern(7, 4, 1, main, player_marker)
            pattern(8, 5, 2, main, player_marker)
            pattern(9, 6, 3, main, player_marker)
            pattern(9, 5, 1, main, player_marker)
            pattern(7, 8, 9, second, player2_marker)
            pattern(4, 5, 6, second, player2_marker)
            pattern(1, 2, 3, second, player2_marker)
            pattern(7, 5, 3, second, player2_marker)
            pattern(7, 4, 1, second, player2_marker)
            pattern(8, 5, 2, second, player2_marker)
            pattern(9, 6, 3, second, player2_marker)
            pattern(9, 5, 1, second, player2_marker)
            full()
            try:
                search_2 = int(input(f'{second}, where would you like to place your {player2_marker}?: '))

            except ValueError:
                print('Please enter a value')
            if board[search_2] != ' ':
                print('Spot taken!')
                continue
            board[search_2] = player2_marker
            tic_board()


tic()
