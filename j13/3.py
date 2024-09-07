n = int(input("enter a number: "))
transposted = [(i*j) for j in range(1, n + 1) for i in range(1, n+1)]
print(transposted)