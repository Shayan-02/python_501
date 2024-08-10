# input numbers
num1 = float(input("enter number1: "))
num2 = float(input("enter number2: "))
num3 = float(input("enter number3: "))

# calculate average
avg = (num1 + num2 + num3) / 3

# convert float avg to int avg if it possible
if avg == int(avg):
    print(int(avg))
else:
    print(avg)