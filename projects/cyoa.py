"""MY CYOA PROJECT: A RANDOM QUIZ"""

from random import randint


answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
true = ["T", "t", "True"]
false = ["F", "f", "False"]
correct = 0 #Storing the correct answers

def main() -> None:
    """The Entrypoint of the quiz"""
    welcome: str = str(greet())
    quiz_begin: str = str(begin())
    extra_fun: str = str(just_for_fun())


def greet() -> None:
    """A welcome note into the game"""
    print("Welcome to a quiz game that is going to test your knowledge on random facts.")
    print("I wish you the best of luck! Have fun and collect as many correct answers as you can.")


def begin() -> str:
    """Begin the quix here"""
    name = input ("What's your name?") #Storing the user's name
    print ("\nOK, " +  name +", let's get started. choose one of the following three options.")
    print ("A. Animals B. disney movies c. exit the quiz")
    quiz_choice = input("what is your coice? ")
    if quiz_choice in answer_A:
        return quiz_animals()
    else:
        if quiz_choice in answer_B:
            return quiz_movies()
        else:
            return greet()


def quiz_animals() -> str:
    """True or False qustions aboiut animals"""
    correct: int = 0
    print ("\nThere is a species of Jelly Fish that is immortal.") 

    choice = input("True or False? ")
    if choice in true:
        correct += 1 #If correct, the user gets one point
    else:
        correct += 0
  
    print ("\nA king Cobra venom is not deadly")
    choice = input("true or false?")
    if choice in false:
        correct += 1
    else:
        correct += 0  

    print ("\nCows cannot have dreams unless they sleep standing")
    choice = input("True or False? ")
    if choice in false:
        correct += 1
    else:
        correct += 0 
  
    print ("\nA housefly hums in the key of C")
    choice = input("True or False? ")
    if choice in true:
        correct += 1
    else:
        correct += 0  
  
    print ("\nSea otters hold their paws in order to keep from losing one another when sleeping.")
    choice = input("True or False? ")
    if choice in true:
        correct += 1
    else:
        correct += 0
  
    print ("\nThe Ram is the overall best animal to have as a mascot.")
    choice = input(">>> ")
    if choice in true:
        correct += 1
    else:
        correct += 0
    
    print ("\nYou're finished with the quiz You got", correct, "out of 6 correct.")


def quiz_movies() -> str:
    """a quiz on disney movie"""
    correct: int = 0
    print ("\nDumbo is disney's shortest feature.") 
    choice = input("True or False? ")
    if choice in true:
        correct += 1 #If correct, the user gets one point
    else:
        correct += 0
  
    print ("\noriginally, there was supposed to be seven dwarfs in snow white.")
    choice = input("true or false?")
    if choice in false:
        correct += 1
    else:
        correct += 0  

    print ("\nRobin Williams played Jafar in Aladdin.")
    choice = input("True or False? ")
    if choice in false:
        correct += 1
    else:
        correct += 0 
  
    print ("\nIt took animators almost three years to complete the stampede scene in lion king.")
    choice = input("True or False? ")
    if choice in true:
        correct += 1
    else:
        correct += 0  
  
    print ("\nThe director of Lilo and Stitch was also the voice actor for Stich.")
    choice = input("True or False? ")
    if choice in true:
        correct += 1
    else:
        correct += 0
  
    print ("\nDinesy should create a short film on how great it is to be a Tar Heel.")
    choice = input("True or False?")
    if choice in true:
        correct += 1
    else:
        correct += 0
    
    print("\nYou're finished with the quiz. You got", correct, "out of 6 correct.")

def just_for_fun() -> str:
    """THIS IS JUST EXTRA"""
    while input("would you like to hear a random fact? yes/no -") == "yes":
        return random_question()

    return ("Thanks for playing!")
       
       
        
def random_question() -> str:
    random: int = randint(0, 10)
    if random < 2:
        print(f"Franklin Street was named after Ben Franklin")
    else:
        if random < 3:
            print(f"Chapel Hill has been referred to as the 'southern part of heaven'!")
        else:
            if random < 5:
                print(f"Carolina will always be better than duke.")
            else:
                print(f"No matter what... GDTBATH...")


if __name__ == "__main__":
  main()

