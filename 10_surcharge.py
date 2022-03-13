

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


# Main routine

pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# loop until exit code
name = ""
while name != "xxx":
    name = input("Name: ")
    if name == "xxx":
        break

    # ask for payment method
    how_pay = "Invalid choice"
    while how_pay == "Invalid choice":
        how_pay = input("Please choose a payment method (cash or credit) ")
        how_pay = string_check(how_pay, pay_method)

    # ask for subtotal (for testing purposes)
    subtotal = float(input("Subtotal? $"))

    if how_pay == "Credit":
        surcharge = 0.05 * subtotal

    else:
        surcharge = 0

    total = subtotal + surcharge

    print("Name: {} | Subtotal: ${:.2f} | Surcharge: ${:.2f} | "
          "Total Payable: ${:.2f}".format(name, subtotal, surcharge, total))
