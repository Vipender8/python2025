expression = input("Expression: ")

x,y,z = expression.split()

x = int(x)
z = int(z)

if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "*":
    print(f"{x * z:.1f}")
else:
    print(f"{x / z:.1f}")

"""
#Problem 4
def main():
    expression = input("Expression: ").strip()
    print(f"{interpreter(expression):0.1f}")

def interpreter(i):
    x,y,z = i.split()

    if y == "+":
        return float(x) + float(z)
    elif y == "-":
        return float(x) - float(z)
    elif y == "/":
        return float(x) / float(z)
    else:
        return float(x) * float(z)
main()

#More robust code.
def interpreter(i):
    x, y, z = i.split()

    # Convert to numbers once at the start
    num1 = float(x)
    num2 = float(z)

    # Now use the numbers in your checks
    if y == "+":
        return num1 + num2
    elif y == "-":
        return num1 - num2
    elif y == "/":
        return num1 / num2
    else: # or elif y == "*"
        return num1 * num2
"""