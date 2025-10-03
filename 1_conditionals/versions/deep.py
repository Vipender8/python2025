answer = input("What is the Answer to the Great Question of Life, the universe, and Everything? ")
answer = answer.lower().strip()

if answer == "42" or answer == "forty-two" or answer =="forty two":
    print("Yes")
else:
    print("No")

"""
#Problem 1
def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe and Everything?: ").lower().strip()  # Added strip method here.
    if is_correct(answer):
        print("Yes")
    else:
        print("No")

def is_correct(c):
    if c == "42" or c == "forty-two" or c == "forty two":
        return True


#Other way to define is_correct function in "Pythonic" version.
def is_correct(c):
    return c == "42" or c == "forty-two" or c == "forty two"

#Other way to define is_correct function using the match statment.
def is_correct(c):
    match c:
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False
main()

#Note: use else block while defining the function, Although it worked without using it.
"""