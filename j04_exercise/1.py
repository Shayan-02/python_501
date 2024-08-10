# input numbers
num1 = float(input("enter number1: "))
num2 = float(input("enter number2: "))
num3 = float(input("enter number3: "))

# print int of numbers in one line
print(int(num1), int(num2), int(num3), sep="*")

# print int of numbers in three lines
print(int(num1), end="*")
print(int(num2), end="*")
print(int(num3))