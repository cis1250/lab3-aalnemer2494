#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.



num_terms = int(input("Enter how many terms of the Fibonacci sequence you want: "))

if num_terms <= 0:
    print("Error: please run the program again and enter a positive integer.")
else:
    first = 0
    second = 1

    print("Fibonacci sequence:")

    for i in range(num_terms):
        print(first)
        next_num = first + second
        first = second
        second = next_num
