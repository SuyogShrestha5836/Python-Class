Name=input("Enter your name: ")
menu = {
        "toppings": {
        "Pepperoni": 50,
        "Mushrooms": 20,
        "Onions": 10,
        "Sausage": 30,
        "Bacon": 40,
        "Extra cheese": 20
    },
        "sizes": {
        "Small": 100,
        "Medium": 200,
        "Large": 300
    }
}

print("Welcome to the Pizza Shop!")

# Initialize total price
total_price = 0
order = True

while order:
    print("\nMenu:")
    print("Toppings:")
    for topping, price in menu["toppings"].items():
        print(f"- {topping}: Rs.{price:}")

    print("\nSizes:")
    for size, price in menu["sizes"].items():
        print(f"- {size.capitalize()}: Rs.{price:}")

    # Ask for user input
    selected_toppings = input("\nSelect your toppings (It should be comma-separated): ").split(",")
    selected_size = input("Select the size (Small, Medium, or Large): ")

    # Calculate the total price
    for topping in selected_toppings:
        topping = topping.strip().lower()
        if topping in menu["toppings"]:
            total_price += menu["toppings"][topping]
 
    if selected_size in menu["sizes"]:
        total_price += menu["sizes"][selected_size]
    else:
        print("Invalid size selected!")

    # Display the total prices
    print(f"\nTotal price: Rs.{total_price:}")

    # Ask if the user wants to continue ordering
    choice = input("\nDo you want to continue ordering? (yes/no): ")
    if choice.lower() != "yes":
        order = False

print("\nThank you for your order! Enjoy your pizza!")