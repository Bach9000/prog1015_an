# Author: Adrian T. Neumann
# Date: 2018, Sept 17th
# Description: Write a console program that converts a weight given 
# in tons (imperial), stones, pounds, and ounces to the metric equivalent 
# in metric tons, kilograms, and grams. Begin by designing your solution 
# to this problem in pseudocode, which will be submitted along with the program.
# After the numbers of tons, stones, pounds, and ounces are input by the user, 
# the weight should be converted entirely into ounces (the lowest common denominator) and then divided by 35.274 to obtain the value in kilos. The Python int function should be used to break the total number of kilos into a whole number of metric tons and kilos. The number of grams should be displayed to one decimal place.
# Required formulas:
# total ounces = 35840 * tons + 224 * stone + 16 * pounds + ounces
# total kilos = total ounces / 35.274
# metric tons = Int(kilos/1000)



def main():
 
 
    # Input and Variables
    # Collect weights from user in imperial Tons, Stones, Pounds, and Ounces
    print("Imperial To Metric Conversion.\n")
    Tons = int(input("Enter the number of tons: "))
    Stones = int(input("Enter the number of stone: "))
    Pounds = int(input("Enter the number of pounds: "))
    Ounces = int(input("Enter the number of ounces: "))

    # Processing
    # Convert imperial weights to Metric Tons, Kilos, and Grams
    TotalOunces = 35840 * Tons + 224 * Stones + 16 * Pounds + Ounces
    TotalKilos = TotalOunces / 35.274
    MetricTons = int(TotalKilos/1000)
    Kilos = int(TotalKilos - MetricTons * 1000)
    TotalGrams = float(TotalKilos * 1000)
    Grams = TotalGrams - Kilos * 1000 - MetricTons * 1000000
    
    # Output
    print("\n")
    print("The metric weight is {:.0f} metric tons, {:.0f} kilos, and {:.1f} grams.".format(MetricTons, Kilos, Grams))	
    
    
if __name__ == "__main__":
    main()
