# Functions go here


def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        
        else:
            print("Sorry - this can't be blank")

# Main routine

# Ask user for name
name = not_blank("Name: ")
