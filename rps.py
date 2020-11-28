from random import randint
pl1 = input("Enter your choice\n")
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
    print("Player wins")
elif pl1 == "scissors" and computer == "paper":
    print("Player wins")
elif pl1 == "paper" and computer == "rock":
    print("Player wins")
else:
    print("Computer wins")
# print("***NO CHEATING***\n" * 100)
# pl2 = input("Player2 choice\n")
# if pl1 == pl2:
#     print("Tie")
# elif pl1 == "rock":
#     if pl2 == "scissors":
#         print("Player1 wins")
#     elif pl2 == "paper":
#         print("Player2 wins")
# elif pl1 == "paper":
#     if pl2 == "scissors":
#         print("Player2 wins")
#     elif pl2 == "rock":
#         print("Player1 wins")
# else:
#     if pl2 == "rock":
#         print("Player2 wins")
#     elif pl2 == "paper":
#         print("Player1 wins")
# print("Haha Python go b" + "r" * 10)
