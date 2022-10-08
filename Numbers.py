# ---------------------------------------------------Find Pi Digits----------------------------------------------------------------------------------------------------
def pi():
    while True:
        
        try:
            w=int(input('Enter how many digits of pi you want after the decimal (Up to 25): '))
            if w>25:
                print('Only up to 25!')
                continue
        except ValueError:
            print('Only numbers are allowed!')
        else:
            e='1415926535897932384626433'
            t=e[0:w]
            return float(f'3.{t}')
# -------------------------------------Find e Digits (Euler's Number)--------------------------------------------------------------------------------------------------
def e():
    while True:
        
        try:
            w=int(input('Enter how many digits of e you want after the decimal (Up to 25): '))
            if w>25:
                print('Only up to 25!')
                continue
        except ValueError:
            print('Only numbers are allowed!')
        else:
            e='7182818284590452353602874'
            t=e[0:w]
            return float(f'2.{t}')
# ----------------------------------Random Prime Number Generator (1-100)----------------------------------------------------------------------------------------------
import random
def prime_numbers():
    mylist=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    gameon=False
    while True:
    
            e=input('Do you want to see a prime number from 1-100? (y/n): ')
            if e=='n'.lower():
                break
            elif e=='y':
                gameon=True
            if gameon==True:
                return random.choice(mylist)
# ----------------------------------Next Prime Number Generator (1-100)------------------------------------------------------------------------------------------------
def prime_generator():
    mylist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    while True:
        print('\n')
        if len(mylist) == 0:
            print('Out of numbers!')
            break
        ask = input('Would you like to see the next prime number? (Type "yes" or "no"): ')
        if ask == 'yes':
            print(mylist.pop(0))
        elif ask == 'no':
            break
#-------------------------------------------Collatz Conjecture---------------------------------------------------------------------------------------------------------
def steps(number):
    num = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    print(f'{num}. {number}')
    if number == 1:
        return 0
    while number != 1:
        if number%2 == 0:
            num+=1
            number = number/2
            print(f'{num}. {number}')
            if number == 1:
                return num
        if number%2 != 0:
            num+=1
            number = 3 * number + 1
            print(f'{num}. {number}')
            if number == 1:
                return num
