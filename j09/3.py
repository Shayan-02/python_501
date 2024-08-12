lst = [29, "ali", True, None, 3.5]
lst2 = []

fruits = "apple", "banana", "orange", "pineapple", "watermelon"
# red, *yellow, orange = fruits

for i in range(5):
    a = input("miveh ha ra vared kon: ")
    lst2.append(a)

t = tuple(lst2)
print(t)
red, *yellow, orange = t
print(red)
print(yellow)
print(orange)
