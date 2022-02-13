# Import statements


# Functions go here


# Checks that ticket name is not blank
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


# Checks a number is between a min and max
def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} and {}".format(low_num, high_num)

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if low_num <= response <= high_num:
                return response
            else:
                print(error)

        # if an integer is not entered, display an error
        except ValueError:
            print(error)


# ----- Main Routine -----

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if answer is no

# Loop to get ticket details
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # print number of tickets left
    if count < 4:
        print("You have {} seats left".format(MAX_TICKETS - count))

    # Warns user that only one seat is left
    else:
        print("*** There is only ONE seat left! ***")

    # Get name (can't be blank), if the name is not 'xxx' add one to the counter
    name = not_blank("Name: ")

    if name != "xxx":
        count += 1
    else:
        break

    # Get age (between 12 and 130)
    age = int_check("Age: ", 12, 130)
    print()

# End of ticket loop

# If all tickets are sold print statement
if count == MAX_TICKETS:
    print("You have sold all the available tickets!")

# If not all tickets are sold, print how many were sold and how many were left
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available".format(count, MAX_TICKETS - count))

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (apply surcharge if needed)

# Calculate total sales and profit

# Output data to text file