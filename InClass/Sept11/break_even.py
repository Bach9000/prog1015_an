# Author: Adrian Neumann
# Date: Sept 11, 2018
# Description: The following steps calculate a company’s break-even point, the number of units of goods the company must manufacture and sell in order to break even:
# A.Assign the value 5000 to the variable fixed_costs.
# B.Assign the value 8 to the variable price_per_unit.
# C.Assign the value 6 to the variable cost_per_unit.
# D.Assign the value fixed_costs divided by (the difference of price_per_unit and cost_per_unit) to the variable break_even_point.
# E.Display the value of the variable break_even_point in a console application.




def main():
    # Input and Variables
    fixed_costs = 5000
    price_per_unit = 8
    cost_per_unit = 6
    
    # Processing
    break_even_point = fixed_costs/(price_per_unit-cost_per_unit)
    
    # Output
    print(break_even_point)
    
	
if __name__ == "__main__":
    main()
