# Lovely Loveseat! Furniture Shop

#Catalog

# Item N° 1 = The Homonymous Lovely Loveseat
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00
# Item N° 2 = The Stylish Settee.
stylish_setee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_setee_price = 180.50
# Item N° 3 = The Luxurious Lamp
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

# Sales tax calculation
sales_tax = 0.08

# Oop! It seems we have our first customer! Let's deal with that!
customer_one_total = 0
customer_one_itemization = ""
customer_one_total = lovely_loveseat_price
customer_one_itemization = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
customer_one_total += luxurious_lamp_price
customer_one_itemization += ""
customer_one_itemization += " Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# Let's print their receipt!
print("Receipt")
print("")  # To space code.
print("Customer One Items:")
print(customer_one_itemization)
print("") #To space code.
print("Customer One Total:")
print(customer_one_total)
print("Thanks for purchasing with Lovely Loveseat!")
