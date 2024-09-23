num1 = int(input("enter a number: "))
op = input("enter an operator: ")
num2 = int(input("enter another number: "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("invalid input")
else:
    print("invalid operator")


print("edameh")
