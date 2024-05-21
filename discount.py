def calculate_discount(price, discount_percent):

    original_price = int(input("Enter the original price of the Item"))
    discount_percent = int(input("Enter the discount percentage"))

    if discount_percent >= 20:
        price = original_price - ((original_price * discount_percent) / 100)
        print("Discounted Price:", price)

    else:
        print("No Discount Applied")
        print("Price = ", original_price)

calculate_discount (price=..., discount_percent=...)