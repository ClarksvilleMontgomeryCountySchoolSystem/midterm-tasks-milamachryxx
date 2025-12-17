# TESTING must = False!!!!!!
# Testing flag - will be set by test
TESTING = False  # <-- Should be False by default
item = None
price = None
quantity = None

print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"
   Prosperity comes in threes!
========================================
ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
""")

menu ='''
Flying Carpet...............$119.99
Flying Carpet - $119.99
Phoenix Feather - $14.99
Time Turner - $84.99
Enchanted Sword - $65.99
Potion of Luck - $11.99
Crystal Ball - $39.99
'''
print(menu)

# Shopkeeper's rule: All purchases must be at least 3 items for good luck!
# (Don't worry - the shopkeeper checks every order himself)

def get_purchase_info(): # Convert input when necessary
    # TODO Use input to collect item name and store into - item
    item = input("item")
    # TODO Use input to collect item price and store into - price
    price = float(input("price"))
    # TODO Use input to collect item quantity and store into - quantity
    quantity = int(input("quantity"))
    price = float(price)
    quantity = int(quantity)

    return item, price, quantity

# Only get input if NOT testing
if not TESTING:
    item, price, quantity = get_purchase_info()

# Calculate using the input values (NOT hardcoded!)
# TODO Calculate subtotal
subtotal = price * quantity
tax_rate = 0.095 #This is slightly different from the review. The tax multiplier is stored into a variable.
# TODO Calculate tax
tax = subtotal * tax_rate
# TODO Calculate total
total = subtotal + tax
total = round(total,2)
# TODO Round total to 2 decimal places

# Print statements
print("--------------------------")
print(f"{item} x{quantity} @ ${price}")
print("--------------------------")
# TODO Print subtotal
print(f"Subtotal: ${subtotal}")
# TODO Print tax# TODO Print total.
print(f"Tax: ${tax}")
print(f"Total: ${total}")
print("\nThank you for shopping at\nThe Peculiar Emporium!")
