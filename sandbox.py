# ask user if they want to see all columns
print_all = input("Print all columns? (y) for yes ")

# if yes print all columns
if print_all == "y":
    print(movie_frame)

# if no only print 'ticket', 'subtotal'
# 'surcharge' and 'Total'
else:
    print(movie_frame[['Ticket', 'Sub Total',
                       'Surcharge', 'Total']])

