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
