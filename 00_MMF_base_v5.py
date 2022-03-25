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


# checks a string based on a given list
def string_check(choice, options):

    for var_list in options:

        # if the snack is in one of the lists, return the full word
        if choice in var_list:

            # Get full name of snack and put it in title case so it looks nice
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if chosen option is not valid set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not ok - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "Invalid choice"


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


# get list of snacks
def get_snack():
    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # Each item in valid snacks is a list with
    # valid options for each snack <full name, letter code (a - e)
    # and possible abbreviations etc>
    valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "orange", "juice", "e"]
    ]

    # holds snack order for as single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        # ask for desired snack and put in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        # if item has a number, separate it into two (number / item)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        # if item does not have a number infront of it set number to 1
        else:
            amount = 1
            desired_snack = desired_snack

        # remove white space around snack
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)
        if snack_choice == "Invalid choice":
            print("Please enter a valid snack")

        # check if snack amount is valid
        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "Invalid choice"

        # add snack and amount to list
        snack_row.append(amount)
        snack_row.append(snack_choice)

        # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "Invalid choice":
            snack_order.append(snack_row)


# ----- Main Routine -----

# Set up dictionaries / lists needed to hold data

# lists of valid responses for payment method
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# lists for valid yes / no responses
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# Initialise loop so it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# Initialise lists
all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

surcharge_mult_list = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Lists to store summary data...
summary_headings = ["Popcorn", "M&M's", "Pita Chips", "Water",
                   "Orange Juice", "Snack Profit", "Ticket Price", "Total Profit"]

summary_data = []

# Data frame dictionary
movie_data_dict = {
    'Name': all_names,
    "Ticket": all_tickets,
    "Popcorn": popcorn,
    "Water": water,
    "Pita Chips": pita_chips,
    "M&Ms": mms,
    "Orange Juice": orange_juice,
    "Surcharge_Multiplier": surcharge_mult_list
}

# summary dictionary
summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}

# cost of each snack
price_dict = {
    "Popcorn": 2.5,
    "Water": 2,
    "Pita Chips": 4.5,
    "M&Ms": 3,
    "Orange Juice": 3.25
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
    check_snack = "Invalid choice"
    while check_snack == "Invalid choice":

        # asks user if they want snacks
        want_snack = input("Do you want to order snacks? ").lower()

        # checks whether answer is within the list
        check_snack = string_check(want_snack, yes_no)

    if check_snack == "Yes":
        snack_order = get_snack()

    else:
        snack_order = []

    # assume no snacks have been bought...
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    # Ask for payment method (apply surcharge if needed)
    how_pay = "Invalid choice"
    while how_pay == "Invalid choice":
        how_pay = input("Please choose a payment method (cash or credit) ")
        how_pay = string_check(how_pay, pay_method)

    if how_pay == "Credit":
        surcharge_multiplier = 0.05

    else:
        surcharge_multiplier = 0

    surcharge_mult_list.append(surcharge_multiplier)

# End of loop

# Order columns
movie_frame = pandas.DataFrame(movie_data_dict, columns=["Name",
                                                         "Ticket",
                                                         "Popcorn",
                                                         "Water",
                                                         "Pita Chips",
                                                         "M&Ms",
                                                         "Orange Juice",
                                                         "Surcharge_Multiplier"])


# create snacks column
# fill it with price of snacks
movie_frame["Snacks"] = \
    movie_frame["Popcorn"] * price_dict["Popcorn"] + \
    movie_frame["Water"] * price_dict["Water"] + \
    movie_frame["Pita Chips"] * price_dict["Pita Chips"] + \
    movie_frame["M&Ms"] * price_dict["M&Ms"] + \
    movie_frame["Orange Juice"] * price_dict["Orange Juice"]

# create column called 'Sub Total'
# fill it price for snacks and ticket
movie_frame["Sub Total"] = \
    movie_frame["Ticket"] + \
    movie_frame["Snacks"]

# create surcharge column
movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

# create total column
movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame['Surcharge']

# shorten column names
movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                                          'Pita Chips': 'Chips',
                                          'Surcharge_Multiplier': 'SM'})

# Set up summary dataframe
# populate snack items...
for item in snack_lists:
    # sum items in each snack list
    summary_data.append(sum(item))

# Get snack profit
# Get snack total from panda
snack_total = movie_frame['Snacks'].sum()
snack_profit = snack_total * 0.2
summary_data.append(snack_profit)

# Get ticket profit and add to list
ticket_profit = ticket_sales - (5 * ticket_count)
summary_data.append(ticket_profit)

# Work out total profit and add to list
total_profit = snack_profit + ticket_profit
summary_data.append(total_profit)

# Set up columns to be printed
pandas.set_option('display.max_columns', None)

# Display numbers to 2 dp
pandas.set_option('precision', 2)

# ask user if they want to see all columns
print_all = input("Print all columns? (y) for yes ")

# if yes print all columns
if print_all == "y":
    print()
    print(movie_frame)

# if no only print 'ticket', 'subtotal'
# 'surcharge' and 'Total'
else:
    print()
    print(movie_frame[['Ticket', 'Snacks',
                       'Sub Total', 'Surcharge', 'Total']])


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
