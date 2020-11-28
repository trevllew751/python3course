from random import randint

# age = int(input("Type your age:\n"))
# if age in range(0, 18):
#     print("You are a minor")
# else:
#     print("You are an adult")

# times = int(input("How many times do I have to tell you?\n"))
# for n in range(times):
#     print("CLEAN UP YOUR ROOM")

# for n in range(1, 21):
#     if n == 4 or n == 13:
#         print(f"{n}: Unlucky")
#     elif n % 2 == 1:
#         print(f"{n}: Odd")
#     else:
#         print(f"{n}: Even")

# msg = input("What's the secret password? ")
# while msg != "bananas":
#     print("Wrong!")
#     msg = input("What's the secret password? ")
# print("Correct!")

# for n in range(1, 11):
#     print("\U0001F600" * n)
# n = 1
# while n < 11:
#     print("\U0001F600" * n)
#     n += 1

# print("Say something: ")
# response = input()
# while response != "stop copying me":
#     print(response)
#     response = input()

play_again = "y"
while play_again == "y":
    random_num = randint(1, 10)
    guess = int(input("What is your guess?\n"))
    while guess != random_num:
        if guess < random_num:
            hint = "low"
        else:
            hint = "high"
        print(f"Your guess was too {hint}, guess again!")
        guess = int(input())
    print("Correct!")
    print("Would you like to play again? (y/n)")
    play_again = input()
print("Thanks for playing!")
