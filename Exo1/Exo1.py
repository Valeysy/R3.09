def divEntier(x: int, y: int) -> int:
        if y == 0:
            raise ValueError("Le diviseur ne peut pas être 0")   
        if y <= 0:
            raise ValueError("Le diviseur ne peut pas être négatif")   
        if x < y:
            return 0
        else:
            x = x - y
            return divEntier(x, y) +  1     
    
def main():
    try:
        x = int(input("Entrez un nombre entier : "))
        y = int(input("Entrez un nombre entier : "))
        result = divEntier(x, y)
        print(f"Le quotient de {x} et de {y} est {result}")
    except ValueError as e:
        print(f"Erreur : {e}")

main()