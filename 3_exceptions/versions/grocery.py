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


"""
item_dic = {}

def main():
    while True:
        try:
            item = input().upper()
            if item in item_dic:
                item_dic[item] += 1
            else:
                item_dic[item] = 1
        except EOFError:
            break

    for item in sorted(item_dic):
        print(item_dic[item],item)

main()

An alternative way for if else block:
# Get the current count of 'item'. If it's not in the dict, default to 0.
count = item_dic.get(item, 0) 
item_dic[item] = count + 1


#This essentially says, "Get the current count for this item. 
# If there is no current count, assume it's 0. Then, add one to it and update the dictionary."
"""