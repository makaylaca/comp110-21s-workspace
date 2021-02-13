"""Tar Heels exercise redux as a structured program."""

__author__ = "730342554"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(GDTBATH(choice))


# TODO 1: Define the tar_heels function, and its logic, here.
def GDTBATH(choice: int) -> str:
    if ((choice % 2 == 0) and (choice % 7 == 0)):
        print("TAR HEELS")
    else:
        if choice % 2 == 0:
            print("TAR")
        else:
            if choice % 7 == 0:
                print("HEELS")
            else:
                print("CAROLINA")


if __name__ == "__main__":
    main()
