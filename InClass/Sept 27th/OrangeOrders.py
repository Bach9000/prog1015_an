# Author: Adrian T. Neumann
# Date: September 27, 2018
# Description: Create a program called "Orange Orders" that calculates the price of a shipment of oranges from an 
# oline store.  The program calculates total price of oranges given a price per pound of $1.99, and flat shipping price of $7.50
# on orders less than a 100 pounds.  On orders of a 100 pounds or more the flat shipping price is changed to $6.00.  The program 
# calculates the total price of an order given the total pounds of oranges ordered.
#
#Pseudocode
#1.Hard code price of oranges per pound variable
#2.Hard code flat rate shipping price variable
#3.Collect total order quantity of oranges from user
#4.If the total quantity of oranges ordered is equal to or greater than 100 pounds, go to step 5, or if not, go to step 6
#5.Calculate the adjusted total order price by multiplying the order quantity from step 3 by the value from step 1 and then adding the value from step 2 minus $1.50
#6.Calculte the total order price by multiplying the order quantity from step 3 by the value from step 1 and then adding the value from step 2
#7.Display the total order price for a given quantity of oranges weighed in pounds. 
#


def main():
 
 
    # Input and Variables
    OrangePricePerPound = 1.99
    FlatShippingRate = 7.50
    TotalPoundsOrange = int(input("Please enter the total quantity of oranges ordered in Lbs: "))
    
    
    
    # Processing
    if TotalPoundsOrange >= 100:
        TotalOrderPrice = TotalPoundsOrange * OrangePricePerPound + FlatShippingRate - 1.50
    TotalOrderPrice = TotalPoundsOrange * OrangePricePerPound + FlatShippingRate 
    


    # Output
    print("The total price of shipping {:.0f} Lbs of Ornages is ${:.2f}".format(TotalPoundsOrange,TotalOrderPrice))
    
    
if __name__ == "__main__":
    main()
