jour= 0
heure = 0
minute = 0
minute = 0
print("saisir un nombre de minute : ")
minute = int(input())
jour = minute // 1440
minute = minute %1440
heure = minute // 60
minute = minute% 60
print(jour,heure,minute)