class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(f"({self.x}, {self.y})")
    
    def afficherX(self):
        print(f"{self.x}")
    
    def afficherY(self):
        print(f"{self.y}")
    
    def changerX(self, x):
        self.x = x
    
    def changerY(self, y):
        self.y = y
