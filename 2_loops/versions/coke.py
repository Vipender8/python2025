due = 50

while (due > 0):
    coin = int(input("Insert Coin: "))
    if not (coin == 25 or coin == 10 or coin == 5):
        print("Amount Due:", due)
    else:
        due = due - coin
        if due <= 0:
            break
        else:
            print("Amount Due:", due)

if due < 0:
    print("Change Owed:", abs(due))
else:
    print("Change Owed:", due)
