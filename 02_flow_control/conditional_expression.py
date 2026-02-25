# ==============================================================================
# SCRIPT: conditional_expression.py
# PURPOSE: Demonstrating conditional statement control flow
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================

# Syntax --> var = X if condtion else Y

role = "admin" # role = "developer" # role = "guest"
access_level = "Full access" if role == "admin" else "Limited access"
print(access_level)

# Above program checks if "role" is admin, and then give result based on validity of the condition.