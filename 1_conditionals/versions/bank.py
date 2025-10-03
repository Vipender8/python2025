greeting = input("Greeting: ").lower().strip()


if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")


"""
#Problem 2
def main():
    greeting = input("Greeting: ").lower().strip()
    check(greeting)

def check(c):
    if c.startswith("hello"):
        print("$0")
    elif c.startswith("h"):
        print("$20")
    else:
        print("$100")
main()

Note: Here's a tip that will make your code much more flexible. Right now, your check function prints the result.
It's generally better practice to have your helper functions return a value and let main be in charge of printing.

#A good practise:
def main():
    greeting = input("Greeting: ").lower().strip()
    print(check(greeting))

def check(c):
    if c.startswith("hello"):
        return "$0"
    elif c.startswith("h"):
        return "$20"
    else:
        return "$100"

main()
"""