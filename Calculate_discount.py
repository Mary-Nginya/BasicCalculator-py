def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
# Part two of the code task. Get input from the user and apply the discount if applicable.

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if final_price != price:
    print(f"Discount was applied. The final price is: {final_price:.2f}")
else:
    print(f"No discount was applied below 20%. The price remains: {price:.2f}")
