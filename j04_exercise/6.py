# input three numbers
num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))
num3 = int(input("enter number3: "))

# sort numbers and print
if num1 == num2 == num3:
    print("numbers are equal")
elif num1 < num2 < num3:
    print(f"{num1} < {num2} < {num3}")
elif num1 < num3 < num2:
    print(f"{num1} < {num3} < {num2}")
elif num2 < num1 < num3:
    print(f"{num2} < {num1} < {num3}")
elif num2 < num3 < num1:
    print(f"{num2} < {num3} < {num1}")
elif num3 < num1 < num2:
    print(f"{num3} < {num1} < {num2}")
elif num3 < num2 < num1:
    print(f"{num3} < {num2} < {num1}")
