# input users name
u1_name = input("enter your name: ")
u2_name = input("enter your name: ")

# input users choice
u1 = input(f"{u1_name} enter your choice(""rock"",""paper"",""scissors""): ")
u2 = input(f"{u2_name} enter your choice(""rock"",""paper"",""scissors""): ")

# conditions
if u1 == "rock" or u1 == "paper" or u1 == "scissors" and u2 == "rock" or u2 == "paper" or u2 == "scissors":
    if u1 == u2:
        print("it's a tie")
    elif u1 == "rock":
        if u2 == "scissors":
            print(f"rock smashes scissors, {u1_name} win!")
        else:
            print(f"paper covers rock, {u2_name} win!")
    elif u1 == "paper":
        if u2 == "rock":
            print(f"paper covers rock, {u1_name} win!")
        elif u2 == "scissors":
            print(f"scissors cuts paper, {u2_name} win!")
    elif u1 == "scissors":
        if u2 == "paper":
            print(f"scissors cuts paper, {u1_name} win!")
        elif u2 == "rock":
            print(f"rock smashes scissors, {u2_name} win!")
else:
    print("invalid input")