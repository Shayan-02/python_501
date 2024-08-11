lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lst[6] = 5
# tpl[3] = 5

c = list(tpl)
c[5] = "ali"
tpl = tuple(c)

lst.remove(4)
lst.insert(3, "ali")