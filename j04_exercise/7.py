# input grades
math = float(input("math: "))
phisics = float(input("phisics: "))
chemistry = float(input("chemistry: "))
arabic = float(input("arabic: "))

# calculate average
avg = (math + phisics + chemistry + arabic) / 4

# if 0 <= math <= 20 and 0 <= phisics <= 20 and 0 <= chemistry <= 20 and 0 <= arabic <= 20:
#     if avg >= 18:
#         print(f"avg: {avg} so you earned grade A")
#     elif avg >= 16:
#         print(f"avg: {avg} so you earned grade B")
#     elif avg >= 14:
#         print(f"avg: {avg} so you earned grade C")
#     elif avg >= 10:
#         print(f"avg: {avg} so you earned grade D")
#     else:
#         print(f"avg: {avg} so you Failed")
# else:
#     print("invalid marks")

# print average status
if math in range(21) and phisics in range(21) and chemistry in range(21) and arabic in range(21):
    if avg >= 18:
        print(f"avg: {avg} so you earned grade A")
    elif avg >= 16:
        print(f"avg: {avg} so you earned grade B")
    elif avg >= 14:
        print(f"avg: {avg} so you earned grade C")
    elif avg >= 10:
        print(f"avg: {avg} so you earned grade D")
    else:
        print(f"avg: {avg} so you Failed")
else:
    print("invalid marks")