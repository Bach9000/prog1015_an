# Author: Adrian T. Neumann
# Date: 11 October 2018
# Description: Putting the Hogwarts' Sorting Hat into a function.

from random import randint
import re
import sys

def CountStudents(in_house_name):
    
    # Variables
    HouseTotal = 0
    Gryffindor = 0
    Hufflepuff = 0
    Ravenclaw = 0
    Slytherin = 0

    HouseName = in_house_name
    
    # Processing

    if HouseName == "Gryffindor":
        Gryffindor = Gryffindor + 1
        return Gryffindor    
    
    elif HouseName == "Hufflepuff":
        Hufflepuff = Hufflepuff + 1
        return Hufflepuff    
    
    elif HouseName == "Ravenclaw":
        Ravenclaw = Ravenclaw + 1
        return Ravenclaw
    
    elif HouseName == "Slytherin":
        Slytherin = Slytherin + 1
        return Slytherin

  

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
    Name = ""
    HouseGryffindor = 0
    HouseHufflepuff = 0
    HouseRavenclaw = 0
    HouseSlytherin = 0


    while Name != "q":
        print("")
        Name = input("""To get assigned to a House, please enter your last name: 
        first letter capitalized followed by one or more letters lower case. Enter 
        'q' to quit:  """ )
        print("")
    
   
   # Validation & Processing & Output

        if NamePatternMatch.fullmatch(Name):
            AssignedHouse = AssignHouse(Name)
            print("{0} has been assigned to House {1}".format(Name,AssignedHouse))	

            if AssignedHouse == "Gryffindor":
                HouseGryffindor = HouseGryffindor + 1
            elif AssignedHouse == "Slytherin":  
                HouseSlytherin = HouseSlytherin  + 1
                
            elif AssignedHouse == "Hufflepuff":
                HouseHufflepuff = HouseHufflepuff + 1
            elif AssignedHouse == "Ravenclaw":
                HouseRavenclaw = HouseRavenclaw + 1
                       
            # if Name == "q":
            #     print("")
            #     print("There are {0} students in House Gryffindor, {1} students in House Hufflepuff,".format(HouseGryffindor,HouseHufflepuff)) 
            #     print("{0} students in House Ravenclaw, and {1} students in House Slytherin".format(HouseRavenclaw,HouseSlytherin))
        

            
            
        elif Name == "q":
            print("")
            print("There are {0} students in House Gryffindor, {1} students in House Hufflepuff,".format(HouseGryffindor,HouseHufflepuff)) 
            print("{0} students in House Ravenclaw, and {1} students in House Slytherin".format(HouseRavenclaw,HouseSlytherin))
            sys.exit()
        else:
            print("Last name does not match pattern!")
    

    print("")
    
if __name__ == "__main__":
    main()
