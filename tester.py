# Declare variables 'age' and 'budget' with appropriate values
age = 2
budget = 500  # Update this value as needed

# Write an 'if' statement to determine if the traveler is over 18
if age > 18:
    # Inside the 'if' block, write another 'if' statement to check if the budget is more than 1000
    if budget > 1000:
        print("You are eligible for the international travel package.")
    else:
        print("You are eligible for the local travel package.")
else:
    # Else block for travelers 18 or below
    print("You are eligible for the children's travel package.")