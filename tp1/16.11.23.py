Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
nom = 'Adam'
nom = 'El Mouktafi'
prenom = 'Adam'
math = 12
anglais = 11.5
info = 10
promotion = 'RT13'
moy = var ( 12 + 11.5 + 10) / 3
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    moy = var ( 12 + 11.5 + 10) / 3
NameError: name 'var' is not defined. Did you mean: 'vars'?
var = ( 12 + 11.5+ 10 ) / 3
var
11.166666666666666
moy = var
moy
11.166666666666666
print (" je m'appelle {nom} {prenom}, je suis en {promotion} , j'ai eux {math} en math , {anglais} en anglais et {info} en info , ma moyenne est de {moy}")
 je m'appelle {nom} {prenom}, je suis en {promotion} , j'ai eux {math} en math , {anglais} en anglais et {info} en info , ma moyenne est de {moy}
nom
'El Mouktafi'
moy
11.166666666666666
math =13
var = math +  anglais
var
24.5
var = ( math + anglais + info ) / 3
var
11.5
moy = var
moy
11.5
11.5
11.5
moy = ( math + anglais + info ) / 3
moy
11.5
type (math)
<class 'int'>
print (math)
13
print (" je m'appelle {nom} {prenom}, je suis en {promotion} , j'ai eux {math} en math , {anglais} en anglais et {info} en info , ma moyenne est de {moy}")
 je m'appelle {nom} {prenom}, je suis en {promotion} , j'ai eux {math} en math , {anglais} en anglais et {info} en info , ma moyenne est de {moy}
>>> print (" je m'appelle (nom) (prenom), je suis en (promotion) , j'ai eux {math} en math , {anglais} en anglais et {info} en info , ma moyenne est de {moy}")
 je m'appelle (nom) (prenom), je suis en (promotion) , j'ai eux {math} en math , {anglais} en anglais et {info} en info , ma moyenne est de {moy}
>>> je m'appelle (nom) (prenom), je suis en (promotion) , j'ai eux {math} en math , {anglais} en anglais et {info} en info , ma moyenne est de {moy}
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> nom = 'toto'
>>> prenom = 'titi'
>>> promotion = 2023
>>> moy = 12.5
>>> print(" L'etudiant {nom}, {prenom}, de la promotion, {promotion} a une moyenne de ,{moy} ")
 L'etudiant {nom}, {prenom}, de la promotion, {promotion} a une moyenne de ,{moy} 
>>> f(" L'etudiant {nom}, {prenom}, de la promotion, {promotion} a une moyenne de ,{moy} ")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    f(" L'etudiant {nom}, {prenom}, de la promotion, {promotion} a une moyenne de ,{moy} ")
NameError: name 'f' is not defined
>>> f" L'etudiant {nom}, {prenom}, de la promotion, {promotion} a une moyenne de ,{moy} "
" L'etudiant toto, titi, de la promotion, 2023 a une moyenne de ,12.5 "
>>> " L'etudiant toto, titi, de la promotion, 2023 a une moyenne de ,12.5 "
" L'etudiant toto, titi, de la promotion, 2023 a une moyenne de ,12.5 "
>>> 
>>> jour = 16
>>> heure = 09
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> heure = 9
>>> minite = 22
