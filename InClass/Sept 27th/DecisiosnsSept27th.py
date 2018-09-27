# Author: Adrian T. Neumann
# Date: Sept 27th, 2018
# Description: Calculate weekly pay and overtime pay. 


def main():
 
 
    # Input and Variables
    PayRate = float(input("Enter your hourly pay rate: "))
    HoursWorked = float(input("Enter your weekly hours worked: "))
    
    # Processing
    if HoursWorkd > 40:
        OverTimeHours = HoursWorked - 40
        OverTimePay = OverTimeHours * (PayRate * 1.5)
           
    WeeklyPay = PayRate * HoursWorked


    # Output
    print(WeeklyPay)
    pirnt(OverTimePay)	
    
    
if __name__ == "__main__":
    main()
