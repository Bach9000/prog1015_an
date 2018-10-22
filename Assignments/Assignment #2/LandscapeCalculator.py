###################################################################                                                                 #
# Author: Adrian T. Neumann                                       #
# Date Create: 2018-10-16                                         #
# Description: "Alandscaping companyneeds a program that          #
# computes the price oflandscaping for a newhousing development.  #
#  Workorders are based on:address,plot length and widthinfeet,   #
# type ofgrass(“fescue”, “bentgrass” or “campus”), and number of  #
# trees. The priceiscomputed as follows:There is a baselabour     #
# charge of $1000.If the surface (length * width) is over5000     #
# squarefeet, add $500.The cost is calculated per square foot.    #
# If thegrassis “fescue”the cost is$0.05;                         # 
# for “bentgrass”it is$0.02;“campus”is $0.01.Each tree requested  # 
# has a$100 charge.                                               #
###################################################################


import sys
import re


    # Validate the house number    
def ValidateHouseNumber(in_house):


    HouseNumber = re.compile('[0-9]{1,5}')
    
    # Validate input string and convert to integer if matched, 
    # else print warning message and exit gracefully
    if HouseNumber.fullmatch(in_house):
        return int(in_house)
    else:
        print("Invalid numeric input!")
        sys.exit()



    # Function to validate the depth and width of the property as well
    # as the number of trees    
def ValidateDepthWidthAndTrees(in_value):


    TestValue = re.compile('[0-9]{1,7}')
    
    # Validate input string and convert to integer if matched, 
    # else print warning message and exit gracefully
    if TestValue.fullmatch(in_value):
        return int(in_value)
    else:
        print("Invalid numeric input!")
        sys.exit()



    # Function to determine the lanscaping cost
def LandscapingCost(in_labour,in_grass,in_trees,in_square_feet):


    # Lanscaping cost by grass type given labour cost, number of trees, and square footage
    if in_grass == "fescue":
        TotalCost = in_labour + in_trees * 100 + in_square_feet * 0.05
    elif in_grass == "bentgrass":
        TotalCost = in_labour + in_trees * 100 + in_square_feet * 0.02
    elif in_grass == "campus":
        TotalCost = in_labour + in_trees * 100 + in_square_feet * 0.01
    else:
        TotalCost = -1
    
    return TotalCost




def main():
 
    # Input & Variables

    # Collect the house number a property details
    HouseNumber = ValidateHouseNumber(input("Enter House Number: "))
	
    print("")
    
    PropertyDepth = ValidateDepthWidthAndTrees(input("Enter property depth (feet): "))
	
    print("")
    
    PropertyWidth = ValidateDepthWidthAndTrees(input("Enter property width (feet): "))
	
    print("")

    GrassType = input("Enter the type of grass (fescue, bentgrass, campus): ").lower()
	
    print("")

    NumberOfTrees = ValidateDepthWidthAndTrees(input("Enter the number of trees: "))
	
    print("")

    BaseLabour = 1000

# Processing

    # Calculate square feet
    SquareFeet = PropertyDepth * PropertyWidth

    # Determine additional labour costs
    if SquareFeet > 5000:
        BaseLabour = BaseLabour + 500


    # Call function to determine cost of the landscaping project
    Cost = LandscapingCost(BaseLabour,GrassType,NumberOfTrees,SquareFeet)


# Output

    #validate grass type and print the cost of the landscaping project if validation passes
    if Cost == -1:
        print("You have entered an invalid grass type!")
        SystemExit()
    else:
        print("The total cost for house {0} is: ${1:.2f}".format(HouseNumber,Cost))

if __name__ == "__main__":
    main()
