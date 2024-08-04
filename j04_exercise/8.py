temp = int(input("enter a number: "))

if temp < 0:
    print("ice")
else:
    if temp < 100:
        print("water")
    else:
        print("steam")