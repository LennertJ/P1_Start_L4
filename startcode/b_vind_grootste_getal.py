# Maak een lijst met getallen.
# Schrijf een functie vind_grootste_getal die de grootste waarde uit een lijst teruggeeft.
# Gebruik een for-loop om de grootste waarde te vinden.
lijst = [1,12,42,13,6]

def vind_hoogste_getal_traag(lijst):
    lijst.sort()
    lijst.reverse()
    print(lijst[0])

def vind_hoogste_getal(lijst):
    hoogste_getal = lijst[0]
    for item in lijst:
        if item > hoogste_getal:
            hoogste_getal = item
    print(hoogste_getal)
vind_hoogste_getal(lijst)