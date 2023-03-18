# Question 1
# I am building some very high quality chairs and need exactly four nails for each chair. I've written a
# program to calculate how many nails I need to buy to build these chairs.

# chairs = '15'
# nails = 4
# total_nails = chairs * nails
# message = 'I need to buy {} nails'.format(total_nails)
# print('You need to buy {} nails'.format(message))

# When I run the program it tells me that I need to buy 15151515 nails. This seems like a lot of nails. Is
# my program calculating the total number of nails correctly? What is the problem? How do I fix it?

# My solution to Question 1
# The problem is that the variable chairs was a string, instead of a number. The print statement was also wrong.
chairs = 15
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print(message)

# Question 2
# I'm trying to run this program, but I get an error. What is the error telling me is wrong? How do I fix
# the program?

# my_name = Penelope
# my_age = 29
# message = 'My name is {} and I am {} years old'.format(my_name, my_age)
# print(message)

# My solution to Question 2
# The variable my_name needs to be a string. Otherwise, it assumes that Penelope is the name of another variable.
my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

# Question 3
# I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can
# make. Write a program to calculate this.
# Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be
# able to easily change these values if I want. The output should say something like "You can make 9
# omelettes with 6 boxes of eggs".

# My solution to Question 3
num_boxes = 6
num_eggs  = num_boxes * 6
num_omelettes = int(num_eggs/4)
print('You can make {} omelettes with {} boxes of eggs'.format(num_omelettes, num_boxes))
