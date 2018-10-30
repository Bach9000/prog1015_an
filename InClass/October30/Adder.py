# Author: Adrian T. Neumann
# Date: October30
# Description: Validate the sum of two numbers 


def main():
 
   
   # Initialize variables
   One = 0
   Two = 0
   NumberOne = ""
   NumberTwo = ""
   ContinueToCalculateOuter = True
   ContinueToCalculateInner = True

   # Processing
   while ContinueToCalculateOuter:

       if NumberTwo.isdigit() == False:
           print("")

           NumberOne = input("Please enter a first integer!")

           if NumberOne.isdigit():
               One = int(NumberOne)

               while ContinueToCalculateInner:

                   print("")
                   NumberTwo = input("Please enter a second integer!")

                   if NumberTwo.isdigit():
                       Two = int(NumberTwo)
                       ContinueToCalculateInner = False

                   # Processing & Output
                   if NumberOne.isdigit() and NumberTwo.isdigit():
                       Sum = One + Two
                       print("")
                       print("The sume of the first and second integer is: {0}".format(Sum))
                       ContinueToCalculateOuter = False






if __name__ == "__main__":
    main()
