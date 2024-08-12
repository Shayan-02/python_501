lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 6, 7, 8]

for i in lst1:
    if i not in lst2:
        print(i)


a = 10
print(a is int(a))
print(type(a) is int)