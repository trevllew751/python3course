from random import randint

computer_score = 0
player_score = 0
winning_score = 3
while computer_score != winning_score and player_score != winning_score:
    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")
    pl1 = input("Enter your choice\n").lower()
    if pl1 == "quit" or pl1 == "q":
        break
    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"Computer: {computer}")
    if pl1 == computer:
        print("Tie")
    elif pl1 == "rock" and computer == "scissors":
        player_score += 1
    elif pl1 == "scissors" and computer == "paper":
        player_score += 1
    elif pl1 == "paper" and computer == "rock":
        player_score += 1
    else:
        computer_score += 1
if computer_score > player_score:
    winner = "Computer"
else:
    winner = "Player"
print(f"Player: {player_score}")
print(f"Computer: {computer_score}")
print(f"{winner} wins!")
