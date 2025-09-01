user_input = input("Time: ")

def main(user_input):
    time = convert(user_input)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes)
    minutes = minutes/60
    sum = hours + minutes

    return sum


if __name__ == "__main__":
    main(user_input)
