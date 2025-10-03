def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    tip = float(dollars) * float(percent)
    print(f"Leave ${tip: .2f}")


def dollars_to_float(d):
    d = float(d.replace("$",""))
    return f"{d:.1f}"



def percent_to_float(p):
    p = float(p.replace("%",""))
    return (p/100)

main()

"""
#Problem 5
def main():
    dollars = dollars_to_float(input("How much was the meal: "))
    percent = percent_to_float(input("What percent would you like to tip: "))
    tip = dollars*percent
    print(f"Leave: ${tip:0.2f}")

def dollars_to_float(d):
    d = float(d.replace("$",""))
    return d

def percent_to_float(p):
    p = float(p.replace("%",""))
    return p/100

main()
"""