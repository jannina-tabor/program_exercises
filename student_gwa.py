# Psuedocode

# Create a text file containing the name of 20 students with their respective GWA
# Create a read function for the text file
# Initialize the variables: GWA set to zero and Student to empty string ""
# Splitting the line into name and GWA 
# Creating an if function to determine who has the highest GWA
# Creating an output function to determine if the program is working

# Read the text file containing the names and their GWAs
with open('students_and_gwa.txt','r') as file:
    student_data = file.readlines()

# Initialize the variables
highest_gwa = 0         # 0 as the starting point of the GWA
highest_gwa_of_student = ""     

# Split and Strip the name and GWA from the .txt file
for data in student_data: 
    name = data.strip().split('- GWA: ')
    gwa = float(gwa)