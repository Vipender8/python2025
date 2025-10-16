#Problme 4
#Version 1
"""
from random import randint

def main():
    level = get_int("Level: ")
    guess = randint(1,level)

    while True:
        user_guess = get_int("Guess: ")
        if user_guess > guess:
            print("Too large!")
        elif user_guess < guess:
            print("Too small!")
        else:
            print("Just right!")
            break


def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n <= 0:
                raise ValueError
        except ValueError:
            pass
        else:
            break
main()
"""
#The above code works fine but we can make it pythonic.
#Version 2 , just chaneged the get_int function.def get_int(prompt):
"""
def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass
"""


from random import randint

def main():
    level = get_int("Level: ")
    guess = randint(1,level)

    while True:
        user_guess = get_int("Guess: ")
        if user_guess > guess:
            print("Too large!")
        elif user_guess < guess:
            print("Too small!")
        else:
            print("Just right!")
            break


def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass
main()
