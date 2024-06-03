
def decoreer(tekst=""):
 tekst="header"
 lengte = len(tekst) + 4
 print()
 print(lengte * "*")
 print(f"* {tekst} *")
 print(lengte * "*")
 print()


def fooi_pp(bedrag, personen):    
    bedrag_pp = bedrag/personen    

def onderstreep(tekst=""):
 uit = []
 uit.append(len(tekst) * "=")
 uit.append(tekst)
 return uit

def som(mijn_dictionary):
    values = list(mijn_dictionary.values())
    totaal = sum(values)
    return values, totaal