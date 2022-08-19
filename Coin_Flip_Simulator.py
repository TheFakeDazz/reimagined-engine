import random
import collections


def coin_flipper(num):
    choices = ['Heads', 'Tails']
    mylist = []
    for w in range(num):
        x = random.choice(choices)
        print(f'Result: {x}')
        mylist.append(x)
    d = collections.Counter(mylist)
    print(f'Number of Heads: {d["Heads"]}')
    print(f'Number of Tails: {d["Tails"]}')
    
    
