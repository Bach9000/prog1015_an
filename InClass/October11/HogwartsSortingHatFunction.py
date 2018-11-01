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
    Name = ""

    GryfStudents = []
    HufStudents = []
    RavStudents = []
    SlythStudents = []
    



    while Name != "q":


        print("")
        Name = input("""To get assigned to a House, please enter your last name: 
        first letter capitalized followed by one or more letters lower case. Enter 
        'q' to quit:  """ )
        print("")
    
   
   # Validation & Processing & Output

        if NamePatternMatch.fullmatch(Name):
            AssignedHouse = AssignHouse(Name)
           # print("{0} has been assigned to House {1}".format(Name,AssignedHouse))
            if AssignedHouse == "Gryffindor":
                GryfStudents.append(Name)
               # GryfTotal = GryfTotal + 1
            elif AssignedHouse == "Hufflepuff":
                HufStudents.append(Name)
            elif AssignedHouse == "Ravenclaw":
                RavStudents.append(Name)
            elif AssignedHouse == "Slytherin":
                SlythStudents.append(Name)


           

        elif Name == "q":
            
            
            for GryfNames in range (len(GryfStudents)):
                print(GryfStudents[GryfNames])
            
            print("{0} Are assigned to House Gryffindor".format(len(GryfStudents)))

            print("")    
            for HufNames in range (len(HufStudents)):
                print(HufStudents[HufNames])
            
            print("{0} Are assigned to House Hufflepuff".format(len(HufStudents)))

            print("")    
            for RavNames in range (len(RavStudents)):
                print(RavStudents[RavNames])
            
            print("{0} Are assigned to House Ravenclaw".format(len(RavStudents)))

            print("")    
            for GryfNames in range (len(SlythStudents)):
                print(SlythStudents[GryfNames])
            
            print("{0} Are assigned to House Slytherin".format(len(SlythStudents)))
                

             
            
                
           # print("There are {0} students in House Gryffindor, {1} students in House Hufflepuff,".format(GryfTotal,HufTotal))
           # print("{0} students in House Ravenclaw, and {1} students in House Slytherin".format(RavTotal,SlythTotal))
            sys.exit()
        else:
            print("Last name does not match pattern!")
    

    
       
   
    
if __name__ == "__main__":
    main()
