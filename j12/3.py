def test(*a):
    alireza = []
    sums = 0
    for i in a:
        alireza.append(int(i))
        sums += i
        avg = sums/len(a) if len(a) != 0 else 0
    mohammad = max(set(alireza), key=alireza.count)
    return avg, max(alireza), min(alireza), mohammad

a = input().split()
print(test(a))
