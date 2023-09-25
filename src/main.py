import pandas as pd

# Path to the .xlsx file .

xlsx_file = "data\Test Files.xlsx"

df = pd.read_excel(xlsx_file)

df.info()

# Load the student data from the Excel file
excel_file = 'your_test_file.xlsx'  # Replace with the actual file name
df = pd.read_excel(xlsx_file)

# Function to generate email addresses
def generate_email(name):
    # Remove special characters and split the name
    clean_name = ''.join(e for e in name if e.isalnum() or e.isspace())
    name_parts = clean_name.split()

    # Extract first and last name (or use what's available)
    if len(name_parts) >= 2:
        first_name = name_parts[0][0]
        last_name = name_parts[-1]
    else:
        first_name = name_parts[0]
        last_name = ""

    # Generate a unique email address
    email = f"{first_name.lower()}{last_name.lower()}@gmail.com"

    return email

# Create a dictionary to store email addresses
email_addresses = {}

# Generate email addresses for each student
for index, row in df.iterrows():
    student_name = row['Student Name']
    email = generate_email(student_name)

    # Ensure uniqueness
    while email in email_addresses.values():
        email = generate_email(student_name)

    email_addresses[student_name] = email

# Print the generated email addresses
for student_name, email in email_addresses.items():
    print(f"Student Name: {student_name} - Email Address: {email}")

 
