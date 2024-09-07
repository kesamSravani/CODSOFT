import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_choices(user_choice, computer_choice):
    """Display the choices made by the user and the computer."""
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

def main():
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock-Paper-Scissors Game!")
    
    while True:
        # User input
        user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please select rock, paper, or scissors.")
            continue
        
        # Computer choice
        computer_choice = get_computer_choice()
        
        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        
        # Display results
        display_choices(user_choice, computer_choice)
        if result == 'tie':
            print("It's a tie!")
        elif result == 'user':
            print("Congratulations! You win!")
            user_score += 1
        else:
            print("Sorry, you lose!")
            computer_score += 1
        
        # Display scores
        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThank you for playing! Goodbye!")
            break

# Run the main function
if __name__ == "__main__":
    main()
