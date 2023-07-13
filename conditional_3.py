marks=int(input("Enter your marks: "))
if marks>=80:
    obtained ="A Grade"
elif marks>=70:
    obtained ="B Grade" 
elif marks>=60:
    obtained ="C Grade"
elif marks>=50:
    obtained ="D grade" 
elif marks>=40:
    obtained ="E grade"
else: 
    obtained ="Not graded"
#print("The grade is: " + str(obtained))
print(f'The grade is: {obtained}')