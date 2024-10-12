lijst = []
input_dier = ""
print("kies je 3 favoriete dieren, 1 per keer:")
for i in range(3):
    input_dier = input("dier " + str(i+1))
    lijst.append(input_dier)
print(lijst)