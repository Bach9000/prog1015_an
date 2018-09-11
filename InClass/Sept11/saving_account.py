# Author: Adrian Neumann
# Date: Sept 11, 2018
# Description: The following steps calculate the balance at the end of three years when $100 is deposited at the beginning of each year in a savings account at 5 % interest compounded annually:
# A.Assign the value 100 to the variable balance.
# B.Increase the variable balance by 5 % of its value, and add 100.
# C.Increase the variable balance by 5 % of its value, and add 100.
# D.Increase the variable balance by 5 % of its value.
# E.Display the value of balance (rounded to two decimal places) in the console window.





def main():
    # Input and Variables
    balance = 100

    # Processing
    balance = (balance*1.05 + 100)
    balance = (balance*1.05 + 100)
    balance = (balance*1.05)    

    # Output
    print(round(balance,2))


if __name__ == "__main__":
    main()
