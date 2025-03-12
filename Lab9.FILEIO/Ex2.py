import csv

# File path - update this to match your actual CSV file location
csv_filename = "my_custom_spreadsheet.csv"

# List to store salary data
salaries = []

# Read the CSV salary spreadsheet and getting the salaries as a list
with open(csv_filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader) 
    print(header)
    salary_index = header.index("Annual Salary")
    
    for row_data in reader:
        salaries.append(float(row_data[salary_index]))

# computing the salary statistics
average_salary = sum(salaries) / len(salaries) if salaries else 0
max_salary = max(salaries) if salaries else 0
min_salary = min(salaries) if salaries else 0

# Print results
print(f"Average Salary: ${average_salary:.2f}")
print(f"Maximum Salary: ${max_salary:.2f}")
print(f"Minimum Salary: ${min_salary:.2f}")


