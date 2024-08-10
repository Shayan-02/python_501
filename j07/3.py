a = [1, 2, 3, "ali", "reza", True, None]
print(a)
b = 1, 2, 3, 4
print(b)
c = list(b)
d = list()
e = list((1, 2, 3))

c[2] = "ali"
b = tuple(c)