# Initial variable to track game play
User_play='y'


# Set start and last number
start_number=0


# While we are still playing...
while User_play == 'y': 
    

    # Ask the user how many numbers to loop through
    User_value = int(input("How many would you like to see?")) 

    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(start_number, User_value + start_number):

        # Print each number in the range
        print(x)

    # Set the next start number as the last number of the loop
        start_number = x+1

    # Once complete... ask if the user wants to continue
    User_play = input(f"Would you like to play again? (y)es or (n)o?")
    

