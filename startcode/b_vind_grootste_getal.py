# Maak een lijst met getallen.
# Schrijf een functie vind_grootste_getal die de grootste waarde uit een lijst teruggeeft.
# Gebruik een for-loop om de grootste waarde te vinden.

def vind_grootste_getal_traag(lijst):
    if(len(lijst)<1):
        print("list too short")
    lijst.sort()
    lijst.reverse()
    print(lijst[0])

def vind_grootste_getal(lijst):
    if(len(lijst)<1):
        print("list too short")
    grootste_getal = lijst[0]
    for item in lijst:
        if item > grootste_getal:
            grootste_getal = item
    print(grootste_getal)
lijst = [12,4,42]
vind_grootste_getal(lijst)