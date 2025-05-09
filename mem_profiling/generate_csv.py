import csv
import random
import string

# Function to generate random text
def random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Define the CSV file name
file_name = '10mb_file.csv'

# Define the number of rows and columns
num_rows = 100000  # Adjust this to reach ~10MB
num_columns = 10

# Generate the CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    header = [f'Column_{i+1}' for i in range(num_columns)]
    writer.writerow(header)
    
    # Write the rows
    for _ in range(num_rows):
        row = [random_string(20) for _ in range(num_columns)]  # 20-character random strings
        writer.writerow(row)

print(f"Generated {file_name} with size ~10MB")
