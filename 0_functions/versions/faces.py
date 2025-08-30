input = input()

def main():
    print(emotion(input))


def emotion(input):
    return (input.replace(":)" ,"🙂")
                .replace(":(","🙁"))


main()

