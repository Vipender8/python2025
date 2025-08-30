
camelcase = input("camelCase: ")

for case in camelcase:
    if case.isupper():
        case = case.lower()
        new_case = case
        final_case = case.replace(new_case,"_")
        print(final_case + case, end="")
    else:
        print(case, end="")
print()
