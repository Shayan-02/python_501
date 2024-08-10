# input number
num = int(input("enter a number: "))

# print number status
if num == 0:
    print("number is zero")
elif num % 2 == 0:
    print("number is even")
else:
    print("number is odd")