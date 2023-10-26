BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives= int(input("entrer le nombre de convives:"))

nouvelleQuantiteFromage = fromage * nbConvives / BASE
nouvelleQuantiteEau = eau * nbConvives / BASE
nouvelleQuantiteAil = ail * nbConvives / BASE
nouvelleQuantitePain = pain * nbConvives / BASE

print(f"Recette pour {nbConvives} convives:")
print(f"Fromage: {nouvelleQuantiteFromage} grammes")
print(f"Eau: {nouvelleQuantiteEau} décilitres")
print(f"Ail: {nouvelleQuantiteAil} gousses")
print(f"Pain: {nouvelleQuantitePain} grammes")
