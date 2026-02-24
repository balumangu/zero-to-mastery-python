# ==============================================================================
# SCRIPT: basic_calculator.py
# PURPOSE: Demonstrating Arithmetic Operators and Math Functions
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================

# import math libraries for in-built functions and constants such as pi
import math

# User input and casting
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmatic operators
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1/num2
remainder = num1 % num2

print(f"Sum of {num1} and {num2} is {sum}")
print(f"Difference of {num1} and {num2} is {difference}")
print(f"Product of {num1} and {num2} is {product}")
print(f"Quotient of {num1} and {num2} is {quotient}")
print(f"Remainder of {num1} and {num2} is {remainder}")

num3 = float(input("Enter number for math functions: "))

# Math functions
exponent = math.pow(num3, 2) # can also be written as x ** y
sqrt = math.sqrt(num3)
absolute = abs(difference)
ceil = math.ceil(num3)
floor = math.floor(num3)

print(f"Exponent of {num3} times 2 is {exponent}")
print(f"Square-root of {num3} is {sqrt}")
print(f"Absolute of difference of {num1} and {num2} is {absolute}")
print(f"Floor and ceil values s of {num3} are {floor} and {ceil}")

print("End of program")