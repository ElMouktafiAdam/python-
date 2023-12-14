#question a

"""
x=0
n=int(input(" Donnez une valeur : "))
for i in range (n+1):
    x+=i
print("La somme d'eentiers de 0 a",n,"inclut est",x, )

"""

#question b

"""
n=int(input("Merci de saisir un nombre"))
while n!=100:
    n=int(input("donnez une autre valeur: "))
"""

"""
x=0
y=0
n=int(input("Donnez une valeur entre 0 et 20 : "))
while y != 10:
    if n>=0 and n<=20:
        y+=1
        if n<10:
            a+=1
        elif n>=10 and n<=15:
            b+=1
        elif n=>15:
            c+=1
print("Le nomre de valeur inférieur strictement a 10 est" ,a,)
print("Le nomre de valeur supérieur ou égale a 10 et inferieur a 15 est" ,b,)
print("Le nomre de valeur superieur ou égale a 15 est" ,c,)
"""

#question d
x=int(input("Dooner un nombre : "))
while x<1 :
    x = int(input("donner un plus grand que 1: "))
n=0
i=0
while n <= x :
        i+=1
        n=n+1
if i==x:
    print("le nombre chercher est:" ,i,)
elif i>x:
    print("le nombre chercher est:" ,i-1)

