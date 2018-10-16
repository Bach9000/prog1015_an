# Author: Adrian T. Neumann
# Date: 11 October 2018
# Description: Putting the Hogwarts' Sorting Hat into a function.

from random import randint
import re
import sys

def assignHouse(in_Name):

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
    
    Name = input("""Please enter your last name, to get assigned to a House
    first letter capital followed by one or more letters lower case:  """ )
    
   
   # Validation & Processing & Output

    if NamePatternMatch.fullmatch(Name):
        print("{0} has been assigned to House {1}".format(Name,assignHouse(Name)))	
    else:
        print("Last name does not match pattern!")
        SystemExit()   


if __name__ == "__main__":
    main()