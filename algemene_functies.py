def mijn_functie_1(a):
    return a * a

teruggeefwaarde = []

for i in range (2, 14, 2):
    totaal = mijn_functie_1(i)
    teruggeefwaarde.append(totaal)

teruggeefwaarde = teruggeefwaarde[:2] + teruggeefwaarde[4:]

print(teruggeefwaarde)

argumenten = []

def mijn_functie_2(a,b):
    plus = a + b
    min = a - b
    keer = a * b
    gedeeld = int (a/b)
    return plus, min, keer, gedeeld
    
argument1 = mijn_functie_2(12,3)
argument2 = mijn_functie_2(12,2)
argument3 = mijn_functie_2(10,5)
argument4 = mijn_functie_2(100,20)

print(argument1)
print(argument2)
print(argument3)
print(argument4)