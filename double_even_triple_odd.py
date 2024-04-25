# Pseudocode

# Create a text file consisting 20 random integers
# Create a read function for the text file
# Convert the strings to integers from the text file
# Separate the odd and even numbers
# Calculate the square of the even numbers and the cube of the odd numbers
# Create a write function for the even squares naming 'double.txt'
# Create a write function for the odd cubes naming 'triple.txt'
# Make the user know that the text files have been created

# Read the source file from 'integers.txt'
with open('integers.txt', 'r') as file:
    numbers = file.readlines