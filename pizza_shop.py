def welcome():
    welcome=("Welcome to the pizza shop")
    print(welcome)
welcome()

r=input("Enter your name: ")
print(f"What would you like to order {r}?")
types_of_pizza={
    "Chicken pizza":450,
    "Pepperoni pizza":500,
    "Pork pizza":600,
    "Veg pizza":690,
    "Italian pizza":900
}

for key,value in types_of_pizza.items():
    print(key,value)
sum=0
while True:
    y=input("Enter the type of pizza: \n")
    break
sum+=types_of_pizza[y]

print(f"Which toppings do you want to add in the pizza {r}?\n")

Toppings={
          "Mushroom":350,
          "Olives":450,
          "Extra Cheese":650,
          "Capsicum":460,
          "Sausages":450,
 }

for key,value in Toppings.items():
    print(key,value)
while True:
    t=input("Enter the toppings:\n")
    break


sum_topping=Toppings[t]
Total=sum+sum_topping
print(f"Your total bill is {Total}")
print(f"Your ordered pizza:{y}")
print(f"Your ordered topping is {t}")
print(f"Thank you {r}.")

pizza=open("pizza.txt",'w+')
pizza.write(f"Name of the customer is {r}\n")
pizza.write(f"Total bill of {r} is {Total}\n")
pizza.write(f"pizza is {y}\n")
pizza.write(f"Toppings is {t}")
print(pizza)
pizza.close()

choice = input("\nDo you want to continue ordering? (yes/no): ")
if choice.lower() != "yes":
        order = False

print("\nThank you for your order! Enjoy your pizza!")
