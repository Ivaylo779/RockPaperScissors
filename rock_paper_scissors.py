import random

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

if player_move == 'rock' and computer_move == 'scissors' or \
        player_move == 'paper' and computer_move == 'rock' or \
        player_move == 'scissors' and computer_move == 'paper':
    print("You Won!")

elif player_move == computer_move:
    print("Draw!")

else:
    print("You Lost!")
