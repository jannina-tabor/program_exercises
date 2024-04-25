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
    lines = file.readlines()

# Conversion of strings to integers
numbers = [int(line.strip()) for line in lines]

# Separation of odd and even numbers 
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the odd and even numbers
print("Even numbers:", even_numbers)
print("Odd numbers: ", odd_numbers)

# Calculations of Even squares and Odd cubes
even_squares = [num ** 2 for num in even_numbers]
odd_cubes = [num ** 3 for num in odd_numbers]

# Write even squares to a new text file as 'double.txt'
#with open ('double.txt', 'w') as even_file:
    #for square in even_squares:
        #even_file.write(str(square) + '\n')

# Write odd cubes to a new text file as 'triple.txt'
#with open ('triple.txt' , 'w') as odd_file:
    #for cube in odd_cubes:
        #odd_file.write(str(cube) + '\n')

# Make the user know that the file is created
#print ("The text files of odd cubes and even squares named as 'double.txt' and 'triple.txt' have been successfully created.")
