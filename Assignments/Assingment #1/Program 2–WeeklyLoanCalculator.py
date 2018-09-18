# Author: Adrian T. Neumann
# Date: 2018, Sept 17
# Description: Develop a short term loan calculator program as 
# a console application with the following specifications. Begin 
# by designing your solution to this problem in pseudocode, which 
# will be submitted along with the program.
# If A dollars are borrowed at r% interest compounded 
# weekly to purchase something with weekly payments for n years, 
# then the monthly payment is given by the formula:
# If: i  = r/5200 
# Then calculate the monthly payment as:
# monthly payment  =  i/1 – (1 + i)-52n	* A
# Write a console application that calculates the weekly payment 
# after the user gives the amount of the loan, interest rate, and number of years.



def main():
 
 
    # Input and Variables
    print("""Weekly Loan Calculator
                                                                           """)
    LoanAmount = round(float(input("Enter the loan amount: $")),2)
    PercentInterest = round(float(input("Enter the interest rate(%): ")),2)
    PaymentYears = int(input("Enter the number of years: "))
    
    # Processing
    Numerator = PercentInterest/5200
    Denominator = (1-((1 +(Numerator))**(-52*PaymentYears))) 
    CalculatedMonthlyPayment = (Numerator/Denominator) * LoanAmount
    #WeeklyPayment = MonthlyPayment/4
    
    # Output
    print("\n")	
    print("Your weekly payment will be: ${:.2f}".format(CalculatedMonthlyPayment))	
    
if __name__ == "__main__":
    main()
