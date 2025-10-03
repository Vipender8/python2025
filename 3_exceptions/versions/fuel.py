from fractions import Fraction

while True:
    try:
        fraction_input = input("Fraction: ")
        numerator, denominator = fraction_input.split('/')
        numerator = int(numerator)
        denominator = int(denominator)
        fraction = Fraction(numerator/denominator)
        if (numerator < 0 or denominator < 0 or (numerator/denominator) > 1):
            raise ValueError
        break
    except (ValueError, ZeroDivisionError):
        pass

percent = round(fraction*100)

if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{percent}%")

#Problem 1
"""
from fractions import Fraction

def main():
    percentage = fuel_percentage(get_fraction())
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


def get_fraction():
    while True:
        try:
            x = Fraction(input("Fraction: "))
            if x < 0 or x > 1:
                raise ValueError
            return x
        except (ValueError, ZeroDivisionError):
            pass

def fuel_percentage(x):
    return round(float(x*100))
main()

# You used fractions library, but what if you don't have to use a library.


def main():
    percentage = fuel_percentage(get_fraction())
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ")
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x < 0 or y < 0 or x > y:
                raise ValueError
            return x/y
        except (ValueError,ZeroDivisionError):
            print("Enter the correct fraction. Eg. 3/4")


def fuel_percentage(x):
    return round(float(x*100))
main()
"""