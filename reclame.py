from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van  {prijs} euro, voor {korting} euro"
    return uitvoer

print(aanbieding_1("aardbij", 4, 4 * 0.1))

daginkomsten = [220, 430, 125, 160, 205, 90, 345]

def inkomsten_totaal(inkomsten, btw):
   totaal_inkomsten = sum(inkomsten)
   belasting = (totaal_inkomsten * btw)
   uitvoer2 = f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {belasting} euro btw betaald dient te worden."
   return uitvoer2

print (inkomsten_totaal(daginkomsten, 0.09))

def laag_en_hoog(mijn_lijst):
    laag = min(mijn_lijst)
    hoog = max(mijn_lijst)
    mijn_lijst = [laag, hoog]
    return mijn_lijst


print (laag_en_hoog(daginkomsten))

def gemiddelde(mijn_lijst):
    totaal_inkomsten = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    avg = int(totaal_inkomsten / aantal)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {avg} euro"
    return uitvoer


print (gemiddelde(daginkomsten))

int_lijst = [10,5,3,2,1,2,9]

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)


print (meervoudig(int_lijst))

def combinatie(invoer_lijst_2):
 korte_lijst = laag_en_hoog(invoer_lijst_2)
 uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
 return uitvoer

print (combinatie(int_lijst))