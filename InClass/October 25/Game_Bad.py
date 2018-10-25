import random

def main():
    
	# Variables
		
	NumberOfGuesses = 10
    
	Target = random.randint(1,100)
    
	# Processing

	# Print welcome message
	print("Welcome to my game!")
    
	# Begin loop to guess the Target random number
	for i in range(NumberOfGuesses):    
    	
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

