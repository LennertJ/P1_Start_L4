lijst = []
print("geef je 3 favoriete dieren, 1 dier per keer.")

for i in range(3):
    dier = input("Dier " + str(i+1) + ": ")
    lijst.append(dier)
print(lijst)