# Author: Adrian T. Neumann
# Date: October 4, 2018
# Description: ?? 


def main():
 
 
    # Input and Variables
    LetterGrade = input("Please enter a letter grade: ")
    Modifier = input("Please enter a modifier: ")
    
    
    # Processing
    if(LetterGrade.upper() == "A" and Modifier == "+" or Modifier == ""):
        GradePoints = 4.0
    elif(LetterGrade.upper() == "A" and Modifier == "-"):
        GradePoints = 3.7
    elif(LetterGrade.upper() == "B" and Modifier == "+"):
        GradePoints = 3.3
    elif(LetterGrade.upper() == "B" and Modifier == ""):
        GradePoints = 3.0
    elif(LetterGrade.upper() == "B" and Modifier == "-"):
        GradePoints = 2.7
    elif(LetterGrade.upper() == "C" and Modifier == "+"):
        GradePoints = 2.3
    elif(LetterGrade.upper() == "C" and Modifier == ""):
        GradePoints = 2.0
    elif(LetterGrade.upper() == "C" and Modifier == "-"):
        GradePoints = 1.7
    elif(LetterGrade.upper() == "D" and Modifier == "+"):
        GradePoints = 1.3
    elif(LetterGrade.upper() == "D" and Modifier == ""):
        GradePoints = 1.0
    elif(LetterGrade.upper() == "D" and Modifier == "-"):
        GradePoints = 0.7
    elif(LetterGrade.upper() == "F" and Modifier == "+"):
        GradePoints = 0.0
    elif(LetterGrade.upper() == "F" and Modifier == ""):
        GradePoints = 0.0
    elif(LetterGrade.upper() == "F" and Modifier == "-"):
        GradePoints = 0.0        
    else:
        print("You entered an invalid letter grade")
    
    # Output
    print("""Grade Point Calculator
    
    Valid letter grades that
    can be entered: A, B, C, D, F.
    Valid grade modifiers are +, - or nothing.
    All letter grades except F can include a + or - symbol.
    Calculated grade point value cannot exceed 4.0.
    """)
        
   
  
    if(GradePoints == 4.0):
        print("The numeric value is: {:.1f}".format(GradePoints))
    elif(GradePoints == 3.7):
        print("The numeric value is: {:.1f}".format(GradePoints))
    elif(GradePoints == 3.3):
        print("The numeric value is: {:.1f}".format(GradePoints))	
    elif(GradePoints == 3.0):
        print("The numeric value is: {:.1f}".format(GradePoints))	
    elif(GradePoints == 2.7):
        print("The numeric value is: {:.1f}".format(GradePoints))	
    elif(GradePoints == 2.3):
        print("The numeric value is: {:.1f}".format(GradePoints))	
    elif(GradePoints == 2.0):
        print("The numeric value is: {:.1f}".format(GradePoints))	
    elif(GradePoints == 1.7):
        print("The numeric value is: {:.1f}".format(GradePoints))	
    elif(GradePoints == 1.3):
        print("The numeric value is: {:.1f}".format(GradePoints))
    elif(GradePoints == 1.0):
        print("The numeric value is: {:.1f}".format(GradePoints))	
    elif(GradePoints == 0.7):
        print("The numeric value is: {:.1f}".format(GradePoints))	
    elif(GradePoints == 0.0):
        print("The numeric value is: {:.1f}".format(GradePoints))
    else:
        ("You entered an invalid letter grade")				
    
if __name__ == "__main__":
    main()
