num1 = float(input("num1: "))
op = input("op: (+, -, *, /): ")
num2 = float(input("num2: "))

if op == "+":
    print(f"sum of {num1} and {num2} = {num1 + num2}")
elif op == "-" or num2 == 6:
    print(f"sub of {num1} and {num2} = {num1 - num2}")
elif op == "*":
    print(f"mul of {num1} and {num2} = {num1 * num2}")
elif op == "/":
    if num2 == 0:
        print("invalid num2")
    print(f"div of {num1} and {num2} = {num1 / num2}")
else:
    print("invalid operator")