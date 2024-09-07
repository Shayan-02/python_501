lst = [1, 2, 3, 5, 4, 5, 5, 6, 4, 7, 7, 5, 3]

def most(lst):
    counter = 0
    element = lst[0]
    for i in lst:
        f = lst.count(i)
        if f > counter:
            counter = f
            element = i
    return element, counter


print(most(lst))

print(max(lst, key=lst.count))