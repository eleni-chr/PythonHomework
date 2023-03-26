# Question 1:
# Explain what this program does:

# for number in range(100):
#     output = 'o' * number
#     print(output)

# My answer to Question 1:

# It prints 99 lines of the character 'o', where each line contains one more character than the previous line.
# The first iteration of the loop does not print anything because number is equal to zero. The last iteration prints 99
# characters.

# Question 2: Your boss really likes calculating VAT on their purchases. It is their favourite hobby. They've written
# this code to calculate VAT and need your help to fix it.

# def calculate_vat(amount):
#     amount * 1.2

# total = calculate_vat(100)
# print(total)

# When your boss runs the program they get the following output:
# None
# Your boss expects the program to output the value 120. What is wrong? How do you fix it?

# My anser to Question 2:

# The return word was missing from the return statement. The code should be like this:

def calculate_vat(amount):
    return amount * 1.2

total = calculate_vat(100)
print(total)