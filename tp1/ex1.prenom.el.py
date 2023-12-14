nom = 'El Mouktafi'
prenom = 'Adam'
math = 12
anglais = 11.5
info = 10
promotion = 'RT13'
moy = ( math + anglais + info ) / 3

print (type (nom))
print (type (prenom))
print (type (math))
print (type (anglais))
print (type (info))
print (type (promotion))
print (type (moy))
print (f"L'etudiant {nom} {prenom}, de la promotion {promotion} a une moyenne de {moy}")
print ("L'etudiant {} {}, de la promotion {} a une moyenne de {:.2f}".format (nom, prenom ,promotion, moy))
 (
