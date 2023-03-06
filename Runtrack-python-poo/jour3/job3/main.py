class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"
        
    def marquer_comme_finie(self):
        self.statut = "terminée"
        
    def __repr__(self):
        return f"Tache({self.titre}, {self.description}, {self.statut})"

class ListeDeTaches:
    def __init__(self):
        self.taches = []
        
    def ajouter_tache(self, tache):
        self.taches.append(tache)
        
    def supprimer_tache(self, tache):
        self.taches.remove(tache)
        
    def marquer_comme_finie(self, tache):
        tache.marquer_comme_finie()
        
    def afficher_liste(self):
        for tache in self.taches:
            print(tache)
            
    def filter_liste(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]

# Exemple d'utilisation
tache1 = Tache("Faire du sport", "Aller a la piscine, Bien s'alimenter")
tache2 = Tache("S'éduquer finacièrement", "Apprendre de son mentor")
tache3 = Tache("Aller en cours", "Faire ces 35 heures a la plat")

liste_de_taches = ListeDeTaches()
liste_de_taches.ajouter_tache(tache1)
liste_de_taches.ajouter_tache(tache2)
liste_de_taches.ajouter_tache(tache3)

# les tâches
liste_de_taches.afficher_liste()

# les tâches à faire
taches_a_faire = liste_de_taches.filter_liste("à faire")
print(taches_a_faire)

# tâche terminée
liste_de_taches.marquer_comme_finie(tache1)

# réafficher toutes les tâches
liste_de_taches.afficher_liste()

# Supprimer une tâche
liste_de_taches.supprimer_tache(tache3)

# réafficher toutes les tâches
liste_de_taches.afficher_liste()
