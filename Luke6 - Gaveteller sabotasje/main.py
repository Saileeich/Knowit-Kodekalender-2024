def segment_til_tall(segmenter: dict) -> int:
    resultat = 0
    for i in range(len(list(segmenter.keys()))):
        if (
            segmenter["a"] and
            segmenter["b"] and
            segmenter["c"] and
            segmenter["d"] and
            segmenter["e"] and
            segmenter["f"] and
            not segmenter["g"]
        ):
            resultat += 0*10**i
        elif (
            not segmenter["a"] and
            segmenter["b"] and
            segmenter["c"] and
            not segmenter["d"] and
            not segmenter["e"] and
            not segmenter["f"] and
            not segmenter["g"]
        ):
            resultat += 1*10**i
        elif (
            segmenter["a"] and
            segmenter["b"] and
            not segmenter["c"] and
            segmenter["d"] and
            segmenter["e"] and
            not segmenter["f"] and
            segmenter["g"]
        ):
            resultat += 2*10**i
        elif (
            segmenter["a"] and
            segmenter["b"] and
            segmenter["c"] and
            segmenter["d"] and
            not segmenter["e"] and
            not segmenter["f"] and
            segmenter["g"]
        ):
            resultat += 3*10**i
        elif (
            not segmenter["a"] and
            segmenter["b"] and
            segmenter["c"] and
            not segmenter["d"] and
            not segmenter["e"] and
            segmenter["f"] and
            segmenter["g"]
        ):
            resultat += 4*10**i
        elif (
            segmenter["a"] and
            not segmenter["b"] and
            segmenter["c"] and
            segmenter["d"] and
            not segmenter["e"] and
            segmenter["f"] and
            segmenter["g"]
        ):
            resultat += 5*10**i
        elif (
            segmenter["a"] and
            not segmenter["b"] and
            segmenter["c"] and
            segmenter["d"] and
            segmenter["e"] and
            segmenter["f"] and
            segmenter["g"]
        ):
            resultat += 6*10**i
        elif (
            segmenter["a"] and
            segmenter["b"] and
            segmenter["c"] and
            not segmenter["d"] and
            not segmenter["e"] and
            not segmenter["f"] and
            not segmenter["g"]
        ):
            resultat += 7*10**i
        elif (
            segmenter["a"] and
            segmenter["b"] and
            segmenter["c"] and
            segmenter["d"] and
            segmenter["e"] and
            segmenter["f"] and
            segmenter["g"]
        ):
            resultat += 8*10**i
        elif (
            segmenter["a"] and
            segmenter["b"] and
            segmenter["c"] and
            segmenter["d"] and
            not segmenter["e"] and
            segmenter["f"] and
            segmenter["g"]
        ):
            resultat += 9*10**i
        else:
            resultat += 0*10**i
    return resultat

def tall_til_segment(tall: int) -> dict:
    match tall:
        case 0:
            return {
                "a": True,
                "b": True,
                "c": True,
                "d": True,
                "e": True,
                "f": True,
                "g": False
            }
        case 1:
            return {
                "a": False,
                "b": True,
                "c": True,
                "d": False,
                "e": False,
                "f": False,
                "g": False
            }
        case 2:
            return {
                "a": True,
                "b": True,
                "c": False,
                "d": True,
                "e": True,
                "f": False,
                "g": True
            }
        case 3:
            return {
                "a": True,
                "b": True,
                "c": True,
                "d": True,
                "e": False,
                "f": False,
                "g": True
            }
        case 4:
            return {
                "a": False,
                "b": True,
                "c": True,
                "d": False,
                "e": False,
                "f": True,
                "g": True
            }
        case 5:
            return {
                "a": True,
                "b": False,
                "c": True,
                "d": True,
                "e": False,
                "f": True,
                "g": True
            }
        case 6:
            return {
                "a": True,
                "b": False,
                "c": True,
                "d": True,
                "e": True,
                "f": True,
                "g": True
            }
        case 7:
            return {
                "a": True,
                "b": True,
                "c": True,
                "d": False,
                "e": False,
                "f": False,
                "g": False
            }
        case 8:
            return {
                "a": True,
                "b": True,
                "c": True,
                "d": True,
                "e": True,
                "f": True,
                "g": True
            }
        case 9:
            return {
                "a": True,
                "b": True,
                "c": True,
                "d": True,
                "e": False,
                "f": True,
                "g": True
            }
        case _:
            return {
                "a": False,
                "b": False,
                "c": False,
                "d": False,
                "e": False,
                "f": False,
                "g": False
            }

def øk_visning(segmenter: dict) -> dict:
    for visning in segmenter:
        tall = segment_til_tall(segmenter[visning])
        if tall == 9:
            segmenter[visning] = tall_til_segment(0)
            continue
        segmenter[visning] = tall_til_segment(tall + 1)
        break

def print_segmenter(segmenter: dict):
    visninger = ""
    for visning in list(segmenter.keys())[::-1]:
        visninger += f"{segment_til_tall(segmenter[visning])}"
    print(visninger)

segmenter = {
    "A": {
        "a": True,
        "b": True,
        "c": True,
        "d": True,
        "e": True,
        "f": True,
        "g": False
    },
    "B": {
        "a": True,
        "b": True,
        "c": True,
        "d": True,
        "e": True,
        "f": True,
        "g": False
    },
    "C": {
        "a": True,
        "b": True,
        "c": True,
        "d": True,
        "e": True,
        "f": True,
        "g": False
    },
    "D": {
        "a": True,
        "b": True,
        "c": True,
        "d": True,
        "e": True,
        "f": True,
        "g": False
    },
    "E": {
        "a": True,
        "b": True,
        "c": True,
        "d": True,
        "e": True,
        "f": True,
        "g": False
    },
    "F": {
        "a": True,
        "b": True,
        "c": True,
        "d": True,
        "e": True,
        "f": True,
        "g": False
    },
    "G": {
        "a": True,
        "b": True,
        "c": True,
        "d": True,
        "e": True,
        "f": True,
        "g": False
    },
    "H": {
        "a": True,
        "b": True,
        "c": True,
        "d": True,
        "e": True,
        "f": True,
        "g": False
    },
    "I": {
        "a": True,
        "b": True,
        "c": True,
        "d": True,
        "e": True,
        "f": True,
        "g": False
    }
}
