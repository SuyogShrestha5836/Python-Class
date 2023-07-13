num =input("Enter the symbol: ")
if num =="+":
    a=10
    b=20
    obtained=a+b
elif num =="-":
    a=10
    b=20
    obtained=a-b
elif num =="*":
    a=10
    b=20
    obtained=a*b
elif num =="/":
    a=10
    b=20
    obtained=a/b
else:
    obtained="Something went wrong"
print(f'The required ans is: {obtained}')
