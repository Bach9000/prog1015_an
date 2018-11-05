# Author: Adrian T. Neumann
# Date: November 5, 2018
# Description: Take two numbers and calculate the highest common divisor.

def GetHighestCommonDivisor(in_num_one,in_num_two):

    
    NumberOne = in_num_one
    NumberTwo = in_num_two
    
    HighestDivisor = 0
    Divisor = 1

    
    
    
    if NumberOne > NumberTwo:
        
        while(Divisor <= NumberTwo):

            if NumberOne % Divisor == 0 and NumberTwo % Divisor == 0:
                HighestDivisor = Divisor
                Divisor = Divisor + 1
            else:
                Divisor = Divisor + 1



        return HighestDivisor

    elif NumberOne < NumberTwo:

        while(Divisor <= NumberOne):

            if NumberOne % Divisor == 0 and NumberTwo % Divisor == 0:
                HighestDivisor = Divisor
                Divisor = Divisor + 1
            else:
                Divisor = Divisor + 1



        return HighestDivisor

    else:

        HighestDivisor = NumberOne

        return HighestDivisor








def main():
 
   
   # Initialize variables
   DoYouWantToContinue = "Y"
   

   # Processing
   while DoYouWantToContinue == "Y":
        
        NumberOne = ""
        NumberTwo = ""

        while NumberOne.isdigit() == False:
           
           print("")
           
           NumberOne = input("Please enter a first whole number!")

        while NumberTwo.isdigit() == False:
           
           print("")

           NumberTwo = input("Please enter a second whole number!")

        # Processing & Output
        if NumberOne.isdigit() and NumberTwo.isdigit():
            
            GCD = GetHighestCommonDivisor(int(NumberOne),int(NumberTwo))
            
            print("")
            print("The GCD of the first and second whole is: {0}".format(GCD))
            print("")
            DoYouWantToContinue = input("Enter 'y' to continue: ").upper()






if __name__ == "__main__":
    main()

