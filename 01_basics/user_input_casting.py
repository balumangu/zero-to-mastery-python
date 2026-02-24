# ==============================================================================
# SCRIPT: user_input_casting.py
# PURPOSE: Handling user input and converting data types (Casting)
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================


# Import pi for calculation
from math import pi

# User input is always read as a string
print("We are calculating perimeter of a rectangle and a circle.")

raw_length = input("Please enter integer value for length: ")
raw_height = input("Please enter integer value for height: ")
raw_radius = input("Please enter value for radius: ")

length = int(raw_length)
height = int(raw_height)
radius = float(raw_radius)

print(f"The circumference of your rectangle is {2*(length+height)} and circle is {2*pi*radius}")
