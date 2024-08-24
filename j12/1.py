def avg(num1, num2):
    # global avge
    avge = (num1 + num2) / 2
    max_num = max(num1, num2)
    return avge, max_num


b = avg(10, 20)
for i in b:
    print(i*3, end=" ")

