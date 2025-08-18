#Shopping Cart Validation
#Instructions:
#1. Create a variable ItemsInCart and initialize it to 0.
#2. Write a function called add_to_cart that accepts an integer parameter items_to_add.
#3. If items_to_add is less than 0, raise an exception with
# the message "Cannot add a negative number of items."
#4. If the total count of items after addition exceeds 5,
# raise an exception with the message "Cart limit exceeded."

ItemsInCart = 0
def add_to_cart(items_to_add):
    global ItemsInCart
    if items_to_add < 0:
        raise Exception ("Cannot add a negative number of items.")
    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")
    ItemsInCart += items_to_add
    print(f"{items_to_add} items added. Total in cart: {ItemsInCart}")



try:
    add_to_cart(2)
    add_to_cart(-1)
except Exception as e:
    print(e)

