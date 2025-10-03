import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_first_two_char(s):
        if check_length(s):
            if is_clean(s):
                if check_digit(s):
                    return True


def check_first_two_char(s):
    if s[0:2].isalpha() and s[2:3] !="0":
        return True


def check_length(s):
    if (len(s) <= 6 and len(s) >= 2):
        return True

def is_clean(s):
    # To check is there is space
    if " " in s:
        return False

    for char in s:
        if char in string.punctuation:
            return False

    return True

#To check if there are numbers in between plate.
def check_digit(s):
    i = 0
    for char in s:
        if char.isdigit():
            index = i
            break
        else:
            i += 1
    if s[index:].isdigit():
        return True
    

main()
"""
#getting a tarceback error when plate is having only alphabets eg "Hello"
#reason: when there is no digit in the string, index variable is not getting assigned any value and hence it is throwing an error.


#Easy fix:
def check_digit(s):
    i = 0
    found_digit = False
    for char in s:
        if char.isdigit():
            index = i
            found_digit = True
            break
        else:
            i += 1
    if found_digit:
        return print(index)
    else:
        return print("No digit found")
check_digit("Hello1") 

        #This version works because you added the found_digit flag, which prevents the code from trying to access index when no digit was found.


pythonic way:
def check_digit(s):
    for i, char in enumerate(s):        
        if char.isdigit():
            return s[i:].isdigit()  
    return True
"""


#Problem 4
"""
def main():
    plate_number = input("Plate: ")
    if is_valid(plate_number):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False

    if not s[:2].isalpha():
        return False

    if not s.isalnum():
        return False

    return check_number_inbetween(s)

index = None # If the plate has no digits at all (like "CS"), this loop never runs the break.
             #That means index is never defined. When you later do user_input[index:], you’ll get an UnboundLocalError.
def check_number_inbetween(user_input):
    for i, char in enumerate(user_input):
        if char.isdigit():
            index = i
            break

    if index is None:
        return True

    if not user_input[index:].isdigit():
        return False

    if user_input[index] == "0":
        return False

    return True

main()
"""