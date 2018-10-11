# Author: Adrian T. Neumann
# Date: 10/11/2016
# Description: This program will determine whether the input year is a leap year.  
# If the year is evenly divisible by 400 or 4 and not by 100, it is a leap year

#def LeapYear(in_year)

def DetermineLeapYear(in_year): 

    Year = in_year
   
    if (Year % 4 == 0 and Year % 100 != 0): 
        return True
    elif (Year % 400 == 0): 
        return True
    else:
        return False


   
   
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
