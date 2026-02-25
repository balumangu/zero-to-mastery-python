# ==============================================================================
# SCRIPT: string_functions.py
# PURPOSE: Demonstrating string functions for cleaning data
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================

# String functions always return string only and are not mutable

text = "Python for DevOps"
result = text.find("for")
print(result)               # Returns index of first occurance of sub-string in find function from left of main string

result = text.rfind("for")
print(result)               # Returns index of first occurance of sub-string in find function from right of main string

# Text with extra spaces
text = " Python for DevOps "
result = text.strip()
print(result)               # Strip trims extra spaces before and after text

result = text.rstrip()
print(result)               # Rstrip trims extra spaces from right side of text

result = text.lstrip()
print(result)               # Lstrip trims extra spaces from left side of text

text = "Python for DevOps"
result = text.replace("for", "For")
print(result)               # Replaces old text with new text

text = "python for devops"
result = text.title()
print(result)               # Capitalize first letter of all words

text = "python for devops"
result = text.capitalize()
print(result)               # Capitalize first letter of first word

csv_line = "server-01,10.0.0.1,healthy"
data_list = csv_line.split(",")
print(data_list)            # ['server-01', '10.0.0.1', 'healthy']

path_parts = ["etc", "nginx", "conf.d"]
full_path = "/".join(path_parts)
print(full_path)            # Output: 'etc/nginx/conf.d'

phone_number = "1234567890"
result = phone_number.isdigit()
print(result)               # Returns true if text is all numbers/digits having no alphabets of special chars

text = "Python"
result = text.isalpha()
print(result)               # Returns true if text is all alphabets having no numeric or special character inputs