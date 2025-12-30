

# Day 1
def armstrongNumber(num: int)-> bool:
    total = 0
    nod = list(str(num))
    for i in nod:
        total += int(i)**len(nod)
    return num == total

print(armstrongNumber(153))
print(armstrongNumber(128))


