import random


class Card:

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


full_deck = [Card('Ace', 'Clubs'), Card('Two', 'Clubs'), Card('Three', 'Clubs'), Card('Four', 'Clubs'),
             Card('Five', 'Clubs'), Card('Six', 'Clubs'), Card('Seven', 'Clubs'), Card('Eight', 'Clubs'),
             Card('Nine', 'Clubs'), Card('Ten', 'Clubs'), Card('Jack', 'Clubs'), Card('Queen', 'Clubs'),
             Card('King', 'Clubs'), Card('Ace', 'Diamonds'), Card('Two', 'Diamonds'), Card('Three', 'Diamonds'),
             Card('Four', 'Diamonds'), Card('Five', 'Diamonds'), Card('Six', 'Diamonds'), Card('Seven', 'Diamonds'),
             Card('Eight', 'Diamonds'), Card('Nine', 'Diamonds'), Card('Ten', 'Diamonds'), Card('Jack', 'Diamonds'),
             Card('Queen', 'Diamonds'), Card('King', 'Diamonds'), Card('Ace', 'Hearts'), Card('Two', 'Hearts'),
             Card('Three', 'Hearts'), Card('Four', 'Hearts'), Card('Five', 'Hearts'), Card('Six', 'Hearts'),
             Card('Seven', 'Hearts'), Card('Eight', 'Hearts'), Card('Nine', 'Hearts'), Card('Ten', 'Hearts'),
             Card('Jack', 'Hearts'), Card('Queen', 'Hearts'), Card('King', 'Hearts'), Card('Ace', 'Spades'),
             Card('Two', 'Spades'), Card('Three', 'Spades'), Card('Four', 'Spades'), Card('Five', 'Spades'),
             Card('Six', 'Spades'), Card('Seven', 'Spades'), Card('Eight', 'Spades'), Card('Nine', 'Spades'),
             Card('Ten', 'Spades'), Card('Jack', 'Spades'), Card('Queen', 'Spades'), Card('King', 'Spades')]
player_1 = []
player_2 = []


def player_deck():
    for number in range(26):
        one = full_deck.pop(0)
        player_2.append(one)
    for number in range(26):
        two = full_deck.pop(0)
        player_1.append(two)


rank_defined = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
                'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 20}


def tie():
    print("It's time for War!!\n \nEach player draws 3 cards and compares the top card!\n")
    # Player 1 cards
    flamethrower = player_1.pop(0)
    hydro_pump = player_1.pop(0)
    recover = player_1.pop(0)
    # Player 2 cards
    shadow_ball = player_2.pop(0)
    psychic = player_2.pop(0)
    energy_ball = player_2.pop(0)
    print(f'Player 1 drew: {str(flamethrower)}\nPlayer 2 drew: {str(shadow_ball)}\n ')
    if rank_defined[flamethrower.rank] > rank_defined[shadow_ball.rank]:
        print('Player 1 wins the War and takes all 6 cards!\n ')
        player_1.append(flamethrower)
        player_1.append(hydro_pump)
        player_1.append(recover)
        player_1.append(shadow_ball)
        player_1.append(psychic)
        player_1.append(energy_ball)
    elif rank_defined[flamethrower.rank] < rank_defined[shadow_ball.rank]:
        print('Player 2 wins the War and takes all 6 cards!\n ')
        player_2.append(flamethrower)
        player_2.append(hydro_pump)
        player_2.append(recover)
        player_2.append(shadow_ball)
        player_2.append(psychic)
        player_2.append(energy_ball)


def war():
    i=0
    random.shuffle(full_deck)
    player_deck()
    while True:
        start = input('Start the game? (Y/N): ').lower()
        if start == 'y':
            game_on = True
        elif start not in ['y', 'n']:
            print('Sorry, I do not understand')
            continue
        else:
            break

        while game_on == True:
            i+=1
            print(f'Round {i}')
            if len(player_1) == 0:
                print('Player 1 runs out of cards,\nPlayer 2 Wins the Game!')
                return
            if len(player_2) == 0:
                print('Player 2 runs out of cards,\nPlayer 1 Wins the Game!')
                return
            shell = player_1.pop(0)
            earth = player_2.pop(0)
            
            print(f'Player 1 drew: {str(shell)}\nPlayer 2 drew: {str(earth)}')
            if rank_defined[shell.rank] > rank_defined[earth.rank]:
                print('Player 1 asserts his dominance by taking both cards!\n')
                player_1.append(earth)
                player_1.append(shell)
                continue
            elif rank_defined[shell.rank] < rank_defined[earth.rank]:
                print('Player 2 asserts his dominance by taking both cards!\n')
                player_2.append(earth)
                player_2.append(shell)
                continue
            if rank_defined[shell.rank] == rank_defined[earth.rank]:
                tie()
