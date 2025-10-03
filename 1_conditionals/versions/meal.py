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
"""
#problem 5
def main():
    time = input("What time is it? ")
    time_in_decimal = convert(time)

    meal_timing = meal_time(time_in_decimal)
    if meal_timing:
        print(meal_timing)

def convert(t):
    h,m = t.split(":")
    hours = float(h)
    minutes = float(m)
    return (hours + minutes/60)

def meal_time(d):
    if 7.0 <= d <= 8.0:
        return "breakfast time"
    elif 12.0 <= d <=13.0:
        return "lunch time"
    elif 18.0 <= d <= 19.0:
        return "dinner time"
    else:
        return

main()
"""