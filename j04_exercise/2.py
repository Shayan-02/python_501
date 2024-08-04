num1 = float(input("enter number1: "))
num2 = float(input("enter number2: "))
num3 = float(input("enter number3: "))

avg = (num1 + num2 + num3) / 3

if avg == int(avg):
    print(int(avg))
else:
    print(avg)