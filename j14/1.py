import random

correct = random.randint(1, 10)
for i in range(5):
    guess = int(input(f"enter your guess{i+1}: "))
    if guess == correct:
        print("you are right")
        break
    elif guess < correct:
        print("too low")
    else:
        print("too high")

