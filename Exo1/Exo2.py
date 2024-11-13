ficher = "texte.txt"

try:
    with open(ficher, 'r') as f:
        for ligne in f:
            print(ligne.rstrip(""))
except FileNotFoundError : 
    print("Erreur le fichier est introvable")
except IOError: 
    print("Erreur probleme d'acces au fichier")
except FileExistsError: 
    print("Erreur le fichier exist déjà")
except PermissionError : 
    print("Erreur acces au fichier interdit")
finally:
    print("fin du programme")