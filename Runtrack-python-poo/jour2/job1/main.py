class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def get_longueur(self):
        return self.__longueur
        
    def set_longueur(self, longueur):
        self.__longueur = longueur
        
    def get_largeur(self):
        return self.__largeur
        
    def set_largeur(self, largeur):
        self.__largeur = largeur
        
    def calculer_aire(self):
        return self.__longueur * self.__largeur

mon_rectangle = Rectangle(10, 5)

print("Dimensions initiales : longueur =", mon_rectangle.get_longueur(), "largeur =", mon_rectangle.get_largeur())

mon_rectangle.set_longueur(19)
mon_rectangle.set_largeur(10)

print("Dimensions modifiées : longueur =", mon_rectangle.get_longueur(), "largeur =", mon_rectangle.get_largeur())

aire = mon_rectangle.calculer_aire()
print("Aire du rectangle :", aire)
