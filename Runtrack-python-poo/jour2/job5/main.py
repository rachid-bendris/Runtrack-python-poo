class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.en_marche = False
        self.reservoir = 50
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        

    def demarrer(self):
        if self.verifier_plein():
            self.en_marche = True
            print("Démarrage.")
        else:
            print("Le réservoir est vide.")

    def arreter(self):
        self.en_marche = False
        print("La voiture s'arrête.")

    def verifier_plein(self):
        if self.reservoir > 5:
            return True
        else:
            return False

    def get_marque(self):
        return self.marque

    def set_marque(self, marque):
        self.marque = marque

    def get_modele(self):
        return self.modele

    def set_modele(self, modele):
        self.modele = modele

    def get_annee(self):
        return self.annee

    def set_annee(self, annee):
        self.annee = annee

    def get_kilometrage(self):
        return self.kilometrage

    def set_kilometrage(self, kilometrage):
        self.kilometrage = kilometrage

    def get_en_marche(self):
        return self.en_marche

    def set_en_marche(self, en_marche):
        self.en_marche = en_marche

    def get_reservoir(self):
        return self.reservoir

    def set_reservoir(self, reservoir):
        self.reservoir = reservoir

ma_voiture = Voiture("bmw", "i8", 2014, 30000)

print(ma_voiture.get_kilometrage()) 

ma_voiture.set_kilometrage(30500)

ma_voiture.demarrer() 

print(ma_voiture.get_en_marche()) 

ma_voiture.arreter() 

print(ma_voiture.get_reservoir()) 

ma_voiture.demarrer() 

ma_voiture.set_reservoir(3)

ma_voiture.demarrer() 
 
