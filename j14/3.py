def randint(a, b):
    global c
    c = 50
    return int(a) + int(b)

a = int(input())
b = int(input())
print(randint(a, b) * 2)
print(c)