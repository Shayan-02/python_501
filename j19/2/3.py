lst = [1, 2, 3, 5, 4, 5, 5, 6, 4, 7, 7, 5, 3]


counter = 0
element = lst[0]
for i in lst:
    f = lst.count(i)
    if f > counter:
        counter = f
        element = i


print(element)


print(max(lst, key=lst.count))
print(max(set(lst), key=lst.count))
