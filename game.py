import random
comp_score=0
user_score=0
for loop in range(0,5,1):
    comp_guess =random.randint(0,6) 
    user_guess =int(input("Enter a guess number: "))
    print(f"The computer guess is : {comp_guess}")
    if comp_guess<user_guess:
        comp_score+=10
    print(f"The computer score is: {comp_score}")
    print(f"The user score is: {user_score}")

    if user_guess<comp_guess:
        user_score+=10
    elif comp_guess == user_guess:
        print("No increment in score")
       
