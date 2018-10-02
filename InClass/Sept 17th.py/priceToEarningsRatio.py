# Author: Adrian T. Neumann
# Date: 2018, Sept 17
# Description: Request a company’s earnings-per-share for the year 
# and the price of one share of stock as input, and then display 
# the company’s price-to-earnings ratio (that is, price/earnings)


def main():
 
 
    # Input and Variables
    earningsPerShare = round(float(input("Enter the earnings per share: $")),2)
    pricePerShare = round(float(input("Enter the price per share: $")),2)
    
    # Processing
    priceToEarningsRatio = pricePerShare/earningsPerShare
    
    # Output	
    print("The price-to-earning ratio for the company's share price is $ {:.2f} for $ 1.00 earned".format(priceToEarningsRatio))


if __name__ == "__main__":
    main()
