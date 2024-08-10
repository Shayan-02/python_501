lst = []

lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
b = [5, 6, 7, 8]
lst.append(b)  # [1, 2, 3, 4, [5, 6, 7, 8]]
print(lst)
for i in b:
    lst.append(i)  # [1, 2, 3, 4, [5, 6, 7, 8], 5, 6, 7, 8]

lst.insert(2, "ali")
print(lst)
lst.pop()
lst.pop(3)
print(lst)
lst.remove("ali")
print(lst)