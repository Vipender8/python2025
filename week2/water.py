import random

moisture = random.randint(25, 40)


def main():
    moisture = sample()
    days = 0
    print(f"Days {days} Moisture is {moisture}%")

    while moisture > 20:
        days += 1
        moisture = sample()
        print(f"Days {days} Moisture is {moisture}%")
    
    print("Turn on the water!")


def sample():
    global moisture
    moisture = moisture - random.randint(1, 5)
    return moisture

main()