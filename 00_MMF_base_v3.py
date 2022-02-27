# Import statements
import re
import pandas


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


# Checks number of tickets left and warns user
# if maximum is being approached
def check_tickets(tickets_sold, ticket_limit):
    # tells user how many seats are left
    if tickets_sold < ticket_limit - 1:
        print("You have {} seats left".format(ticket_limit - tickets_sold))

    # warns user that only one seat is left
    else:
        print("*** There is ONE seat left!! ***")

    return ""


# Gets ticket price based on age
def get_ticket_price():

    # Get age (between 12 and 130)
    age = int_check("Age: ")

    # check that age is valid...
    if age < 12:
        print("Sorry you are too young for this movie")
        return "invalid ticket price"
    elif age > 130:
        print("That is very old - it looks like a mistake")
        return "invalid ticket price"

    # Calculate ticket price
    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price


# ----- Main Routine -----

# Set up dictionaries / lists needed to hold data

# Initialise loop so it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# Initialise lists
all_names = []
all_tickets = []

# Data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

# Ask user if they have used the program before
# if no, show instructions

# Begin loop to get details
while name != "xxx" and ticket_count < MAX_TICKETS:

    # print number of tickets left
    check_tickets(ticket_count, MAX_TICKETS)

    # Get name (can't be blank), if the name is not 'xxx' add one to the ticket_counter
    name = not_blank("Name: ")

    if name == "xxx":
        break

    # Get ticket price based on age
    ticket_price = get_ticket_price()

    # If age is invalid, restart loop (and get name again)
    if ticket_price == "invalid ticket price":
        continue

    # add one to the ticket counter
    ticket_count += 1
    ticket_sales += ticket_price

    # add name and ticket to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (apply surcharge if needed)

# End of ticket loop

# print details...
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

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
