def tekst_til_tall(tekst: str):
    teksttall = {
        "nitti": 90,
        "åtti": 80,
        "sytti": 70,
        "seksti": 60,
        "femti": 50,
        "førti": 40,
        "tretti": 30,
        "tjue": 20,
        "nitten": 19,
        "atten": 18,
        "sytten": 17,
        "seksten": 16,
        "femten": 15,
        "fjorten": 14,
        "tretten": 13,
        "tolv": 12,
        "elleve": 11,
        "ti": 10,
        "ni": 9,
        "åtte": 8,
        "syv": 7,
        "seks": 6,
        "fem": 5,
        "fire": 4,
        "tre": 3,
        "to": 2,
        "en": 1
    }

    sum = 0
    for key, value in teksttall.items():
        if (x:=tekst.count(key)):
            tekst = tekst.replace(key, "")
            sum += value*x
            print(key, x, value*x)

    return sum

tekst = ""
with open("Luke9 - Væralven/tall.txt", "r", encoding="utf-8") as f:
    tekst = f.read()

print(tekst_til_tall(tekst)/6)

