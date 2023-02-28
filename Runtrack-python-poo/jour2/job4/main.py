class Student:
    def __init__(self, nom, prenom, num_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = credits
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()
        else:
            print("Le crédits doit être supérieur à zéro.")

    def get_credits(self):
        return self.__credits

john_doe = Student("Doe", "John", 145)
john_doe.add_credits(10)
john_doe.add_credits(10)
john_doe.add_credits(10)



print("Crédits", john_doe._Student__prenom, john_doe._Student__nom, ":", john_doe.get_credits())
