with open("test.txt", "r+") as f:
    f.write("\nsalam")
    f.write("\nhello")
    print(f.read())
    print(f.readline(2))
