class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants
    
    def set_nb_habitants(self, nb_habitants):
        self.__nb_habitants = nb_habitants

    
    def get_nb_habitants(self):
        return self.__nb_habitants
    
    def get_nom(self):
        return self.__nom
    
    
    
    

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
    
    def get_nom(self):
        return self.__nom
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville
    
    def ajouterPopulation(self):
        nb_habitants = self.__ville.get_nb_habitants()
        self.__ville.set_nb_habitants(nb_habitants + 1)


# Création de deux villes
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage de Paris et de Marseille
print(f"Nombre d'habitants à {paris.get_nom()} : {paris.get_nb_habitants()}")
print(f"Nombre d'habitants à {marseille.get_nom()} : {marseille.get_nb_habitants()}")

#Trois nouvelles personnes
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Ajout des personnes 
john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

# Affichage après l'arrivée des nouvelles personnes
print(f"Nombre d'habitants à {paris.get_nom()} : {paris.get_nb_habitants()}")
print(f"Nombre d'habitants à {marseille.get_nom()} : {marseille.get_nb_habitants()}")

