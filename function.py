def add_number(xyz,b_parameter): #creating function expecting 2 parameters 
    sum=xyz+b_parameter 
    return sum
#default return type

a_value= int(input("Enter the first number "))
b_value= int(input("Enter the second number "))
print(add_number(a_value,b_value))