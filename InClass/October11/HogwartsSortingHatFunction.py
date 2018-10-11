# Author: Adrian T. Neumann
# Date: 11 October 2018
# Description: Putting the Hogwarts' Sorting Hat into a function.

from random import randint

def assignHouse(in_Name):

    Number = 0
    LastName = in_Name

    if LastName == "POTTER":
        House = "Gryffindor"
    elif LastName == "MALFOY":
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
    Name = input("Please enter your last name to get assigned to a House:").upper()
   
   
    
    # Processing
    
     
       
    # Output
    print("{0} has been assigned to House {1}".format(Name,SortingHat(Name)))	
    
    
if __name__ == "__main__":
    main()
