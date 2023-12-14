from time import *
Nombre=float(input("enter un chiffre : "))
table=[]
for i in range ( 0 , 10):
    r= Nombre * i
    Arrondi = round(r,2)
    table.append(Arrondi)
for i in range (0,10):
    print(Nombre ,"*",i,"=",table[i])



