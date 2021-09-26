#
# Fichier d'exemple pour les classes for working with classes
#


#Class avec COnstructeur


class Velo:
    "Ceci est une classe qui permet d'instancier un velo"
    roues = 2

    def __init__(self, marque, prix, poids=3.5):
        self.marque = marque
        self.prix = prix
        self.poids = poids

    def rouler(self):
        print("Nous roulons sur un velo {}".format(self.marque))
    
    def lampe():
        print("Lampe allumée")
    
    def __str__(self):
        return "Velo de marque {} coutant {}, pesant {} et ayant {} roues".format(self.marque, self.prix, self.poids, self.roues)
    

#### Exercice Rectangle
    
class Rectangle():
    "Classe Rectangle"
    def __init__(self, longueur = 0, largeur = 0):
        self.longueur = int(longueur)
        self.largeur = int(largeur)
        self.nom = "Rectangle"
    
    def perimetre(self):
        return (self.longueur + self.largeur) * 2
    
    def surface(self):
        return self.longueur * self.largeur
    
    def mesures(self):
        return "Un {} de longueur {} et de largeur {}".format(self.nom, self.longueur, self.largeur)


class Carre(Rectangle):
    "Class de carrés"
    def __init__(self, cote):
        Rectangle.__init__(self, cote, cote)
        self.nom = "Carré"


    

def main():
    x1 = Rectangle(5,4)
    print(x1.mesures())
    

    print(isinstance(x1, Rectangle))
    print(issubclass(int, Rectangle))

if __name__ == "__main__":
    main()

