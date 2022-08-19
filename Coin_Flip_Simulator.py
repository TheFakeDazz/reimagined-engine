from random import choice
from collections import Counter


def coin_flipper(num):
    choices = ['Heads', 'Tails']
    mylist = []
    for number in range(num):
        choose = choice(choices)
        print(f'Result: {choose}')
        mylist.append(choose)
    count = Counter(mylist)
    print(f'Number of Heads: {count["Heads"]}')
    print(f'Number of Tails: {count["Tails"]}')
    
    
