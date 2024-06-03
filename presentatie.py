
from helper import onderstreep, som

mijn_dict = {
    "vis" : 10, 
    "vlees": 25, 
    "overig" : 15,
    }


values, totaal = som(mijn_dict)

def presenteer(dictionary, totaal):
    for sleutel, waarde in dictionary.items():
     print(f"{sleutel} : {waarde} euro")
     
    totaalstring = f"totaal : {totaal} euro"
    
    opmaak = onderstreep(totaalstring)
    
    for line in opmaak:
        print(line)
    
    return dictionary, totaal, opmaak, totaalstring

uitvoer = presenteer(mijn_dict, totaal)