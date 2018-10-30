# Author: Adrian T. Neumann
# Date: October30
# Description: Validate the sum of two numbers 


def main():
 
   
   # Initialize variables
    NumberOne = 0
    NumberTwo = 0
    ContinueToCalculate = "Y"

    while ContinueToCalculate == "Y":
        
        # Initialize variables
    
        NumberOne = input("Please enter a first integer!")
        
        
        # Input
        if NumberOne.isdigit() == False: 
            NumberOne = input("Incorrect input! Please enter a first integer: ")
        else:
            One = int(NumberOne)
        
        NumberTwo = input("Pleaes enter a second intger!")



        if NumberTwo.isdigit() == False: 
            NumberTwo = input("Incorrect input! Please enter a second integer: ")
        else:
            Two = int(NumberTwo)
        
        
               
        # Processing
        Sum = One + Two
        
        # Output	
        
        print("The sume of the first and second integer is: {0}".format(Sum))
        print("")
        ContinueToCalculate = input("Do you want to continue? Enter 'Y/y' to continue or 'N/n' to quit: ").upper()



if __name__ == "__main__":
    main()
