# Jule-3-tall
<big>*Av* ***Hugo Wallenburg***</big>

Lystige juletall er tall hvor du gjentatte ganger tar summen av kvadratene til sifrene i tallet og til slutt ender opp med bare 1. For eksempel er 19 et lystig juletall fordi 1<sup>2</sup> + 9<sup>2</sup> = 82, 8<sup>2</sup> + 2<sup>2</sup> = 68, 6<sup>2</sup> + 8<sup>2</sup> = 100, 1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1. Vi sier også at 0 er et lystig juletall.

Dessverre er ikke disse tallene julete nok til å bestemme hvor mange lys de skal henge på treet på Nordpolen, for fy flate der skal himmelen lyse opp! Alvene pønsker ut en type Jule-3-tall som kan bestemme antall lys på treet deres:

Et tall er et jule-3-tall dersom det er et lystig juletall OG tallets første halvdel av sifre er et lystig juletall OG tallets siste halvdel av sifre er et lystig juletall (dersom tallet har et odde antall sifre inkluderes ikke det midterste tallet) OG alle tallets 3 påfølgende sifre satt sammen er lystige juletall.

Eksempler:

* 1 er åpenbart et jule-3-tall
* 7 er et jule-3-tall fordi det er et lystig juletall (7<sup>2</sup> = 49, 4<sup>2</sup> + 9<sup>2</sup> = 97, 9<sup>2</sup> + 7<sup>2</sup> = 130, 1<sup>2</sup> + 3<sup>2</sup> + 0<sup>2</sup> = 10, 1<sup>2</sup> + 0<sup>2</sup> = 1) og det er ikke nok sifre til at noen av de andre reglene slår inn.
* 70 er et jule-3-tall fordi det er et lystig juletall (7<sup>2</sup> + 0<sup>2</sup> = 49, 4<sup>2</sup> + 9<sup>2</sup> = 97, 9<sup>2</sup> + 7<sup>2</sup> = 130, 1<sup>2</sup> + 3<sup>2</sup> + 0<sup>2</sup> = 10, 1<sup>2</sup> + 0<sup>2</sup> = 1), og samtidig er tallets første halvdel av sifre (bare ```7```) et lystig juletall og tallets siste halvdel av sifre (bare ```0```) et lystig juletall. Det er ikke nok sifre til at regelen om 3 påfølgende sifre slår inn.
* 3100 er et jule-3-tall fordi det er et lystig juletall (3<sup>2</sup> + 1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 10, 1<sup>2</sup> + 0<sup>2</sup> = 1) og samtidig er tallets første halvdel av sifre (```31```) et lystig juletall og tallets siste halvdel av sifre (```00```) et lystig juletall og til slutt er 3-kombinasjonene ```310``` og ```100``` også lystige juletall.
* 13023 er et jule-3-tall fordi det er et lystig juletall (1<sup>2</sup> + 3<sup>2</sup> + 0<sup>2</sup> + 2<sup>2</sup> + 3<sup>2</sup> = 23, 2<sup>2</sup> + 3<sup>2</sup> = 13, 1<sup>2</sup> + 3<sup>2</sup> = 10, 1<sup>2</sup> + 0<sup>2</sup> = 1) og ```13``` er et lystig juletall og ```23``` er et lystig juletall og ```130```, ```302``` og ```023``` er lystige juletall.

# Oppgave
Nissen ønsker seg minst noen millioner lys på treet sitt. Hva er det største jule-3-tallet under ```10 000 000```?