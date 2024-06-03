
import csv
from presentatie import *

with open('boekhouding.csv’, 'w',newline='') as csvfile:
     for key, value in inkomsten.items():
     writer = csv.writer(csvfile, delimiter=';')
     writer.writerow([key,value])

inkomsten = {  
    "Aardbeien-ijs-totaal" : 1000,  
    "Vanille-ijs-totaal" : 2000,  
    "Chocolade-ijs-totaal" : 1500,  
    "waterijsjes-totaal" : 750,  
}

values, totaal_inkomsten = som(inkomsten)

print()
resultaat = presenteer(inkomsten, totaal_inkomsten)
