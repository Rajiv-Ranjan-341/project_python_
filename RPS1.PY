import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "Player"
    else:
        return "Computer"

def get_player_choice(player_number):
    while True:  
        choice = input(f"Player {player_number}, type Rock/Paper/Scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid input. Please choose Rock, Paper, or Scissors.")

def main():
    player_wins = {i: 0 for i in range(4)} 
    computer_wins = 0
    results = []

    while True:
        num_players = int(input("Enter the number of players (1-4) or 0 to quit: "))

        if num_players == 0:
            break
        elif num_players < 1 or num_players > 4:
            print("Invalid number of players. Please enter a number between 1 and 4.")
            continue

        player_choices = [get_player_choice(i) for i in range(num_players)]
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("Computer picked", computer_choice + ".")

        for i, player_choice in enumerate(player_choices):
            winner = determine_winner(player_choice, computer_choice)
            if winner == "Player":
                player_wins[i] += 1  
                print(f"Player {i + 1} won!")
            elif winner == "Computer":
                computer_wins += 1
                print(f"Player {i + 1} lost!")
            else:
                print(f"Player {i + 1} drew with the computer!")

            results.append({"Player": f"Player {i + 1}", "Outcome": winner})

    print("Results:")
    for player, wins in player_wins.items():
        print(f"Player {player + 1} won {wins} times.") 
    print("The computer won", computer_wins, "times")

if __name__ == "__main__":
    main()
