# Author: Adrian T. Neumann
# Date: 11 October 2018
# Description: Putting the Hogwarts' Sorting Hat into a function.

from random import randint
import re
import sys

def AssignHouse(in_Name):

    Number = 0
    LastName = in_Name

    
    if LastName == "Potter":
            House = "Gryffindor"
    elif LastName == "Malfoy":
            House = "Slytherin"
    else:
        Number = randint(1, 4)
   
    if Number == 1:
        House = "Gryffindor"
    elif Number == 2:
        House = "Hufflepuff"
    elif Number == 3:
        House = "Ravenclaw"
    elif Number == 4:
         House = "Slytherin"

    return House


def main():
 
    # Input and Variables
    NamePatternMatch = re.compile('[A-Z][a-z]+')
    Gryffindor = 0
    Hufflepuff = 0
    Ravenclaw = 0
    Slytherin = 0
    
    for steps in range(0,10):
    A    print("")
        Name = input("""To get assigned to a House, please enter your last name: 
        first letter capitalized followed by one or more letters lower case:  """ )
        print("")
    
   
   # Validation & Processing & Output

        if NamePatternMatch.fullmatch(Name):
            print("{0} has been assigned to House {1}".format(Name,AssignHouse(Name)))	
            if AssignHouse(Name) == "Gryffindor":
                Gryffindor = Gryffindor + 1
            elif AssignHouse(Name) == "Hufflepuff":
                Hufflepuff = Hufflepuff + 1
            elif AssignHouse(Name) == "Ravenclaw":
                Ravenclaw = Ravenclaw + 1
            elif AssignHouse(Name) == "Slytherin":
                Slytherin = Slytherin + 1
        else:
            print("Last name does not match pattern!")
            SystemExit()   
    
    print("")
    print("""There are {0} students in House Gryffindor, {1} students in House Hufflepuff, 
    {2} students in House Ravenclaw, and {3} students in House Slytherin""".format(Gryffindor,Hufflepuff,Ravenclaw,Slytherin))

if __name__ == "__main__":
    main()
