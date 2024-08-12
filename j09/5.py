lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 6, 7, 8]

s1 = set(lst1)
s2 = set(lst2)

s3 = s1 - s2 # a - b
s4 = s2 - s1 # b - a
s5 = s1 - (s1 - s2) # a & b

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

