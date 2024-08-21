def jam(num1, num2):
    result = num1 + num2
    print(result)


def tafrigh(num1, num2):
    result = num1 - num2
    print(result)


def zarb(num1, num2):
    result = num1 * num2
    print(result)


def taghsim(num1, num2):
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print("div by 0")


num1 = int(input("num1: "))
op = input("op: (+, -, *, /): ")
num2 = int(input("num2: "))

if op == "+":
    jam(num1, num2)
elif op == "-":
    tafrigh(num1, num2)
elif op == "*":
    zarb(num1, num2)
elif op == "/":
    taghsim(num1, num2)