num_1=int(input("Enter a number: "))
num_2=int(input("Enter a number: "))
cal=input("Enter the symbol: ").lower()
if cal=="+":
    obtained=num_1+num_2
elif cal=="-":
    obtained=num_1-num_2
elif cal=="*":
    obtained=num_1*num_2
elif cal=="/":
    obtained=num_1/num_2
print(f"The required ans is {obtained}")
