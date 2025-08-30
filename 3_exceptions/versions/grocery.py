def main():
    dic = items()
    for key in sorted(dic):
        print(dic[key], key )


def items():
    dic = {}
    while True:
        try:
            item = input().strip().upper()
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
        except EOFError:
            break
    return dic

main()
