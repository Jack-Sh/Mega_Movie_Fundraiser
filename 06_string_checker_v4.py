import re


# functions
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


# regular expression to find if item starts with a number
number_regex = "^[1-9]"

# valid snacks holds list of all snacks
# Each item in valid snacks is a list with
# valid options for each snack <full name, letter code (a - e)
# and possible abbreviations etc>
valid_snacks = ["popcorn", "p", "corn", "a"], ["M&M's", "m&m's", "mms", "m", "b"], ["pita chips", "chips", "pc", "pita", "c"], ["water", "w", "d"]

yes_no = ["yes", "y"], ["no","n"]

# holds snack order for as single user
snack_order = []

# loops until user enters yes or no
check_snack = "Invalid choice"
while check_snack == "Invalid choice":

    # asks user if they want snacks
    want_snack = input("Do you want to order snacks? ").lower()
    # checks whether answer is within the list
    check_snack = string_check(want_snack, yes_no)

# if they say yes, ask what snacks they want and add it to our list
if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":

        # ask for desired snack and put in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break

        # if item has a number, seperate it into two (number / item)
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

        # check if snack amount is valid
        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "Invalid choice"

        # add snack and amount to list
        amount_snack = "{} {}".format(amount, snack_choice)

        # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "Invalid choice":
            snack_order.append(snack_choice)

# show snack orders
print()
if len(snack_order) == 0:
    print("Snacks Ordered: None")

else:
    print("Snacks Ordered: ")
    for item in snack_order:
        print(item)
