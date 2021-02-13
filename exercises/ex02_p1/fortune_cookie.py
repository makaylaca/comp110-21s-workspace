"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730324554"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    x: int = randint(0, 100)
    print(my_fortune(randint(0, 100)))
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def my_fortune(x: int) -> str:

    if x < 50:
        if x < 25: 
            return("Great things are coming, you just have to be patient and wait.")
        else:
            return("Like a river flows into the sea... some things are just meant to be.")
    else:
        if x < 60:
            return("Don't let your limitations overshadow your talents.")
        else: 
            if x < 75:
                return("Happiness begins with facing life with a smile and a wink.")
            else:
                return("Keep your face to the sunshine and Syou wll never see shadows.")

    


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
