'''
my_list=[10, 50, 30]
if my_list[0]>my_list[1] and my_list[0]>my_list[2]:
    print(f"The greatest number is: {my_list[0]}")
elif my_list[1]>my_list[0] and my_list[1]>my_list[2]:
    print(f"The greatest number is: {my_list[1]}")
else:
    print(f"The greatest number is: {my_list[2]}")'''
    
my_list=[]
for i in range (0,3,1):
    user_input=int(input("Enter a number: "))
    my_list.append(user_input)
print(my_list)
if my_list[0]>my_list[1] and my_list[0]>my_list[2]:
    print(f"The greatest number is: {my_list[0]}")
elif my_list[1]>my_list[0] and my_list[1]>my_list[2]:
    print(f"The greatest number is: {my_list[1]}")
else:
    print(f"The greatest number is: {my_list[2]}")
    