# ==============================================================================
# SCRIPT: tuples.py
# PURPOSE: Demonstrating working of tuples
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================

# Tuples are immutable. You cannot add, remove, or reorder items.

fruits = ("apple", "banana", "custard apple", "mango", "pineapple")

# index
pos = fruits.index("banana") # Returns 1

# count
qty = fruits.count("apple") # Returns 1

# append, extend, insert, pop, remove, clear, sort, reverse, copy
# NONE of these exist for tuples. 
# They will all raise an AttributeError.