################################################################
#                                                              #
#  Author: Adrian T. Neumann                                   #
#  Date Created: 2018-10-16                                    #
#  Description:                                                # 
#  A program that computes monthly auto                        #
#  insurance according to the following schedule.              #
#  If you are male and between 15 and 24 the cost is vehicle   #
#  cost times 25% divided by 12. If you are male and between   # 
#  25 and 39 the cost is vehicle#  cost times 17% divided by   #
#  12. If you are male and between 40 and 69 the cost is       #
#  vehicle cost times 10% divided by 12. If you are female and #
#  between 15 and 24 the cost is vehicle cost times 20%        #
#  divided by 12.  If you are female and                       # 
#  between 15 and 24 the cost is vehicle cost times 15%        #
#  divided by 12. If you are female and between                #
#  25 and 39 the cost is vehicle#  cost times 15% divided by   #
#  12. If you are female and between                           #
#  40 and 70 the cost is vehicle cost times 17% divided by     #
#  12.                                                         #
#                                                              #   
################################################################

import sys
import re



    # Function to valid driver age
def ValidateAge(in_age):
    
    TestAge = re.compile('[0-9]{1,3}')
    
    # Validate input string and convert to integer if matched, 
    # else print warning message and exit gracefully
    if TestAge.fullmatch(in_age):
        return int(in_age)
    else:
        print("")
        print("Invalid numeric input!")
        sys.exit()

   
   # Function to validate vehicle price
def ValidatePrice(in_price):
    
    TestAge = re.compile('[0-9]{1,10}')
    
    # Validate input string and convert to integer if matched, 
    # else print warning message and exit gracefully
    if TestAge.fullmatch(in_price):
        return int(in_price)
    else:
        print("")
        print("Invalid numeric input!")
        sys.exit()
    
    
    # Function to calculate insurance premium given gender, age, and vehicle price
def DetermineInsurancePremium(in_sex,in_age,in_vehicle_price):

    Gender = in_sex

    Age = in_age

    CostOfVehicle = in_vehicle_price
    
    # For males premium is computed according to an age bracket   
    if Gender == "MALE":
        if Age < 25:
            MonthlyPremium =  CostOfVehicle * 0.25 / 12
        elif Age >= 25 and Age < 40: 
            MonthlyPremium =  CostOfVehicle * 0.17 / 12
        elif Age >= 40 and Age < 70:
            MonthlyPremium =  CostOfVehicle * 0.10 / 12
    
     # For females premium is computed according to an age bracket 
    if Gender == "FEMALE":
        if Age < 25:
            MonthlyPremium =  CostOfVehicle * 0.20 / 12
        elif Age >= 25 and Age < 40:
            MonthlyPremium =  CostOfVehicle * 0.15 / 12
        elif Age >= 40 and Age < 70:
            MonthlyPremium =  CostOfVehicle * 0.10 / 12
   
    return MonthlyPremium



def main():


    #Input and Variable

    # Collect gender, age and vehicle price from the user
    Sex = input("Are you 'Male' or 'Female': ").upper()
    print("")
    PayeeAge = ValidateAge(input("Enter your age: "))
    print("")
    VehiclePrice = ValidatePrice(input("Enter the purchase price of the vehicle: "))

    IsPerson = False

    IsDriver = False


    #Processing
    if Sex == "MALE" or Sex == "FEMALE":
       IsPerson  = True

    if PayeeAge >= 15 or PayeeAge < 70:
            IsDriver = True
    
    # If gender and age boolean variables are true, call calculate insurance premium function,
    # else print warning message and exit gracefully
    if IsDriver and IsPerson:
        Premium = DetermineInsurancePremium(Sex,PayeeAge,VehiclePrice)
    else:
        print("")
        print("You are not insurable!")
        SystemExit() 
    
    #Output

    # Print formatted insurance premium calculation      
    print("")
    print("Your monthly insurance will be ${:.2f}".format(Premium))
   

if __name__ == "__main__":
    main()

 