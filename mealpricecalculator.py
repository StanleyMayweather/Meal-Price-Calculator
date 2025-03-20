# Coding begins:

# Ask for User Input
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
number_children = int(input("How many children are there? "))
number_adults = int(input("How many adults are there? "))

# Calculate the subtotal
subtotal = (child_meal_price * number_children) + (adult_meal_price * number_adults)

print("-----------------------------------------")

# Display the subtotal
print(f"Subtotal: ${subtotal:.2f}")

print("-----------------------------------------")

# Ask the user for the sales tax rate
sales_tax_rate = float(input("What is the sales tax rate? "))

# Calculate the sales tax
sales_tax = (subtotal * sales_tax_rate) / 100

# Display the sales tax
print(f"Sales Tax: ${sales_tax:.2f}")

# Calculate the total price of the meal
total_price = subtotal + sales_tax

print("-----------------------------------------")
# Step 8: Display the total price
print(f"Total: ${total_price:.2f}")
print("-----------------------------------------")

# Ask the user for the payment amount
payment_amount = float(input("What is the payment amount? "))

# Step 10: Calculate the change
change = payment_amount - total_price

print("-----------------------------------------")
# Display the change
print(f"Change: ${change:.2f}")
print("-----------------------------------------")
