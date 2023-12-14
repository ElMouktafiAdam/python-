from random import randint

x=randint(0,100)
i=0+1

n=int(input("deviner la valeur:"))
while n!=x:
    if n<x:
        n=int(input("essayer avec une valeur superieur : "))

    elif n>x:
        n=int(input("essayer avec une valeur inferieur: "))

print("La valeur était " ,x,)
print("vous avez mis ",i, "tour(s)")

