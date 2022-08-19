from random import choice
from collections import Counter


def coin_flipper(num):
    choices = ['Heads', 'Tails']
    mylist = []
    for w in range(num):
        x = choice(choices)
        print(f'Result: {x}')
        mylist.append(x)
    d = Counter(mylist)
    print(f'Number of Heads: {d["Heads"]}')
    print(f'Number of Tails: {d["Tails"]}')
    
    
