# create function for rock-paper-scisoors game that have choices of rock, paper, and scissors
# and the computer will randomly choose one of them
# 1. input rock, paper, scissors, quit
# 2. computer random choice rock, paper, scissors, quit
# if user input rock and computer random choice scissors, user win
# if user input scissors and computer random choice paper, user win
# if user input paper and computer random choice rock, user win
# if user input rock and computer random choice paper, computer win
# if user input scissors and computer random choice rock, computer win
# if user input paper and computer random choice scissors, computer win
# if user input rock and computer random choice rock, it's a tie
# 3. print out the result and keep track of the score of the game
# 4  print round and current round's winner, player's score and number of games played
# 5. play agin or quit

import random
def rock_paper_scissors():
    user = input("Please enter rock, paper, scissors, or quit: ")
    computer = random.choice(["rock", "paper", "scissors"])
    if user == "quit":
        return "Goodbye"
    elif user == "rock" and computer == "scissors":
        return "You win"
    elif user == "scissors" and computer == "paper":
        return "You win"
    elif user == "paper" and computer == "rock":
        return "You win"
    elif user == "rock" and computer == "paper":
        return "Computer win"
    elif user == "scissors" and computer == "rock":
        return "Computer win"
    elif user == "paper" and computer == "scissors":
        return "Computer win"
    elif user == "rock" and computer == "rock":
        return "It's a tie"
    elif user == "paper" and computer == "paper":
        return "It's a tie"
    elif user == "scissors" and computer == "scissors":
        return "It's a tie"
    else:
        return "Please enter rock, paper, scissors, or quit"

# create function to play again or quit and print out the result and keep track of the score of the game
def play_again():
    while True:
        answer = input("Would you like to play again? yes/no: ")
        if answer == "yes":
            return rock_paper_scissors()
        elif answer == "no":
            return "Goodbye"
        else:
            print("Please enter yes or no")
            continue

# create function to play rock-paper-scissors game
def play_game():
    print(rock_paper_scissors())
    print(play_again())


# create main function
def main():
    play_game()

if __name__ == "__main__":
    main()


