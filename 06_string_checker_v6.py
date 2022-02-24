import re


# functions


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


yes_no = ["yes", "y"], ["no","n"]

# loops until user enters yes or no
check_snack = "Invalid choice"
while check_snack == "Invalid choice":

    # asks user if they want snacks
    want_snack = input("Do you want to order snacks? ").lower()
    # checks whether answer is within the list
    check_snack = string_check(want_snack, yes_no)
    if check_snack == "Invalid choice":
        print("Please enter yes or no")

if check_snack == "Yes":
    get_order = get_snack()

else:
    get_order = []

# show snack orders
print()
if len(get_order) == 0:
    print("Snacks Ordered: None")

else:
    print("Snacks Ordered: ")
    print(get_order)
