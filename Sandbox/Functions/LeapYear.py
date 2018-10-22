# Author: Adrian T. Neumann
# Date: 10/11/2016
# Description: This program will determine whether the input year is a leap year.  
# If the year is evenly divisible by 400 or 4 and not by 100, it is a leap year


from modules import DetermineLeapYear
   
   
def main():
 
 
    # Input and Variables
    Year = int(input("Please enter a year to determine whether it is a leap year: "))
    
     # Processing

    # Output	
    if DetermineLeapYear(Year):
        print("{0} Is a leap year!".format(Year))
    else:
        print("{0} Is not a leap year!".format(Year))
    
if __name__ == "__main__":
    main()
