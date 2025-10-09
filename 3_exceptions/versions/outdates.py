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

#Problem 4
"""
month_dic = {
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
            date = input("Date: ")
            if "/" in date:
                month,day,year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            elif "," in date:
                part, subpart = date.split(",")
                month, day = part.split(" ")
                month = int(month_dic[month.strip().title()])
                day = int(day)
                year = int(subpart)
            else:
                raise ValueError
            if month > 12 or month < 1 or  day > 31 or day < 1:
                raise ValueError
            print(f"{year}-{month:02}-{day:02}")
            break
        except (ValueError,KeyError):
            pass

main()
"""
#This code works but it looks messy and DRY(Don't repeat yourself) principle is not followed.
"""
if month > 12 or month < 1 or  day > 31 or day < 1:
    raise ValueError
print(f"{year}-{month:02}-{day:02}")
break
#These lines repeats.
"""

def main():
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                month,day,year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            elif "," in date:
                part, subpart = date.split(",")
                month, day = part.split(" ")
                month = int(month_dic[month.strip().title()])
                day = int(day)
                year = int(subpart)
            else:                 # This block is added here.
                raise ValueError
            if month > 12 or month < 1 or  day > 31 or day < 1:
                raise ValueError
            print(f"{year}-{month:02}-{day:02}")
            break
        except (ValueError,KeyError):
            pass

main()

