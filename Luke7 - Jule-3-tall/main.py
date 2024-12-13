import math

def er_lystig(tall: int) -> bool:
    if tall == 1 or tall == 0:
        return True

    try:
        return er_lystig(sum(list(map(lambda x: math.pow(int(x), 2), str(int(tall))))))
    except RecursionError:
        return False

def er_jule_3_tall(tall: int) -> bool:
    tallstreng = str(tall)
    sjekk1 = er_lystig(tall)
    sjekk2 = er_lystig(int(tallstreng[:len(tallstreng)//2:]))
    sjekk3 = er_lystig(int(tallstreng[math.ceil(len(tallstreng)/2)::]))

    return sjekk1 and sjekk2 and sjekk3

n = 10_000_000
for i in range(n-1):
    if er_jule_3_tall(n-1-i):
        print(n-1-i)
        break
