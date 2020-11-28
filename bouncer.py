age = input("How old are you?\n")

if age:
    age = int(age)
    if age >= 21:
        print("You can enter and you can drink")
    elif age >= 18:
        print("You can enter but you need a wristband")
    else:
        print("You cannot come in little one")
else:
    print("Please enter an age")
