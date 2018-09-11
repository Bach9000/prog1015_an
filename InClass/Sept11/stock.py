# Author: Adrian Neumann
# Date: Sept 11, 2018
# Description: Stock Purchase The following steps calculate the amount of a stock purchase:
# A.Assign the value 25.625 to the variable cost_per_share.
# B.Assign the value 400 to the variable number_of_shares.
# C.Assign the product of cost_per_share and number_of_shares to the variable markdown.
# D.Display the value of the variable markdown in the console application.





def main():
    
    # Input and Variables
    cost_per_share = 25.625
    number_of_shares = 400
    
    # Processing
    markdown = cost_per_share*number_of_shares



    # Output
    print(markdown)

    
if __name__ == "__main__":
    main()
