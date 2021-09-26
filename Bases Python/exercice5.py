


# 1. Définissez une classe Cercle(). Les objets construits à partir de cette classe seront des cercles de tailles variées. En plus de la méthode constructeur (qui utilisera donc un paramètre rayon), vous définirez une méthode surface(), qui devra renvoyer la surface du cercle.
# Définissez ensuite une classe Cylindre() dérivée de la précédente. Le constructeur de cette nouvelle classe comportera les deux paramètres rayon et hauteur. Vous y ajouterez une méthode volume() qui devra renvoyer le volume du cylindre (rappel : volume d’un cylindre = surface de section × hauteur).

# Exemple d’utilisation de cette classe :
# >>> cyl = Cylindre(5, 7)
# >>> print(cyl.surface())
# 78.54
# >>> print(cyl.volume())
# 549.78

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def surface(self):
        return 3.14 * (self.rayon ** 2)

class Cylindre(Cercle):
    
    def __init__(self, rayon, hauteur):
        self.hauteur = hauteur
        Cercle.__init__(self, rayon)
        
    
    def volume(self):
        return self.surface() * self.hauteur




def main():
    c1 = Cylindre(5,10)
    print(c1.surface())


if __name__ == "__main__":
    main()