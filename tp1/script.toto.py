nom = 'toto'
prenom = 'titi'
promotion = '2023'
moy = 12

print ("Les variables sont:")
print (type (nom))
print (type (prenom))
print (type (promotion))
print (type (moy))
print (f"L'etudiant {nom} {prenom}, de la promotion {promotion} a une moyenne de {moy}")
print ("L'etudiant {} {}, de la promotion {} a une moyenne de {:.2f}".format (nom, prenom ,promotion, moy))

