text = input("Input: ")
chars = ["a","A","e","E","i","I","o","O","u","U"]


for char in text:
    if char in chars:
        rchar = char
        removed_char = char.replace(rchar,"")
    else:
        print(char, end="")
print()
