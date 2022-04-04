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


# holds instructions
def instructions(options):
    show_help = "Invalid choice"
    while show_help == "Invalid choice":
        help = input("Would you like to read the instructions? ").lower()
        show_help = string_check(help, options)

    if show_help == "Yes":
        print()
        print("**** Mega Movie Fundraiser Instructions ****")
        print()
        print("- Firstly you will be asked to enter a name. \n"
              "- Next you will be asked to enter the age of the person (this must be between 12 and 130). \n"
              "- You can then enter the snacks that this person wants. Here is the list of available snacks: \n"
              "- Popcorn, M&Ms, PitaChips, Water and Orange Juice (Note: You can enter the first letter of each snack) \n"
              "- Once you have ordered your snacks type 'xxx' to continue \n"
              "- You will then have to enter your payment method. The two options are cash or credit"
              " (Note: There is a surcharge applied when using the credit method) \n"
              "- Then the loop restarts at 'name'. Once you have entered everyone type 'xxx' to continue \n"
              "- The program will then print a ticket, snack and profit summary.")

    return ""


# Main routine
# valid lists
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# Ask if instructions are needed
instructions(yes_no)
print()
print("Program Launches...")