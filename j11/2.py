def calcBmi(vazn, ghad):
    if ghad >= 100:
        ghad = ghad / 100
    if vazn >= 1000:
        vazn /= 1000
    bmi = vazn / (ghad ** 2)
    print(f"your bmi is {bmi}")
    if bmi < 18:
        print("laaghar")
    elif 18 <= bmi <= 25:
        print("normal")
    elif bmi > 25:
        print("chaagh")


v = int(input("vazn: "))
g = int(input("ghad: "))
calcBmi(v, g)