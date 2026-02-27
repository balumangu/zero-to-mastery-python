# ==============================================================================
# SCRIPT: simple_for_loop.py
# PURPOSE: Demonstrating simple for loop control flow
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================

# We are printing a timer that does countdown

import time

timer = int(input("Enter time to countdown in seconds: "))

for counter in range(timer, 0, -1):
    seconds = counter % 60
    minutes = int(counter / 60) % 60
    hours = int(counter / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP!!!!")