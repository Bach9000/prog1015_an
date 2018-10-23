############################################################
#                                                          #
# Author: Adrian T. Neumann                                #
# Date Create: 2018-10-16                                  #
# Description: ErewhonMobile charges cellular customers a  #
# rate based on the total amount ofdataused by a customer  #
# in the billing period.For simplicity, customers are      #
# charge based on whichrangetheir totaldatausage falls     #
# within. Note, it is not a cumulative charge;your program # 
# will figure out which single range the usage falls into, # 
# then calculate the cost based on that range’s cost.Total # 
# Data UsageRate of ChargeUp to and including200Mb $20.00  # 
# flat rate Over200Mb and up to and including 500Mb$       # 
# 0.105perMbOver500Mband up to and including 1Gb           #
# $0.110perMbOver1Gb $118.00 flat rate                     #
#                                                          #
############################################################

import re
import sys


    # Function to validate data plan 
def ValidateData(in_Mb):

    
    TestMb = re.compile('[0-9]{1,6}')
    
    # Validate input string and convert to integer if matched, 
    # else print warning message and exit gracefully
    if TestMb.fullmatch(in_Mb):
        return int(in_Mb)
    else:
        print("Invalid numeric input!")
        sys.exit()

    

    # Function to calculate cost of data plan
def PlanCalculation(in_data):

    Mb = in_data

    # Calculate cost of data plan according to data usage
    if Mb <= 200:
        Cost = 20.00
    elif Mb > 200 and Mb <= 500:
        Cost = Mb * 0.105
    elif Mb > 500 and Mb <= 1000:
        Cost = Mb * 0.110
    elif Mb > 1000:
        Cost = 118.00


    return Cost



def main():
 

    #Input and Variables

    # Collect and validate data usage in Mb
    MbData = ValidateData(input("Enter data usage (Mb): ")) 
    print("")
    
    #Processing

    # Call function to calculate data cost
    DataCost = PlanCalculation(MbData)
  
    #Output

    # Print formatted cost of data plan    
    print("Total charge is ${:.2f}".format(DataCost))


if __name__ == "__main__":
    main()
