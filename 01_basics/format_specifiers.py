# ==============================================================================
# SCRIPT: format_specifiers.py
# PURPOSE: Demonstrating format specifiers
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================

# Format specifiers are used to format the output

items = ["Bread", "Milk", "Eggs"]
price = [20, 60, 10]
quantity = [10, 10, 20]

bread_cost = price[0] * quantity[0]
milk_cost = price[1] * quantity[1]
eggs_cost = price[2] * quantity[2]
total = bread_cost + milk_cost + eggs_cost

print("Your shopping details:")
print(f"{items[0]} cost you ${bread_cost:,.1f}\n{items[1]} cost you ${milk_cost:,.1f}\n{items[2]} cost you ${eggs_cost:,.1f}")
print(f"Shopping total is ${total:,.1f}")