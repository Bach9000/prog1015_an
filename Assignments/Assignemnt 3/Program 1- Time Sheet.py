############################################################
#                                                          #
# Author: Adrian T. Neumann                                #
# Date: 11 November 2018                                   # 
# Description: A program that accepts the number           #
# of hours worked on each of five work days from the       #
# user, then displays different information calculated     #
# about those entries as output.                           #
#                                                          #
############################################################




# Compute number of days at work
def NonZeroHours(in_hours):

    DaysWorked = 0

    for hours in in_hours:
        if hours != 0:
            DaysWorked = DaysWorked + 1

    
    return DaysWorked


def CalulateTotalHours(in_hours):

    Time = 0
   
    # Sum the hours
    for days in range(5):
        Time += in_hours[days]

    
    return Time


# Calculate the number of hours on any given day
def CalculateMaxHours(in_hours):

    # Sort the HoursWorked list
    SortedHoursWorked = sorted(in_hours)

    # Select the greatest value
    MaxHours = SortedHoursWorked[-1]

    return MaxHours


# Validate the daily hours worked   
def CollectHoursWorked(in_message):
   

    
   
    NumberString = ""
    # Main validation loop
    while NumberString.isdigit() == False:
       
        NumberString = input(in_message)
        Number = int(NumberString)
        
        # Checks to make sure that only increments of 24 hours values are entered
        if Number < 0 or Number > 24:
            
            # Break out of main validation loop
            NumberString = "Incorrect hours"
        
        else:
            return Number
        


def main():
 
 
    # Main program loop flag
    DoYouWantToContinue = "Y"
    NumberOfDays = 5
    
    while DoYouWantToContinue == "Y":
        
        
        # Variables and Input
        HoursWorked = []
        SortedHoursWorked = []
        MaximumHoursWorked = 0
        DaysMaximumHoursWorked = 0

        DayOne = ""
        DayTwo = ""
        DayThree = ""
        DayFour = ""
        DayFive = ""
    
    
        
    
        # Collect hours worked on each of five workdays
        HoursWorked.append(CollectHoursWorked( "Enter hours worked on Day #1: " ))
        HoursWorked.append(CollectHoursWorked( "Enter hours worked on Day #2: " ))
        HoursWorked.append(CollectHoursWorked( "Enter hours worked on Day #3: " ))
        HoursWorked.append(CollectHoursWorked( "Enter hours worked on Day #4: " ))
        HoursWorked.append(CollectHoursWorked( "Enter hours worked on Day #5: " ))
        
        # Processing

        # Calculate maximum hours, total hours, days actually worked, and average hours
        MaximumHoursWorked = CalculateMaxHours(HoursWorked)

        TotalHours = CalulateTotalHours(HoursWorked)

       #DaysWorked = NonZeroHours(HoursWorked)

        AverageHours = TotalHours / NumberOfDays

        Day = []

        # Calculate the days when the maximum hours were worked
        for days in range(NumberOfDays):
            if HoursWorked[days] == MaximumHoursWorked:
                Day.append(days + 1)
            else:
                Day.append("")

        # Assign maximum workload days to individual variable for ouput formatting
        DayOne,DayTwo,DayThree,DayFour,DayFive = Day

        SlackDay = []

        # Calculate slackdays
        for days in range(NumberOfDays):
            if HoursWorked[days] < 7:
                SlackDay.append(days + 1)

        # Output    
        print("--------------------------------------------------------------------------")
        print("The most hours worked was on: ")
        print("Day(s)# {0} {1} {2} {3} {4} when you worked {5} hours.".format(DayOne,DayTwo,DayThree,DayFour,DayFive,MaximumHoursWorked))
        print("--------------------------------------------------------------------------")
        print("The total number of hours worked was: {0} ".format(TotalHours))
        print("The average number of hours worked on each day was: {0} ".format(AverageHours))
        print("------------------------------------------------------------------------- ")
        print("Days you slacked off (i.e. worked less than 7 hours):")
        
        # Print slack days
        for days in SlackDay:
            print('Day #',days,':',HoursWorked[days-1],'hours')
        
        
    
        DoYouWantToContinue = input("Enter 'y' to continue: ").upper()

    
    
if __name__ == "__main__":
    main()
