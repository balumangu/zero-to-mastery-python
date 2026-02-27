# ==============================================================================
# SCRIPT: lists.py
# PURPOSE: Demonstrating working of lists
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================

# Lists - They are ordered. Duplicates allowed. They are mutable, meaning things can be added/deleted.

fruits = ["apple", "banana", "custard apple", "mango", "pineapple"]
veggies = ["potato", "onion", "carrot", "beans"]

# append
fruits.append("orange") # Adds orange to the end

# extend
fruits.extend(veggies) # Merges veggies into fruits

# insert
fruits.insert(2, "papaya") # Adds papaya at index 2

# pop
item = fruits.pop(1) # Removes and returns item at index 1 ("banana")

# remove
fruits.remove("mango") # Removes the first "mango" it finds

# index
pos = fruits.index("apple") # Returns 0

# count
qty = fruits.count("apple") # Returns 1

# sort
fruits.sort() # Sorts fruits alphabetically

# reverse
fruits.reverse() # Reverses the current order

# copy
fruits_copy = fruits.copy() # Creates a separate copy of the list

# clear
fruits.clear() # Removes everything; Result: []