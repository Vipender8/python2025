text = input("Input: ")
chars = ["a","A","e","E","i","I","o","O","u","U"]


for char in text:
    if char in chars:
        rchar = char
        removed_char = char.replace(rchar,"")
    else:
        print(char, end="")
print()

#Problem 3
"""
def main():
    user_input = input("Input: ")
    print(f"Output: {output(user_input)}")

def output(text):
    final_text = []
    removed_letter = ["A","E","I","O","U","a","e","i","o","u"]
    for letter in text:
        if letter not in removed_letter:
            final_text.append(letter)

    return "".join(final_text)

main()

This code is okay, but we can make it more pythonic and defining function in good way.
You used output as function name, don't you think remove_vowels(text), this is good name as it clearly states what it is doing.
def remove_vowels(text):
    final_text = []
    vowels = "aeiou" # Just the lowercase vowels
    for letter in text:
        # Check the lowercase version of the letter
        if letter.lower() not in vowels:
            final_text.append(letter)
    return "".join(final_text)

Another way to write the loop in above function is as follows:
def remove_vowels(text):
    # This one line does the same thing as your entire for loop
    non_vowels = [letter for letter in text if letter.lower() not in "aeiou"]
    return "".join(non_vowels)
"""
