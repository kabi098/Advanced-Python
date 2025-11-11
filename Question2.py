# List of employee work hours in a week
work_hours = [35, 40, 45, 50, 38, 60, 42]

# Filter out employees who worked less than 40 hours
eligible_employees = list(filter(lambda h: h >= 40, work_hours))

# Convert remaining hours to overtime hours (hours - 40)
overtime_hours = list(map(lambda h: h - 40, eligible_employees))

# Display results
print("Original Work Hours:", work_hours)
print("Employees with >= 40 hours:", eligible_employees)
print("Overtime Hours:", overtime_hours)
