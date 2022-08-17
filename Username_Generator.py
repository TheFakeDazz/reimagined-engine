# Random Username Generator
import random


def username_generator():
    while True:
        question = input('Would you like to generate a username? (y/n)').lower().strip()
        match question:
            case 'y':
                con = True
            case 'n':
                break
            case _:
                print('Please enter a valid option')
                continue

        while con == True:
            adjectives = ['Excellent', 'Amazing', 'Fantastic', 'Gloomy', 'Contagious', 'Ambient', 'Agitated', 'Raging',
                          'Critical', 'Determined', 'Healthy', 'Inspired', 'Creative', 'Healthy', 'Livid', 'Bitter',
                          'Strengthened', 'Refreshed', 'Vibrant', 'Motivated', 'Frozen', 'Stunned', 'Dynamic']
            nouns = ['Bread', 'Toast', 'Banana', 'Elephant', 'Apple', 'Ad', 'Wasp', 'Meat', 'Guy', 'Girl', 'Berry',
                     'Clock', 'File', 'Test', 'Pen', 'Sun', 'Moon', 'Cow', 'Chicken', 'List', 'Button', 'Bar', 'Car',
                     'Phone', 'Brand', 'Person', 'Space', 'Ball', 'Air', 'Computer', 'Color']
            numbers = list(range(100))
            return f'{random.choice(adjectives)}{random.choice(nouns)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}'
