#Problem 2
#version 1
"""
import sys
import random

from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 2:
    sys.exit("Invalid usage")

if len(sys.argv) == 3:
    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")

user_input = input("Input: ")

if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(f"Output: {figlet.renderText(user_input)}")

if len(sys.argv) == 3:
    figlet.setFont(font=sys.argv[2])
    print(f"Output: {figlet.renderText(user_input)}")
"""

#Your code mixes these steps a bit. For example, it checks for one error, then asks for input, then handles the valid cases.
#version 2
"""
import sys
import random

from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(f"Output: {figlet.renderText(input('Input: '))}")

elif len(sys.argv) == 2:
    sys.exit("Invalid usage")

elif len(sys.argv) == 3:
    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")
    elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
        figlet.setFont(font=sys.argv[2])
        print(f"Output: {figlet.renderText(input('Input: '))}")
    else:
        print("Invalid usage")

"""
#Right now, the input() and print() calls are still in two different places.
#version 3
"""
import sys
import random

from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))

elif len(sys.argv) == 3:
    if sys.argv[2] in figlet.getFonts():
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

user_input = input("Input: ")
print(f"Output: {figlet.renderText(user_input)}")
"""
#This code is clean, but with one bug.
#version 4 (python figlet.py -x slant) with this command it should exit, but it didn't.

"""
import sys
import random

from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))

elif len(sys.argv) == 3:
    if sys.argv[2] in figlet.getFonts():
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")                        # changed place of this line
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

user_input = input("Input: ")
print(f"Output: {figlet.renderText(user_input)}")
"""
#This is great solution but let's make it in a more pythonic way.

import sys
import random

from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))

elif len(sys.argv) == 3:
    if (sys.argv[2] in figlet.getFonts()) and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

user_input = input("Input: ")
print(f"Output: {figlet.renderText(user_input)}")