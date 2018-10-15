# Author: Adrian T. Neumann
# Date: 10/15/2018
# Description:  GPA Calculator in function 


 #FUNCTION
def CalculateGPA(in_courseName):


    numericGrade = 0.0
  
    letterGrade = input("Please enter a letter grade for {} : ".format(in_courseName)).upper()
    modifier = input("Please enter a modifier (+, - or nothing) : ")
    input("")


    # Determine base numeric value of the grade
    if letterGrade == "A":
        numericGrade = 4.0
    elif letterGrade == "B":
        numericGrade = 3.0
    elif letterGrade == "C":
        numericGrade = 2.0
    elif letterGrade == "D":
        numericGrade = 1.0
    elif letterGrade == "F":
        numericGrade = 0.0
    else:
        print("You entered an invalid letter grade.")
    
    # Determine whether to apply a modifier
    if modifier == "+":
        if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif modifier == "-":
        if letterGrade != "F":     # Minus is not valid on F
            numericGrade -= 0.3

    return numericGrade

def main():


    # Input and Variables
    print("Grade Point Calculator\n")
    print("Course")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")
 
    # Processing
  
    runningTotalOne = CalculateGPA("PROG1700")
    runningTotalTwo = CalculateGPA("NETW1700")
    runningTotalThree = CalculateGPA("OSYS1200")
    runningTotalFour = CalculateGPA("WEBD1000")
    runningTotalFive = CalculateGPA("COMM1700")
    runningTotalSix = CalculateGPA("DBAS1001")

    average = (runningTotalOne + runningTotalTwo + runningTotalThree + runningTotalFour + runningTotalFive + runningTotalSix)/6

    # Output final message and result, with formatting
    print("""******************************************
    """)

    print("The numeric average for PROG1700 is : {}".format(runningTotalOne))
    print("The numeric average for NETW1700 is : {}".format(runningTotalTwo))
    print("The numeric average for OSYS1200 is : {}".format(runningTotalThree))
    print("The numeric average for WEBD1000 is : {}".format(runningTotalFour))
    print("The numeric average for COMM1700 is : {}".format(runningTotalFive))
    print("The numeric average for DBAS1001 is : {}".format(runningTotalSix))
    print("================================================")
    print("The numeric average of all six courses is {0:.2f}.".format(average))
    print("================================================")
if __name__ == "__main__":
    main()
    
