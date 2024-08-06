i = 1
while i <= 20:
    if i == 7:
        i += 2
        continue
    if i == 13:
        continue
        i += 3
    if i == 16:
        break
    
    print(i)
    i += 1