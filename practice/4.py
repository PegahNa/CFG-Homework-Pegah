# I want to hire a venue for my birthday for 3 hours.The venue hire costs £200 per
# hour and a refundable 10% deposit.I've written a program to check that I can afford
# the cost, but something doesn't seem right.
# Have a look at my program and work out what I've done wrong:
# my_money = input('How much money do you have? ')
# hour = 3
# venue cost = (200*hours) + 1.1
# if my_money < venue_cost:
# print('You can afford the venue')
# else :
# print('You cannot afford the venue'

my_money = float(input("How much money do you have? "))
hours = 3
venue_cost = (200 * hours) * 1.1
if my_money >= venue_cost:
    print("You can afford the venue")
else:
    print("You cannot afford the venue")