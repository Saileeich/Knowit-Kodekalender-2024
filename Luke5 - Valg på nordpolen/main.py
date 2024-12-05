import math

kandidater = {}
with open("Luke5 - Valg på nordpolen/kandidater.txt", "r") as f:
    for line in f.readlines():
        inf = list(map(lambda x: x.strip(), line.split("-")))
        kandidater[inf[0]] = {
            "navn": inf[1],
            "parti": inf[2],
            "stemmer": 0
        }

stater = {}
with open("Luke5 - Valg på nordpolen/stater.txt", "r") as f:
    for line in f.readlines():
        inf = list(map(lambda x: x.strip(), line.split("-")))
        stater[inf[0]] = {
            "navn": inf[1],
            "valgnisser": int(inf[2]),
            "stemmer": {},
            "totale_stemmer": 0
        }
        for kandidat, stemmer in list(map(lambda x: list(map(lambda y: y.strip(), x.split(":"))), inf[3].split(","))):
            stater[inf[0]]["stemmer"][kandidat] = int(stemmer)
            stater[inf[0]]["totale_stemmer"] += int(stemmer)
        
valgresultat = {
    "k01": 0,
    "k02": 0,
    "k03": 0,
    "k04": 0
}
for stat in list(stater.values()):
    valgnisser = 0
    rest = {}
    resultat = {}
    for kandidat in stat["stemmer"]:
        res_raw = stat["stemmer"][kandidat] / stat["totale_stemmer"] * stat["valgnisser"]
        res_floored = math.floor(res_raw)
        valgnisser += res_floored
        resultat[kandidat] = res_floored
        rest[kandidat] = res_raw - res_floored
    rest_valgnisser = stat["valgnisser"] - valgnisser
    sorted_rest = sorted(rest.items(), key=lambda x: x[1], reverse=True)
    for i in range(rest_valgnisser):
        resultat[sorted_rest[i][0]] += 1
    for parti in valgresultat:
        valgresultat[parti] += resultat[parti]
    
for kandidat in valgresultat:
    print(f"{kandidater[kandidat]["navn"]} - {valgresultat[kandidat]}")