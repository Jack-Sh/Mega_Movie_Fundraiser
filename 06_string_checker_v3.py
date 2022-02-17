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
    if __name__ == '__main__':
        while desired_snack != "xxx":

            # ask for desired snack and put in lowercase
            desired_snack = input("Snack: ").lower()

            if desired_snack == "xxx":
                break

            # check if snack is valid
            snack_choice = string_check(desired_snack, valid_snacks)
            print("Snack Choice:", snack_choice)

            # add snack to list..

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
