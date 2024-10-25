# Shopping cart

cart = []
price = []
total = 0

while True:
    add_item = input("Please enter what you want to input into cart: (press q to quit): ").lower()
    if add_item == 'q':
        break
    else:
        cart.append(add_item)   

while True:
    for prices in cart:
        add_price = float(input(f"Please enter the price of {prices}: $"))
        price.append(add_price)
    break


for food in cart:
    print(food, end=" ")

for pricess in price:
    total += pricess

print("\n-----------CART-----------/n")
print(f"Your total is ${total:.2f}")
print("-----------CART-----------/n")

