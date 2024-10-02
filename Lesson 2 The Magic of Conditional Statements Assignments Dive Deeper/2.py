# Task 1: Identify the Greatest Write a Python program that asks
#  the user to enter three numbers. Your code should then identify and print out the largest number among the three.
# Ask the user to enter three numbers and convert them to integers
num1 = int(input("Please enter the 1st number: "))
num2 = int(input("Please enter the 2nd number: "))
num3 = int(input("Please enter the 3rd number: "))

# Identify the largest number using the max() function
largest_number = max(num1, num2, num3)
# Added this lowest number line for task 2
lowest_number = min(num1, num2, num3)
# Print the result
print(f"The largest number is: {largest_number}")

# Task 2: Identify the Smallest Improve upon your code from Task 1 
# to also determine the smallest number among the three and print it out.

print(f"The lowest number is: {lowest_number}")