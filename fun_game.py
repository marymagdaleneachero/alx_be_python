import random

secret_number = random.randint(1, 10)
guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it?: "))

match guess:
    case guess:
        if guess == secret_number:
            print("Congratulations, you guessed it!")
        elif guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")
        elif guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")

play_again = input("Play again?(yes/no): ")
if play_again.lower() == "yes":
    print("Restart the program to play again.")
else:
    print("Thanks for playing!")