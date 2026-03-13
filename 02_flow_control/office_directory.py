# ==============================================================================
# SCRIPT: office_directory.py
# PURPOSE: Demonstrating working of dictionaries in Python
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================

# This is a program that simulates an office directory.
# It uses a dictionary to store employee names as keys 
# and their mobile numbers with job titles as values.

office_directory = {
    "Alice Johnson": {"mobile": "555-1234", "job_title": "Software Engineer"},
    "Bob Smith": {"mobile": "555-5678", "job_title": "Project Manager"},
    "Charlie Brown": {"mobile": "555-8765", "job_title": "Data Analyst"},
    "Diana Prince": {"mobile": "555-4321", "job_title": "UX Designer"}
}

# Get method to retrieve employee details
employee_name = "Alice Johnson"
employee_details = office_directory.get(employee_name, "Employee not found.")
print(f"Details of {employee_name}: {employee_details} \n")

# Adding a new employee to the office directory
office_directory.update({"Edward Jones": {"mobile": "555-6789", "job_title": "DevOps Engineer"}})
print(f"Added new employee: Edward Jones - {office_directory['Edward Jones']} \n")

# Updating an existing employee's job title
office_directory["Alice Johnson"]["job_title"] = "Senior Software Engineer"
print(f"Updated employee: Alice Johnson - {office_directory['Alice Johnson']} \n")

# Removing an employee from the office directory
removed_employee = office_directory.pop("Bob Smith")
print(f"Removed employee: Bob Smith - {removed_employee} \n")

# Removing last inserted employee from the office directory
last_removed_employee = office_directory.popitem()
print(f"Removed last inserted employee: {last_removed_employee}")

# Displaying the current office directory
print("\nCurrent Office Directory: \n")
for name, details in office_directory.items():
    print(f"{name}: Mobile - {details['mobile']}, Job Title - {details['job_title']}")
    print()