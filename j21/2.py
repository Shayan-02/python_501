num1 = int(input("enter a number: "))
op = input("enter an operator: ")
num2 = (input("enter another number: "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    try:
        print(num1 / num2)
    except ValueError:
        print("invalid input")
    except ZeroDivisionError:
        print("Cannot divide by zero")
