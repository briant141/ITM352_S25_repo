# Define a function to check if purchases are within budget
def check_budget(recent_purchases, budget):
    total_spent = sum(recent_purchases)  # Calculate total spent

    if total_spent > budget:
        return "This purchase is over budget"
    else:
        return "This purchase is within budget"

# Example usage
recent_purchases = [36.13, 23.87, 18.11, 22.93, 11.62]
budget = 200

# Call the function and print the result
print(check_budget(recent_purchases, budget))