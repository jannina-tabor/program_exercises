# Pseudocode 

# Create a text file that contains 20 integers named "numbers.txt"
# Create a line of code that reads numbers from the text file"
# Convert the strings from the number.txt into integers"
# Separate the odd and even numbers from the file
# Create a 'Write to a File' code for the even numbers
# Create a 'Write to File' code for the odd numbers
# Test the program created

#Read numbers from number.txt
with open('numbers.txt', 'r') as file:
    numbers = file.readlines()

# Convert the strings into integers
numbers = [int(num.strip()) for num in numbers]

print (numbers)