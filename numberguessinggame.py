import random

guess = random.randint(1, 100)

while True:
    try:
        user_guess = int(input("Enter Your Guess Here (only numbers): "))
        
        if user_guess < guess:
            print("Too Low")
        elif user_guess > guess:
            print("Too High")
        else:
            print("Correct! You guessed it! 🎉")
            break  # Exit the loop once the correct guess is made

    except ValueError:
        print("Invalid input! Please enter a number.")
