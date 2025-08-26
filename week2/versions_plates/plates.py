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
main()
"""There is one isssue with this code. 
Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable"""