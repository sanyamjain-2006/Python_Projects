import random
choices=["r","p","s"] #choices for computer
while True:
    user_choice=input("Enter Your Choice (r/p/s):").lower()#taking input of user
    computer_choice=random.choice(choices)#computer choosing it choice
    # when user choose rock
    if (user_choice=="r" and computer_choice=="s") or (user_choice=="s" and computer_choice=="p")or (user_choice=="p" and computer_choice=="r"):#condition when user win 
        print(f"You Choose:{user_choice} \ncomputer choose:{computer_choice}")
        print("You win🎉🎉")
    elif(computer_choice=="r" and user_choice=="s") or (computer_choice=="s" and user_choice=="p") or (computer_choice=="p" and user_choice=="r"):#condition when computer win
        print(f"You Choose:{user_choice} \ncomputer choose:{computer_choice}")
        print("computer win😞😞")
    elif(computer_choice=="r" and user_choice=="r") or (computer_choice=="s" and user_choice=="s") or (user_choice=="p" and computer_choice=="p"):#condition when game tie
        print(f"You Choose:{user_choice} \ncomputer choose:{computer_choice}")
        print(f"The Game is tie")
        
    else:
        print("please Enter a valid choice")
    another_round=input("Do you Want To Continue (y/n):").lower()#continue game
    if another_round=="y":
        print("Loading....")
    elif another_round=="n":
        print("Thanks For Playing")
        break#exiting the loop
    else:
        print("Please Enter The Valid choice from (y/n)")





