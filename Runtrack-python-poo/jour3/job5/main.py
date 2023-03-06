class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} ({self.position}, n°{self.numero}):")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()
            print()

    def mettreAJourStatistiquesJoueur(self, nom, buts=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                joueur.buts_marques += buts
                joueur.passes_decisives += passes_decisives
                joueur.cartons_jaunes += cartons_jaunes
                joueur.cartons_rouges += cartons_rouges

# Création joueurs
joueur1 = Joueur("Lionel Messi", 10, "Attaquant")
joueur2 = Joueur("Erling Haaland", 9, "Attaquant")
joueur3 = Joueur("Neymar Jr", 10, "Attaquant")
joueur4 = Joueur("Ryad Mahrez", 26, "Attaquant")

# Création équipes
equipe1 = Equipe("FC Barcelone")
equipe2 = Equipe("Manchester City")

# Ajout des joueurs 
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur4)

# Affichage statistiques joueurs avant match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Simulation du match
joueur1.marquerUnBut()
joueur1.effectuerUnePasseDecisive()
joueur2.recevoirUnCartonJaune()
joueur3.marquerUnBut()
joueur3.marquerUnBut()
joueur4.marquerUnBut()
