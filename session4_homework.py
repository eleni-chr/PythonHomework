# Question 1
# I have a list of things I need to buy from my supermarket of choice.
# shopping_list = [
# "oranges",
# "cat food",
# "sponge cake",
# "long-grain rice",
# "cheese board",
# ]
# print(shopping_list[1])

# I want to know what the first thing I need to buy is. However, when I run the program it shows me a different answer
# to what I was expecting? What is the mistake? How do I fix it?

# My solution to Question 1
# Indexing starts at 0, not 1.
shopping_list = [
    "oranges",
    "cat food",
    "sponge cake",
    "long-grain rice",
    "cheese board",
]
print(shopping_list[0])
#

# Question 2
# I'm setting up my own market stall to sell chocolates. I need a basic till to check the prices of different chocolates
# that I sell. I've started the program and included the chocolates and their prices. Finish the program by asking the
# user to input an item and then output its price.
# chocolates = {
# 'white': 1.50,
# 'milk': 1.20,
# 'dark': 1.80,
# 'vegan': 2.00,
# }

# My solution to Question 2
chocolates = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}

choice = input('Select a chocolate (white/milk/dark/vegan): ')
if choice == 'white':
    print('Price: ' + str(chocolates['white']))
elif choice == 'milk':
    print('Price: ' + str(chocolates['milk']))
elif choice == 'dark':
    print('Price: ' + str(chocolates['dark']))
elif choice == 'vegan':
    print('Price: ' + str(chocolates['vegan']))

# Question 3
# Write a program that simulates a lottery. The program should have a list of seven numbers that represent a lottery
# ticket. It should then generate seven random numbers. After comparing the two sets of numbers, the program should
# output a prize based on the number of matches:
# £20 for three matching numbers
# £40 for four matching numbers
# £100 for five matching numbers
# £10000 for six matching numbers
# £1000000 for seven matching numbers

# My solution to Question 3
import random

winning_numbers = [6, 7, 25, 95, 48, 3, 68]

random_numbers = [0, 0, 0, 0, 0, 0, 0]
for x in range(7):
    random_numbers[x] = random.randint(1, 100)

print('Lottery ticket: ' + str(random_numbers))

count = 0
for number in random_numbers:
    if number in winning_numbers:
        count = count + 1

if count <= 2:
    print('Prize: £0')
elif count == 3:
    print('Prize: £20')
elif count == 4:
    print('Prize: £40')
elif count == 5:
    print('Prize: £100')
elif count == 6:
    print('Prize: £10000')
else:
    print('Prize: "1000000')

