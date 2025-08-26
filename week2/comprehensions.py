from helpers import get_words, save_counts

def main():

    words = get_words("address.txt")

    lower_words = [word.lower() for word in words if len(word) > 4]

    counts = {word:lower_words.count(word) for word in lower_words}

    save_counts(counts)

main()