# Author: Adrian T. Neumann
# Date: 10/2/2018
# Description: Logic Gate Test code based on pseudo code given in exercise eight.  Pseudocode will test the logic gate 
# included in the Oct2 folder


def main():
 
 
    # Input and Variables
    P = True
    Q = False
    R = True
    
    # Processing
    if((P or Q) and not(Q and R)):
        print("Something printed!")
    
    # Output
    print("Logic gate evaluates to False!")	
    
    
if __name__ == "__main__":
    main()
