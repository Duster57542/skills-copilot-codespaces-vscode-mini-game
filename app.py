import random

def play_game():
    options = {'r': 'rock', 'p': 'paper', 's': 'scissors', 'rock': 'rock', 'paper': 'paper', 'scissors': 'scissors'}
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Enter your choice (r/p/s for rock/paper/scissors): ").lower()

        if player_choice not in options.keys():
            print("Invalid option. Please choose r, p, s, rock, paper, or scissors.")
            continue

        computer_choice = random.choice(list(options.values()))

        print(f"Player chooses: {options[player_choice]}")
        print(f"Computer chooses: {computer_choice}")

        if options[player_choice] == computer_choice:
            print("It's a tie!")
        elif (options[player_choice] == 'rock' and computer_choice == 'scissors') or \
             (options[player_choice] == 'scissors' and computer_choice == 'paper') or \
             (options[player_choice] == 'paper' and computer_choice == 'rock'):
            print("Player wins!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        play_again = input("Do you want to play again? (Y/N) [default: Y]: ").lower() or 'y'
        if play_again not in ['y', 'yes']:
            break

    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

play_game()
