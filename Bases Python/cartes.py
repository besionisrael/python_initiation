

from random import randrange

class JeuDeCartes:
    
    #couleur = ('Pique', 'Trèfle', 'Carreau', 'Coeur')
    couleur = ('Coeur','Carreau','Trèfle', 'Pique')
    valeur = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,'valet', 'dame', 'roi', 'as')

    def __init__(self):
        self.cartes = []
        for x in range(0,4): #Couleur
            for y in range(2,15): #Valeur
                self.cartes.append((y,x))
    

    def nom_carte(self, c):
        #c[0] c[1] (14,3)
        return "{} de {}".format(self.valeur[c[0]], self.couleur[c[1]])
    
    def battre(self):
        nbr = len(self.cartes)
        for i in range(nbr):
            position1, position2 = randrange(nbr), randrange(nbr)
            self.cartes[position1], self.cartes[position2] = self.cartes[position2], self.cartes[position1]
    
    
    def tirer(self):
        nbr = len(self.cartes)
        if nbr > 0:
            return self.cartes.pop(0)
        else:
            return None


class Test:
    "pass"
    def __init__(self):
        self.nom = ""

if __name__ == "__main__":
    jeu = JeuDeCartes()
    jeu.battre()
    for n in range(53):
        c = jeu.tirer()
        if not c:
            print("Terminé")
        else:
            print(jeu.nom_carte(c))