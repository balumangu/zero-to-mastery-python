# ==============================================================================
# SCRIPT: sets.py
# PURPOSE: Demonstrating working of sets
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================

# Sets are unordered and unique. 
# They do not use indices (positions), so methods involving "index" or "sort" do not exist.

fruits = {"apple", "banana", "custard apple", "mango", "pineapple"}
veggies = {"potato", "onion", "carrot", "beans"}

# add (Set version of append)
fruits.add("orange") 

# update (Set version of extend)
fruits.update(veggies) 

# pop
item = fruits.pop() # Removes and returns a RANDOM item (no index allowed)

# remove
fruits.remove("apple") # Removes "apple" from the set

# copy
fruits_copy = fruits.copy() # Creates a separate copy of the set

# clear
fruits.clear() # Removes everything; Result: set()

# insert, index, count, sort, reverse
# NONE of these exist for sets because there is no fixed order.