import random

def play():
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)

    health = 4
    win = False

    # ask user to guess the number
    while health > 0 and !win:
        print(f"You have {health} tries")
        user_guess = int(input("Guess a number from 1 to 10: "))

        # check if user guessed the number correctly
        if user_guess == random_number:
            print("Congrats! You guessed the number correct")
            result = 1
        elif user_guess > random_number:
            print("Your guess was too high.")
            health -= 1
        else:
            print("Your guess was too low.")
            health -= 1

    if !win:
        print(f"You lost. The number was {random_number}.")

    return win


def main():
    number_of_wins = 0
    number_of_losses = 0
    number_of_games = 0

    print("Option 1 => Play the Guessing Game")
    print("Option 2 => Show game stats")
    print("Option 3 => Exit the game")

    while option != 3:
        if option == 1:
            win = play()  # result = False if lost, True if won
            number_of_games += 1
            if win:
                number_of_wins += 1
            else:
                number_of_losses += 1
        elif option == 2:
            print(f"Number of Games: {number_of_games} Number of Wins: {number_of_wins} Number of Losses: {number_of_losses}")
        elif option == 3:
            print("Thank you for playing the guessing game!")
        else:
            print("Your input is invalid.")

if __name__ == "__main__":
    main()

