a=int(input("entrz un nombre entier"))
b=a%2
if a>0 and b==0:
    print("Le nombrre est positif et pair")
elif a>0 and b!=0 :
    print("Le nombrre est positif et impair")
elif a<0 and b==0 :
    print("Le nombrre est positif et pair")
elif a<0 and b!=0 :
    print("Le nombrre est positif et impair")
else:
    print("Le nombre est zéro et il est pair")


