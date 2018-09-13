# Author: Adrian T. Neumann
# Date: Sept 13, 2018
# Description:  Simple application to calculate final restaurant bill.  


def main():
 
 
    # Input and Variables
    bill = float(input("Please enter your original bill amount: "))
    # tax = 0.15
    # tip = 0.20

    # Processing
    tax = bill * 0.15
    tip = bill * 0.20
    total = bill + tax + tip
    
    
    # Output
    print("Your original bill amount is: " + str(bill))
    print("Your tax is: " + str(tax))
    print("Your tip is: " + str(tip))
    print("Your total is: " + str(total))	
    
    
if __name__ == "__main__":
    main()
