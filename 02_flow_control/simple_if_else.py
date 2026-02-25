# ==============================================================================
# SCRIPT: simpe_if_else.py
# PURPOSE: Demonstrating simple if-else statements control flow
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================

# We are going to assume a sign-up form and check if the user's age is valid

# User input for age
age = int(input("Please enter your age: "))

# Control flow logic
if (age < 0 or age > 75):                               # checks for min and max valid age
    print("Please enter a valid age")
elif age < 18:                                          # checks for min age to sign up
    print("You must be 18 years or older to sign-up")
else:                                                   # When a proper  age is entered, they are allowed to sign up
    print("Welcome Onboard!")
