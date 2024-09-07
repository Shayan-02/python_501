import random

entekhabha = ["sang", "kaghaz", "gheichi"]

c_score, u_score = 0, 0

for i in range(5):
    computer = random.choice(entekhabha)
    user = input("sang kaghaz gheichi: ")
    if user not in entekhabha:
        print("invalid")
    else:
        if user == computer:
            print("draw")
        elif user == entekhabha[0]:
            if computer == entekhabha[1]:
                print("computer")
                c_score += 1
            elif computer == entekhabha[2]:
                print("user")
                u_score += 1
        elif user == entekhabha[1]:
            if computer == entekhabha[0]:
                print("user")
                u_score += 1
            elif computer == entekhabha[2]:
                c_score += 1
                print("computer")
        elif user == entekhabha[2]:
            if computer == entekhabha[0]:
                print("user")
                u_score += 1
            elif computer == entekhabha[1]:
                c_score += 1
                print("computer")

print(c_score, u_score, (5 - c_score - u_score))
