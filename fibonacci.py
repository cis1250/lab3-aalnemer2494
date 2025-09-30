#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

# Fibonacci Sequence Program

# ask the user how many terms they want
num_terms = int(input("Enter how many terms of the Fibonacci sequence you want: "))

# check that the number is positive
while num_terms <= 0:
    print("Please enter a positive integer.")
    num_terms = int(input("Enter how many terms of the Fibonacci sequence you want: "))

# first two numbers of the sequence
first = 0
second = 1

print("Fibonacci sequence:")

# print the sequence
for i in range(num_terms):
    print(first)
    next_num = first + second
    first = second
    second = next_num
