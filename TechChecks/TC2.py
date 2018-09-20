# Author: Adrian T. Neumann
# Date: 20 September 2018
# Description: Given a weekly salary, and number of dependents, write a tax calcualtor that computes provincial 
# tax withheld, the federal tax withheld, 
# the dependent deduction, the total tax withheld, and total take-home pay. 


def main():
 
 
    # Input and Variables
    print("Tax Withholding Calculator \n")
    WeeklySalary = round(float(input("Please enter the full amount of your weekly salary: ")),2)
    NumberOfDependents = int(input("How many dependents do you have?: "))

    # Processing
    ProvTax = 0.06
    ProvTaxWithheld = WeeklySalary * ProvTax
    FedTax = 0.25
    FedTaxWithheld = WeeklySalary * FedTax
    DeductionPerDependent = 0.02
    Deduction = DeductionPerDependent * NumberOfDependents * WeeklySalary
    TotalTaxWithheld = ProvTaxWithheld + FedTaxWithheld - Deduction
    TotalPay = WeeklySalary - TotalTaxWithheld

    # Output
    print("\n")
    print("Provincial tax withheld: ${:.2f}".format(ProvTaxWithheld))
    print("Federal tax withheld: ${:.2f}".format(FedTaxWithheld))
    print("Dependent Deduction for {:.0f} dependents: ${:.2f}".format(NumberOfDependents,Deduction))
    print("Total withheld: ${:.2f}".format(TotalTaxWithheld))
    print("Total Take-Home Pay: ${:.2f}".format(TotalPay))

    
if __name__ == "__main__":
    main()
