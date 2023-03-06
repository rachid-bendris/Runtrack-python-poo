def calculer_puissance(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        racine = calculer_puissance(x, n//2)
        return racine * racine
    else:
        racine = calculer_puissance(x, (n-1)//2)
        return x * racine * racine

x = int(input("Entrez un nombre entier : "))
n = int(input("Entrez la puissance : "))
print(x, "puissance", n, "est égal à", calculer_puissance(x, n))
