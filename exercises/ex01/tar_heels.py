"""An exercise in remainders and boolean logic."""

__author__ = "730342554"

# Begin your solution here...
rand_number: int = int(input("Enter a number: "))

if ((rand_number % 2 == 0) and (rand_number % 7 == 0)):
    print("TAR HEELS")
else:
    if rand_number % 2 == 0:
        print("TAR")
    else:
        if rand_number % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")