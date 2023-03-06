def calculer_factorielle(n):
    if n == 0:
        return 1
    else:
        return n * calculer_factorielle(n-1)

nombre = int(input("Entrez un nombre entier : "))
print("La factorielle de", nombre, "est", calculer_factorielle(nombre))
