# Import statements


# Functions go here


# A function to check that the ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # If the name is not blank, program continues
        if response != "":
            return response

        # If the name is blank, show error and repeat the loop
        else:
            print("Sorry - this can't be blank, please enter your name")


# ----- Main Routine -----

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if answer is no

# Loop to get ticket details

    # Get name (can't be blank)
    name = not_blank("Name: ")

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (apply surcharge if needed)

# Calculate total sales and profit

# Output data to text file