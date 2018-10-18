# Author: Adrian T. Neumann
# Date: ??
# Description: A program to Calculate the on base percentage, slugging percentage, and on base slugging
# given input hits, walsk, bean balls, at bats, sacrifice flies, and total bases.
# The input is validate in a function.

# Import modules for terminating program execution and for validation
import sys
import re

        
def ValidateInput(in_score):
    
    NumberOfDigits = re.compile('[0-9]{1,3}')
    
    #Validate the numeric values
    if NumberOfDigits.fullmatch(in_score):
        return int(in_score)
    else:
        print("You have entered an incorrect value of this player's score!")
        sys.exit()

def main():
 
 
    # Input and Variables
    
    # Collect the player's scores 
    Hits = ValidateInput(input("Enter the players hits: "))
    print("")
            
    Walks = ValidateInput(input("Enter the players walks: "))
    print("")

    BeanBalls = ValidateInput(input("Enter the players bean balls: "))
    print("")

    AtBats = ValidateInput(input("Enter the players at bats: "))
    print("")

    SacrificeFlies = ValidateInput(input("Enter the players sacrifice flies: "))
    print("")

    TotalBases = ValidateInput(input("Enter the players total bases: "))
    print("")


    # Processing
    
    # Calculate the players averages from the players scores
    OnBasePercent = (Hits + Walks + BeanBalls)/(AtBats + Walks + SacrificeFlies + BeanBalls)

    SluggingPercent = TotalBases/AtBats

    OnBasePlusSlugging = OnBasePercent + SluggingPercent


    # Output

    # Print the player's averages
    print("The player's On Base Percent is {0:.2f}, his Slugging Percent is {1:.2f}, and his On Base Plus Slugging is {2:.2f}".format(OnBasePercent,SluggingPercent,OnBasePlusSlugging))	
    
    
if __name__ == "__main__":
    main()
