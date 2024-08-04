correct = 50

guess = int(input("enter your guess: "))

if guess == correct:
    print("you are right")
else:
    if guess < correct:
        print("too low")
    else:
        print("too high")