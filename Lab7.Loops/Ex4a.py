recent_purchases = [36.13, 23.87, 18.11, 22.93, 11.62]
budget = 200
total_spent = 0
for purchase in recent_purchases:
    total_spent += purchase
if(total_spent > budget):
    print("This purhcase is over budget")
else:
    print("This purchase is within budget")
# in class