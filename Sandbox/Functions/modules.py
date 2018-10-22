

def DetermineLeapYear(in_year): 

    Year = in_year
   
    if (Year % 4 == 0 and Year % 100 != 0): 
        return True
    elif (Year % 400 == 0): 
        return True
    else:
        return False

