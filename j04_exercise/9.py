# correct number
correct = 50

# input user guess
guess = int(input("enter your guess: "))

# print user guess status
if guess == correct:
    print("you are right")
else:
    if guess < correct:
        print("too low")
    else:
        print("too high")