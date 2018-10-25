import random

def main():
    
	# Variables

    # Print welcome message
    print("Welcome to my game!")

    Target = random.randint(1,100)
    
	# Initialize guess variable
    Guess = -1
	
	# Processing
	
    # Begin loop to guess the Target random number
    while(Guess!=Target):
    	
        # Collect guess from user
        Guess = int(input("Enter a number: "))
    	
		# Determine whether guess is higher or lower than the target or is a hit
        if Guess < Target:
    		
            print("Higher")
    	
        elif Guess > Target:
    		
            print("Lower")
    	
        elif Guess == Target:
    	
            print("You got it!")
            break

	# Output

	# Print game over message
    print("Game Over")	
    
    
if __name__ == "__main__":
    main()

