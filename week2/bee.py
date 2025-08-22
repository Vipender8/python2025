#Dictionary methods

WORDS = {"PAIR": 4, "HAIR":4, "CHAIR": 5, "GRAPHICS":7}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        if guess == "GRAPHICS":
            WORDS.clear()
            print(f"You won the game!")


        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")
    
    print("That's the game!")


main()