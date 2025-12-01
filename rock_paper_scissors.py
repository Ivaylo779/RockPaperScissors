import random

player_score = 0
computer_score = 0

while True:
    valid_moves = ['rock', 'paper', 'scissors']

    player_move = input("Choose Rock, Paper or Scissors: ").strip().lower()

    if player_move not in valid_moves:
        raise SystemExit("Invalid move. Try again...")

    computer_move = random.randint(1, 3)

    if computer_move == 1:
        computer_move = "rock"
    elif computer_move == 2:
        computer_move = "paper"
    elif computer_move == 3:
        computer_move = "scissors"

    print(f"The computer chose {computer_move}.")

    if player_move == 'rock' and computer_move == 'scissors' or \
            player_move == 'paper' and computer_move == 'rock' or \
            player_move == 'scissors' and computer_move == 'paper':
        print("You Won!")
        player_score += 1

    elif player_move == computer_move:
        print("Draw!")

    else:
        print("You Lost!")
        computer_score += 1

    print("Scores:\n"
          f"Player score: {player_score}\n"
          f"Computer score: {computer_score}")

    quit_condition = input("Do you want to play again? (yes/no): ").strip().lower()
    if quit_condition == 'no':
        print("Final scores:\n"
              f"Player score: {player_score}\n"
              f"Computer score: {computer_score}")
        print("Thank you for playing!")
        exit()
    elif quit_condition == 'yes':
        continue
    else:
        print("Invalid input. Try again.")
