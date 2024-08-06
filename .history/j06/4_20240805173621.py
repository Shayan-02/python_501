i = 1
while i <= 20:
    if i == 7:
        i += 2
        continue
    if i == 13:
        i += 3
        continue
    if i == 16:
        print("bye")
        break
    print(i)
    i += 1