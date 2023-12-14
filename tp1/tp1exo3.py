print("saisir le jour du mois: ")
jour=int(input())
print("sasir une heure: ")
heure=int(input())
print("saisir minute: ")
minute=int(input())
minu = (jour) * 1440 + (heure) * 60 + (minute)
print("Depuis le debut du mois il c'est ecoulé",minu,"minute")

