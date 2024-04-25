# Pseudocode

# Write a write function code for the 'mylife.txt' 
# Create a while function 
# Prompt the user to enter a line of text
# Write the user input to the file
# Prompt the user if there are more lines to enter by answering yes or no
# If the user said no, close the file
# Exit the loop of the while function
# Create an print function to tell the user the file is closed

# Write a text file by urging the users to input a line of text
with open('mylife.txt', 'w') as file:
    while True:
        user_line = input("Please enter a line/phrase: ")
        file.write(user_line + '\n')
        print ("A line is added to your text file 'mylife.txt'")
        need_more = input("Are there more lines? (y/n): ")
        if need_more.lower() != 'y': 
            file.close()
            