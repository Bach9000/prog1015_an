# Author: Adrian Neumann
# Date: 2018 Sept10 9:21 am
# Description: Americans eat an average of 350 slices of pizza per second. 
# Code a console application that calculates and outputs how many slices of pizza they eat per day.



def main():
    # Input and Variables
    pizzaPerSecond = 350
    secondsPerDay = 60*60*24
    
    # Processing
    TotalPizzaPerDay = pizzaPerSecond * secondsPerDay  

    # Output	
    print("The number of slices Americans eat per day: " + str(TotalPizzaPerDay))


if __name__ == "__main__":
    main()
