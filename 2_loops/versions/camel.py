
camelcase = input("camelCase: ")

for case in camelcase:
    if case.isupper():
        case = case.lower()
        new_case = case
        final_case = case.replace(new_case,"_")
        print(final_case + case, end="")
    else:
        print(case, end="")
print()

#Problem 1
"""
def main():
    camelcase = input("camelCase: ")
    print(snake_case(camelcase))

def snake_case(text):
    snakecase = []
    for letter in text:
        if letter.isupper():
           updated_letter = "_" + letter.lower()
           snakecase.append(updated_letter)
        else:
            snakecase.append(letter)
    return "".join(snakecase)

main()
"""