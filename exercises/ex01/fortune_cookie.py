"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730342554"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
b = ("Your fortune cookie says...")
print(b)

random_fortunes: int = randint(0, 100)

if random_fortunes < 50:
    if random_fortunes < 25: 
        print("Great things are coming, you just have to be patient.")
    else:
        print("Like a river flows into the sea... some things are just meant to be.")
else:
    if random_fortunes < 60:
        print("Don't let your limitations overshadow your talents.")
    else: 
        if random_fortunes < 75:
            print("Happiness begins with facing life with a smile and a wink.")
        else:
            print("Keep your face to the sunshine and you wll never see shadows.")

print("Now, go spread positive vibes!")
