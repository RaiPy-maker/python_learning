menu = {
    "popcorn": 2.5,
    "soda": 3,
    "chips": 2.5,
    "pizza": 5,
    "chocolade": 3.5
}
cart = []
total = 0

print("---------------- MENU -----------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------- MENU -----------------\n")

while True:
    food = input("What do you want to add into the cart? (q to continue): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not in menu, try again.")

for item in cart:
    total += menu.get(item)
    print(item, end=" ")

print(f"\nTotal cost: ${total:.2f}")
