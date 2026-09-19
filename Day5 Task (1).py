
#Get the score for each user and declare the winner
#play the game for 10 times --->Task (push to github and share it (tasks))# Get the score for each user and declare the winner
# Play the game for 10 times

import random


def rock_paper_scissors(*args, **kwargs):

    player1_score = 0
    player2_score = 0

    for i in range(1, kwargs["rounds"] + 1):

        print("\nRound", i)

        player1 = input(
            "Enter one of these --> Rock, Paper, Scissors: "
        ).lower().strip()

        player2 = random.choice(args)

        print("Computer:", player2)

        if player1 == player2:
            print("Tie")

        elif (player1 == "rock" and player2 == "scissors") or \
             (player1 == "paper" and player2 == "rock") or \
             (player1 == "scissors" and player2 == "paper"):

            print("Player1 won")
            player1_score += 1

        elif (player1 == "rock" and player2 == "paper") or \
             (player1 == "paper" and player2 == "scissors") or \
             (player1 == "scissors" and player2 == "rock"):

            print("Player2 won")
            player2_score += 1

        else:
            print("Invalid input")

    print("\n----- FINAL SCORE -----")

    print("Player1 Score:", player1_score)

    print("Player2 Score:", player2_score)

    if player1_score > player2_score:
        print("Player1 is the Winner!")

    elif player2_score > player1_score:
        print("Player2 is the Winner!")

    else:
        print("Game is Tie!")


rock_paper_scissors(
    "rock",
    "paper",
    "scissors",
    rounds=10
)



































