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


# Checks for an integer more than 0
def int_check(question):

    error = "Please enter a whole number that is more than 0"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            # if the response is zero or lower print an error
            if response <= 0:
                print(error)

            # if the response is greater than zero, the code continues
            else:
                return response

        # if an integer is not entered, display an error
        except ValueError:
            print(error)


# ----- Main Routine -----

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if answer is no

# Loop to get ticket details
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0


while name != "xxx" and ticket_count < MAX_TICKETS:

    # print number of tickets left
    if ticket_count < MAX_TICKETS - 1:
        print("You have {} seats left".format(MAX_TICKETS - ticket_count))

    # Warns user that only one seat is left
    else:
        print("*** There is only ONE seat left! ***")

    # Get name (can't be blank), if the name is not 'xxx' add one to the ticket_counter
    name = not_blank("Name: ")

    if name == "xxx":
        break

    # Get age (between 12 and 130)
    age = int_check("Age: ")
    print()

    # Check that age is valid
    if age < 12:
        print("Sorry, you are too young for this movie")
        continue

    elif age > 130:
        print("That is very old - it looks like a mistake")
        continue

    # Calculate ticket price
    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    ticket_count += 1
    ticket_sales += ticket_price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (apply surcharge if needed)

# End of ticket loop

# Calculate ticket profit
print()
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# If all tickets are sold print statement
if ticket_count == MAX_TICKETS:
    print()
    print("You have sold all the available tickets!")

# If not all tickets are sold, print how many were sold and how many were left
else:
    print()
    print("You have sold {} tickets. \n"
          "There are {} places still available".format(ticket_count, MAX_TICKETS - ticket_count))

# Output data to text file
