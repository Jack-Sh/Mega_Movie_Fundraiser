# start of loop

# initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # print number of tickets left
    print("You have {} seats left".format(MAX_TICKETS - count))

    # get name, if the name is not 'xxx' add one to the counter
    name = input("Name: ")
    if name != "xxx":
        count += 1
    print()

# If all tickets are sold print statement
if count == MAX_TICKETS:
    print("You have sold all the available tickets!")

# If not all tickets are sold, print how many were sold and how many were left
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available".format(count, MAX_TICKETS - count))