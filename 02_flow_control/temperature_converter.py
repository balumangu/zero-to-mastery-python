# ==============================================================================
# SCRIPT: temperature_converter.py
# PURPOSE: Demonstrating simple if-else statements control flow
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================

# We are going to take input from users and convert the temperatures

# User input
temperature = float( input( "Enter temperature: " ) )
deg = input( "Is this in Celsius or Fahrenhiet (C/F): " )

# Conversion logic
if (deg != "C" and deg != "F"):
    print( "Please enter a valid unit" )
elif deg == "C":
    temperature = ((9/5)*temperature) + 32
    deg = "F"
    print(f"The converted temperature is {round(temperature,2)} {deg}")
else:
    temperature = ((temperature - 32) * (5/9))
    deg = "C"
    print( f"The converted temperature is {round(temperature,2)} {deg} " ) 

print ( "End of program" )