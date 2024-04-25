# Pseudocode 

# Create a text file that contains 20 integers named "numbers.txt"
# Create a line of code that reads numbers from the text file"
# Convert the strings from the number.txt into integers"
# Separate the odd and even numbers from the file
# Print the Odd and Even numbers to see if the code worked
# Create a 'Write to a File' code for the even numbers
# Create a 'Write to File' code for the odd numbers
# Test the program created

#Read numbers from number.txt
with open('numbers.txt', 'r') as file:
    numbers = file.readlines()

# Convert the strings into integers
numbers = [int(num.strip()) for num in numbers]

# Separation of odd and even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_number = [num for num in numbers if num % 2 != 0]

# Print the Even numbers
print ("Even numbers: ")
for num in even_numbers:
    print (num)

# Print the Odd numbers
print ("\nOdd numbers: ")
for num in odd_number:
    print (num)

# Write even numbers to even.txt
with open('even.txt', 'w') as even_file:
    for num in even_numbers:
        even_file.write(str(num) + '\n')

# Write odd numbers to odd.txt
with open ('odd.txt', 'w') as odd_file:
    for num in odd_number:
        odd_file.write(str(num) + '\n')