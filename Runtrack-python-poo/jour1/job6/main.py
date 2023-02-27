class Animal:
    def __init__(self):
        self.age = 0
        self.nom = ""

    def vieillir(self):
        self.age += 1


    def nommer(self, nom):
        self.nom = nom

mon_animal = Animal()
mon_animal.vieillir()
mon_animal.nommer("")


print("Age initial de l'animal :", mon_animal.age)

print("Age actualisé de l'animal :", mon_animal.age)

print("Nom de l'animal :", mon_animal.nom)

