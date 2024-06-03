
import csv
from presentatie import *



inkomsten = {  
    "Aardbeien-ijs-totaal" : 1000,  
    "Vanille-ijs-totaal" : 2000,  
    "Chocolade-ijs-totaal" : 1500,  
    "waterijsjes-totaal" : 750,  
}

values, totaal_inkomsten = som(inkomsten)

print()
resultaat = presenteer(inkomsten, totaal_inkomsten)


with open('boekhouding.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for key, value in inkomsten.items():
       writer.writerow([key,value])
