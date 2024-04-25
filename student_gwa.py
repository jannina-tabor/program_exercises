# Psuedocode

# Create a text file containing the name of 20 students with their respective GWA
# Create a read function for the text file
# Initialize the variables: GWA set to zero and Student to empty string ""
# Strip and split the line into name and GWA 
# Creating an if function to determine who has the highest GWA
# Creating an output function to determine if the program is working

# Read the text file containing the names and their GWAs
with open('students_and_gwa.txt','r') as file:
    student_data = file.readlines()

# Initialize the variables
highest_gwa = 0         # 0 as the starting point of the GWA
student_highest_gwa = ""     

# Split and Strip the name and GWA from the .txt file
for data in student_data: 
    name , gwa = data.strip().split('- GWA: ')
    gwa = float(gwa)

# Find who has the highest GWA
    if gwa > highest_gwa:
        highest_gwa = gwa
        student_highest_gwa = name.strip()

# Output of the name of the student with the highest GWA and their respective GWA
print("Congratulations!")
print("Name: ", student_highest_gwa)
print("GWA: ", highest_gwa)