#Dictionary methods

WORDS = {"PAIR": 4, "HAIR":4, "CHAIR": 5, "GRAPHICS":7}

def main():

    print("Welcome to the Spelling Bee!")
    for word, points in WORDS.items():
        print(f"{word} gives you {points} points")

main()
