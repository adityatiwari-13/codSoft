import random

def rock_paper_scissors():
    print("Rock, Paper, Scissors Game")
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose rock, paper, or scissors:")
        user_choice = input("Your choice: ").lower()

        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break
rock_paper_scissors()
