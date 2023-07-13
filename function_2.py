#def demo(operation,num_one,num_two)
#output=num_one operation num_two
#print(output)
operation=input("Enter the operation:")
first_num=int(input("Enter the first number:"))
second_num=int(input("Enter the second number:"))
def demo(operation,first_num,second_num):
    if operation=="+":
     print(first_num+second_num)
    elif operation=="-":
        print(first_num-second_num)
    elif operation=="*":
        print(first_num*second_num)
    elif operation=="/":
        print(first_num/second_num)
demo(operation,first_num,second_num)