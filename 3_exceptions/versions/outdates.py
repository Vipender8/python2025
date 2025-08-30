months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def main():
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                m,d,y = date.split("/")
                month = int(m)
                day= int(d)
                if month > 12 or day > 31:
                    raise ValueError
                print(f"{y}-{month:02}-{day:02}")
                break

            elif "," in date:
                parts = date.split(",")
                subpart = parts[0].split()
                year = parts[1]
                month = subpart[0].title()
                month_num = months[month]
                date = int(subpart[1])
                if date > 31:
                    raise ValueError
                print(f"{year}-{month_num:02}-{date:02}")
                break
        except (ValueError,KeyError):
            pass

main()
