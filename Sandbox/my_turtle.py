# Author: Adrian T. Neumann
# Date: October30
# Description: First turtle

import turtle

def main():
 
    # Input and Variables
    # Initialize distance
    Distance = -1

    while Distance != 0:
        
        Distance = int(input("Desired line length, zero to quit: "))
        if Distance != 0:
            TurnDirection = int(input("Desired turn(degrees): "))
            color = input("Desired line color: ")
        #  Processing
            turtle.color(color)
            turtle.forward(Distance)
            turtle.right(TurnDirection)
   
    turtle.done()
    # Output	
    
    
if __name__ == "__main__":
    main()
