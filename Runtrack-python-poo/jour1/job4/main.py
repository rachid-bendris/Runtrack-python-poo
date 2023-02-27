class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return f"Je m'appelle {self.nom} {self.prenom}"

personne1 = Personne("Beakman", "Ben")
print(personne1.SePresenter())  

personne2 = Personne("Snow", "Jhon")
print(personne2.SePresenter())  
