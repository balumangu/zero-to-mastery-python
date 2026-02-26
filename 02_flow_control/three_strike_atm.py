# ==============================================================================
# SCRIPT: three_strike_atm.py
# PURPOSE: Simulate ATM withdrawal using while loop (Refactored)
# JOURNEY: Zero to Mastery - Python for DevOps
# ==============================================================================

correct_pin = 1234
balance = 10000.00
attempts_left = 3

while attempts_left > 0:
    # 1. Ask for input at the very start of every loop iteration
    print(f"\n[Attempts remaining: {attempts_left}]")
    user_pin = int(input("Please enter your card pin: "))

    if user_pin == correct_pin:
        amount = float(input("Please enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. Remaining balance: ${balance:,.2f}")
        else:
            print("Transaction denied. Insufficient balance.")
        break  # Exit loop after trying to withdraw
    
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print("Incorrect pin. Try again.")

if attempts_left == 0:
    print("Too many incorrect attempts. Card Blocked. Please contact your branch.")