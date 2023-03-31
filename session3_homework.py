# Question 1
# Create a program that tells you whether or not you need an umbrella when you leave the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'

# My answer to question 1
raining = input("Is it raining? y/n ")
if raining == 'y':
    print('Take an umbrella')
elif raining == 'n':
    print("You don't need an umbrella")

# Question 2
# I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. I've written a program to
# check that I can afford the cost, but something doesn't seem right.
# Have a look at my program and work out what I've done wrong.

# my_money = input('How much money do you have? ')
# boat_cost = 20 + 5
# if my_money < boat_cost:
#     print('You can afford the boat hire')
# else:
#     print('You cannot afford the board hire')

# My answer to question 2
# The my_money variable is a string and so it cannot be compared to the boat_cost variable which is an integer.
# Also, the operator should be > not <.

my_money = int(input('How much money do you have? '))
boat_cost = 20 + 5
if my_money > boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the boat hire')

# Question 3
# Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to quickly categorise
# books by the century and decade that they were written. Write a program that takes a year (e.g. 1872) and outputs the
# century and decade (e.g. "Nineteenth Century, Seventies")

# My answer to question 3
date = input('What is the year? ')
if int(date) >= 1800 and int(date) < 1850:
    century = "Eighteenth Century, "
elif int(date) >= 1850 and int(date) < 1950:
    century = "Nineteenth Century, "

third_digit = int(date[2])
if third_digit == 0:
    decade = "First decade"
elif third_digit == 1:
    decade = "Teens"
elif third_digit == 2:
    decade = "Twenties"
elif third_digit == 3:
    decade = "Thirties"
elif third_digit == 4:
    decade = "Forties"
elif third_digit == 5:
    decade = "Fifties"
elif third_digit == 6:
    decade = "Sixties"
elif third_digit == 7:
    decade = "Seventies"
elif third_digit == 8:
    decade = "Eighties"
else:
    decade = "Nineties"

output = century + decade
print(output)