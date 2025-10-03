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

#Problem 2
"""
def main():
    amount = 50
    while (amount > 0):
        print(f"Amount Due: {amount}")
        coin_inserted = int(input("Insert Coin: "))
        if check(coin_inserted):
            amount = amount - coin_inserted

    print(f"Change owed: {abs(amount)}")

def check(user_input):
    accepted_amount = [5,10,25]
    return user_input in accepted_amount
main()

#Another solution:
def main():
    amount_due = 50
    # Loop as long as there is an amount due
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        # Check if the coin is one of the accepted values
        if coin in [25, 10, 5]:
            # Subtract the coin from the amount due
            amount_due -= coin

    # After the loop, calculate and print the change owed
    change_owed = -amount_due
    print(f"Change Owed: {change_owed}")

main()
"""