"""
På den polare prærien er det viktig å holde seg varm om nettene, selv for en barsk kugutt-alv. 
Alven vår vil sove og leter etter et koselig sted og et godt teppe for natten, men det eneste 
teppet han finner har en merkelig form. Han prøver alle måter å legge teppet over seg for å 
dekke så mye som mulig av kroppen sin og samtidig sørge for at de viktigste kroppsdelene er 
gode og varme og koser seg.

Hva er den høyeste graden av koselighet kugutt-alven vår kan oppnå ved å legge teppet over seg? 
Koselighetsgraden er summen av koselighets-score for alle deler av kroppen som er dekket. 
Teppet kan flyttes i x- og y-aksen og roteres 90 grader.
"""

blanket = [
    "nxxxn",
    "xxxxx",
    "xxxxx",
    "xxxxx",
    "xxxxx",
    "nnxnn",
    "xxxxx",
    "xxxxx",
    "xxxxx",
    "xxxxx",
    "nxxxn"
]

with open("Luke1/joe.txt", "r") as file:
    joe = file.read().splitlines()

koselighetsgrader = []
for y in range(len(joe)):
    for x in range(-6,14):
        koselighetsgrad0 = 0
        koselighetsgrad90 = 0

        for blanket_y in range(len(blanket)):
            for blanket_x in range(len(blanket[0])):
                if blanket[blanket_y][blanket_x] == "x":
                    try:
                        koselighetsgrad0 += int(joe[y+blanket_y][x+blanket_x])
                    except:
                        pass

        koselighetsgrader.append(max(koselighetsgrad0, koselighetsgrad90))

print(max(koselighetsgrader))
