# ==============================================================================
# SCRIPT: concession_stand.py
# PURPOSE: Demonstrating working of dictionaries in Python
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================

# This program is to use dictionaries and calculate cart total for a concession stand.

menu = {
    "nachos": 200.00,
    "popcorn": 180.00,
    "sandwich": 180.00,
    "pizza": 240.00,
    "burger": 220.00,
    "shawarma": 180.00,
    "french fries": 120.00,
    "sweet corn": 90.00,
    "soft drink": 70.00,
    "water bottle": 60.00
}

# Logic to add items to cart and calculate total
cart = {}

print("Welcome to the Concession Stand! Here's our menu:\n")
for item in menu:
    print(f"{item.title():15}: {menu[item]:.2f}")

while True:
    choice = input("\nEnter the item you want to add to your cart (or type 'done' to finish): ").lower()
    
    if choice == 'done':
        break
    elif choice in menu:
        quantity = int(input(f"How many {choice} would you like to add? "))
        if choice in cart:
            cart[choice] += quantity
        else:
            cart[choice] = quantity
        print(f"Added {quantity} {choice}(s) to your cart.")
    else:
        print("Sorry, we don't have that item. Please choose from the menu.")

# Calculate total

total = sum(menu[item] * quantity for item, quantity in cart.items())
print("\nYour cart:")
for item, quantity in cart.items():
    print(f"{item.title():15}: {quantity} x {menu[item]:.2f} = {quantity * menu[item]:.2f}")
print(f"\nTotal: {total:.2f}")