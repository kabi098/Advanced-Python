# Dictionary of employee names and their salaries
employees = {
    "Ram": 55000,
    "Sita": 60000,
    "Hari": 75000,
    "Rita": 45000,
    "Arpita": 90000
}

# Filter out employees with salaries less than $60,000
filtered_employees = dict(filter(lambda item: item[1] >= 60000, employees.items()))

# Apply a 5% raise to the remaining employees
updated_employees = dict(map(lambda item: (item[0], item[1] * 1.05), filtered_employees.items()))

# Display results
print("Original Employee Salaries:")
print(employees)

print("\nFiltered Employees (Salary >= $60,000):")
print(filtered_employees)

print("\nUpdated Employees after 5% Raise:")
print(updated_employees)
