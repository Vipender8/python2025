input = input()

def main():
    print(emotion(input))


def emotion(input):
    return (input.replace(":)" ,"🙂")
                .replace(":(","🙁"))


main()

"""
#Problem 3
def main():
    user_input = input()
    print(convert(user_input))

def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")
main()
"""