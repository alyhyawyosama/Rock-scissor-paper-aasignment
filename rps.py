import random
#paper","rock","scissor"
choices  = ["p","r","s"]
attempts = 6
user_won = 0
computer_won = 0


while attempts > 0:
    computer_choice = random.choices(choices)[0]
    user_choice = input("P -> paper\nR -> Rock\nS -> Scissor \nEnter Your choice:")
    user_choice = user_choice.lower()
    print(f"User : {user_choice} , Computer : {computer_choice}")
    if user_choice not in choices :
        print("Invalid input ,Try again")
        continue
    if computer_choice == user_choice.lower() :
        print("The same choice,Try again")
        continue
    elif  computer_choice == "p" and user_choice == "r" :
        computer_won += 1 
        print("Computer has a point")
    elif  computer_choice == "s" and user_choice == "p" :
        computer_won += 1
        print("Computer has a point")
    elif  computer_choice == "r" and user_choice == "s" :
        computer_won += 1
        print("Computer has a point")
    else:
        user_won += 1
        print("You have a point")
    attempts -=1
    
    print(f"Result -> Computer: {computer_won} - user: {user_won} ")
    
    if user_won == computer_won and attempts == 0 :
        print("equal points,Try again")
        attempts +=1
    print(f"There are {attempts} left")
    
    #If the computer or the user has more than 3 won stop the game  
    if computer_won > 3 or user_won > 3 :
        break
     
if user_won > computer_won :
    print("Congratulation for you")
else :
    print("Congratulation for the computer")


