
#Problem 5
#Version 1
"""
import random

def main():
    #TODO

def get_level():
    valid_level = [1,2,3]
    while True:
        try:
            level = int(input("Level: "))
            if level in valid_level:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        n = random.randint(0,9)
    elif level == 2:
        n = random.randint(10,99)
    else:
        n = random.randint(100,999)
    return n


if __name__ == "__main__":
    main()
"""

#Version 2:
#Now we have complete only the main function.
"""
def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for k in range(3):
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if x + y == user_answer:
                    score += 1
                    break
                else:
                    print("EEE")

            except ValueError:
                print("EEE")
        if x + y != user_answer:
            print(f"{x} + {y} = {x + y}")
    print(score)
"""
#This works but there is bug here.After the third wrong guess, the inner loop finishes.
# Now, look at the line of code that runs immediately after that inner loop: if x + y != user_answer:.
#On the third wrong guess, a ValueError might occur if the user types "cat".
# In that case, the user_answer variable would never have been assigned a value inside the loop and python will raise a NameError.
#The for...else Loop
#Python has a special, elegant feature designed for this exact situation: you can add an else block to a for loop.

#The else block runs only if the for loop completes all its iterations without being interrupted by a break statement.
"""
def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for k in range(3):
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if x + y == user_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {x + y}")
    print(score)
"""
#This is same thing we faced in class of week4.

import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for k in range(3):
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if x + y == user_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {x + y}")
    print(score)


def get_level():
    valid_level = [1,2,3]
    while True:
        try:
            level = int(input("Level: "))
            if level in valid_level:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        n = random.randint(0,9)
    elif level == 2:
        n = random.randint(10,99)
    else:
        n = random.randint(100,999)
    return n


if __name__ == "__main__":
    main()
