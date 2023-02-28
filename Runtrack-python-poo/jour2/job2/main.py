class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
    
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre
    
    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
    
    def get_nb_pages(self):
        return self.__nb_pages
    
    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur")
    
    def afficher_livre(self):
        print("Titre :", self.__titre)
        print("Auteur :", self.__auteur)
        print("Nombre de pages :", self.__nb_pages)


livre1 = Livre("robinson", "Crusaué", 1745)

livre1.afficher_livre()   
livre1.set_titre("dark night")
livre1.set_nb_pages(350)
livre1.afficher_livre()   
livre1.set_nb_pages(-100)   


