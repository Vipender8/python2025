items = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

total = 0
while True:
    try:
        item = input("Item: ").strip().title()
        if item not in items:
            pass
        elif item in items:
            total = total + float(items[item])
            print(f"Total: ${total:.2f}")
    except EOFError:
        break
print()


"""
Pythonic way:

# Here instead of DIC, you could name it MENU or something more descriptive.

DIC = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    cost = 0
    while True:
        try:
            item = input("Item: ").lower().strip().title()
            cost += DIC[item]
            print(f"Total: ${cost:0.2f}")
        except EOFError:
            break
        except KeyError:
            pass
main()
"""