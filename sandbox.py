import random


def random_number():
    n = random.randint(1,100)
    print(n)

rn = ""
while rn != "xxx":

    rn = input("Random Number? ")
    print(rn)
    if rn == "":
        random_number()
    else:
        continue

    if rn == "xxx":
        break
