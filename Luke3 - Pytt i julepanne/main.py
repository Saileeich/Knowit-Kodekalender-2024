tallerken = {
    "ris": 100,
    "erter": 100,
    "gulrøtter": 100,
    "reinsdyrkjøtt": 100,
    "julekringle": 100
}

påfyll = {
    "ris": [0, 0, 1, 0, 0, 2],
    "erter": [0, 3, 0, 0],
    "gulrøtter": [0, 1, 0, 0, 0, 8],
    "reinsdyrkjøtt": [100, 80, 40, 20, 10]
}

def spis_mat(tallerken: dict) -> list:
    spist_mat = []
    for mat in list(tallerken.keys())[:3:]:
        if mat in spist_mat:
            continue
        
        if tallerken[mat] > 0:
            spist_mat.append(mat)
            tallerken[mat] = max(tallerken[mat] - 5, 0)
            break
    
    if not spist_mat:
        if tallerken["reinsdyrkjøtt"] > 0:
            spist_mat.append("reinsdyrkjøtt")
            tallerken["reinsdyrkjøtt"] = max(tallerken["reinsdyrkjøtt"] - 2, 0)
        else:
            spist_mat.append("julekringle")
            tallerken["julekringle"] = max(tallerken["julekringle"] - 1, 0)
    else:
        for mat in list(tallerken.keys())[1:3:]:
            if mat in spist_mat:
                continue
            
            if tallerken[mat] > 0:
                spist_mat.append(mat)
                tallerken[mat] = max(tallerken[mat] - 3, 0)
                break
    return spist_mat

reinsdyrkjøtt_tid = 0
def fyll_på(tallerken: dict, påfyll: dict, t: int, reinsdyrkjøtt_tid: int) -> list:
    ris_påfyll = påfyll["ris"][t % len(påfyll["ris"])]
    erter_påfyll = påfyll["erter"][t % len(påfyll["erter"])]
    gulrot_påfyll = påfyll["gulrøtter"][(t-31) % len(påfyll["gulrøtter"])] if t > 30 else 0
    fylt_på = []
    
    tallerken["ris"] += ris_påfyll
    tallerken["erter"] += erter_påfyll
    tallerken["gulrøtter"] += gulrot_påfyll

    if ris_påfyll: fylt_på.append("ris")
    if erter_påfyll: fylt_på.append("erter")
    if gulrot_påfyll: fylt_på.append("gulrøtter")

    if not tallerken["reinsdyrkjøtt"] and reinsdyrkjøtt_tid >= 0 and påfyll["reinsdyrkjøtt"]:
        tallerken["reinsdyrkjøtt"] += påfyll["reinsdyrkjøtt"].pop(0)
        reinsdyrkjøtt_tid = -50
        fylt_på.append("reinsdyrkjøtt")
    
    return fylt_på
    


t = 0
while tallerken["julekringle"]:
    spis_resultat = spis_mat(tallerken)
    fyll_resultat = fyll_på(tallerken, påfyll, t, reinsdyrkjøtt_tid)
    print(f"{t:<5} {str(spis_resultat):<20} {str(fyll_resultat):<48} {tallerken}")
    reinsdyrkjøtt_tid += 1
    t += 1
print(t)
