import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.user_score += 1
            return "user"
        else:
            self.computer_score += 1
            return "computer"

    def play_game(self):
        print("\nWelcome to Rock-Paper-Scissors!")
        while True:
            user_choice = input("Enter Rock, Paper, or Scissors (or 'quit' to exit): ").strip().lower()
            if user_choice == "quit":
                break
            if user_choice not in self.choices:
                print("Invalid choice. Try again!")
                continue
            
            computer_choice = self.get_computer_choice()
            winner = self.determine_winner(user_choice, computer_choice)
            
            print(f"Computer chose: {computer_choice.capitalize()}")
            if winner == "draw":
                print("It's a draw!")
            elif winner == "user":
                print("You win this round!")
            else:
                print("Computer wins this round!")
            
            print(f"Score -> You: {self.user_score} | Computer: {self.computer_score}\n")
        
        print("Game Over! Final Score:")
        print(f"You: {self.user_score} | Computer: {self.computer_score}")

# Run the game
if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
