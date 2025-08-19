# creating  a discount function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price
    
# Ask the user for input 

price = float(input("Enter the original price: "))
discount_percent = float(input("enter the discount percentage: "))

# Calculate the discounted price
final_price = calculate_discount(price, discount_percent)

# Display the final price
print("The final price after disciunt:", final_price)