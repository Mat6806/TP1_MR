    jour = 0
    heure = 0
    minute = 0
    print("saisir un jour")
    jour = int(input())
    print("saisir une heure")
    heure = int(input())
    print("saisir une minute")
    minute = int(input())
    calc = (heure * 60 + minute) + jour * 60 * 24
    print(calc)
