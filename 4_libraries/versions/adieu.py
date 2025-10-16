#Problem 3
#version 1
"""
name_list = []
while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        break
print(name_list)
"""
# Now use library to get the desired output.
#version 2
"""
import inflect
p = inflect.engine()
name_list = []
while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        break
print(f'Adieu, adieu, to {p.join(name_list,final_sep="")}')
"""
#There is one bug here, it does not print the sentence on the next line.
#version 3
"""
import inflect

p = inflect.engine()
name_list = []
while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        break
print()
print(f'Adieu, adieu, to {p.join(name_list)}')
"""
#The above code is clean and robust, but still we can add function.
#Final code
import inflect

p = inflect.engine()
name_list = []
while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        break
print()
print(f'Adieu, adieu, to {p.join(name_list)}')