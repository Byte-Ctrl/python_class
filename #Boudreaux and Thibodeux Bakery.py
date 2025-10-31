#Boudreaux and Thibodeux Bakery
 # A small program to take customer orders and calculate totals

#menu and pricing
items = ["Muffin", "King Cake Slice", "Croissant", "Scone"]
prices = [5.95, 4.95, 3.95, 3.75]
tax_rate = 0.0945

#this is where i got to when the timer timed out due to it hitting 12pm 
#this won't count- 
# Display menu
print("Boudreaux & Thibodeaux's Bakery")
print("------------------------------------")
for i in range(len(items)):
    print(f"{i+1}. {items[i]}: ${prices[i]:.2f}")
print("------------------------------------")


# Initialize order and subtotal
subtotal = 0
order_counts = [0] * len(items)  # Tracks quantity ordered for each item

# Order loop
while True:
    choice = input("What would you like to order? Type the number of the menu item or DONE when order is complete: ")

    if choice.upper() == "DONE":
        break

    # Validate input
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(items):
        print("I'm sorry, that is not an appropriate response.\n")
        continue

    index = int(choice) - 1
    quantity_input = input(f"How many of that item would you like to order? ")
    
    # Validate quantity
    if not quantity_input.isdigit() or int(quantity_input) <= 0:
        print("Please enter a valid quantity.\n")
        continue

    quantity = int(quantity_input)
    order_counts[index] += quantity
    print(f"You have ordered {quantity} {items[index].lower()}(s) for ${prices[index]:.2f} each\n")

# Calculate subtotal
for i in range(len(items)):
    subtotal += order_counts[i] * prices[i]

# Calculate tax and total
tax = subtotal * tax_rate
total = subtotal + tax

# Display total
print("------------------------")
print(f"Your total is ${total:.2f}")
