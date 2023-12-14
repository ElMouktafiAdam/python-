
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
notes=[]
for i in range(nombreEtudiants):
    notes.append(float(input(f"\nNote etudiant {i} : ")))
    while notes[i]<0 or notes[i]>20:
        notes.pop()
        notes.append((float(input(f"Note etudiant {i} "))))
    moyenne=notes[i]
moyenne/=len(notes)
print(f"\nMoyenne de classe : ,(moyenne)\n")
print(f"Numéro de l'étudiant | note | ecart a la moyenne\n")
for i in range(len(notes)):
    print(i,"|",notes[i], "|" ,notes[i]-moyenne,)
    
