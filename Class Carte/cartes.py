# Définissez une classe JeuDeCartes() permettant d’instancier des objets dont le 
# comportement soit similaire à celui d’un vrai jeu de cartes. La classe devra 
# comporter au moins les quatre méthodes suivantes :

# • méthode constructeur : création et remplissage d’une liste de 52 éléments, 
# qui sont eux-mêmes des tuples de 2 entiers. Cette liste de tuples contiendra 
# les caractéristiques de chacune des 52 cartes. Pour chacune d’elles, il faut en 
# effet mémoriser séparément un entier indiquant la valeur (2, 3, 4, 5, 6, 7, 8, 9, 
# 10, 11, 12, 13, 14, les 4 dernières valeurs étant celles des valet, dame, roi et as), 
# et un autre entier indiquant la couleur de la carte (c’est-à-dire 3,2,1,0 pour Coeur, 
# Carreau, Trèfle et Pique).

# Dans une telle liste, l’élément (11,2) désigne donc le valet de Trèfle, et 
# la liste terminée doit être du type :
# [(2, 0), (3,0), (3,0), (4,0), ..... (12,3), (13,3), (14,3)] 

# • méthode nom_carte() : cette méthode doit renvoyer, sous la forme d’une chaîne, l’identité
# d’une carte quelconque dont on lui a fourni le tuple descripteur en argument. 
# Par exemple,# l’instruction : 
# print(jeu.nom_carte((14, 3))) doit provoquer l’affichage de : As de pique

# • méthode battre() : comme chacun sait, battre les cartes consiste à les mélanger.  
# Cette méthode sert donc à mélanger les éléments de la liste contenant les cartes, 
# quel qu’en # soit le nombre. 
# • méthode tirer() : lorsque cette méthode est invoquée, une carte est retirée du jeu.
#  Le tuple contenant sa valeur et sa couleur est renvoyé au programme appelant. 
# On retire toujours la première carte de la liste. Si cette méthode est invoquée alors
#  qu’il ne reste plus aucune carte dans la liste, il faut alors renvoyer l’objet 
# spécial None au programme appelant.


from random import randrange


class JeuDeCartes():
    "Classe jeu de cartes"
    couleur = ('Pique', 'Trèfle', 'Carreau', 'Coeur')
    valeur = (0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'valet', 'dame', 'roi', 'as')
        

    def __init__(self):
        "Construction de la liste des 52 cartes"
        self.carte =[]
        for coul in range(4):
            for val in range(13):
                self.carte.append((val +2, coul)) # la valeur commence à 2
    
    def nom_carte(self, c):
        "Renvoi du nom de la carte c, en clair"
        return "{0} de {1}".format(self.valeur[c[0]], self.couleur[c[1]])
    
    def battre(self):
        "Mélange des cartes"
        t = len(self.carte) # nombre de cartes restantes
        # pour mélanger, on procède à un nombre d'échanges équivalent :
        for i in range(t):
            # tirage au hasard de 2 emplacements dans la liste :
            h1, h2 = randrange(t), randrange(t)
            # échange des cartes situées à ces emplacements :
            self.carte[h1], self.carte[h2] = self.carte[h2], self.carte[h1]
    
    def tirer(self):
        "Tirage de la première carte de la pile"
        t = len(self.carte) # vérifier qu'il reste des cartes
        if t >0:
            carte = self.carte[0] # choisir la première carte du jeu
            del(self.carte[0]) # la retirer du jeu
            return carte # en renvoyer copie au prog. appelant
        else:
            return None # facultatif


if __name__ == "__main__":
    jeu = JeuDeCartes() # instanciation d'un objet
    print(jeu.carte)
    # jeu.battre() # mélange des cartes
    # for n in range(53): # tirage des 52 cartes :
    #     c = jeu.tirer()
    #     if c == None: # il ne reste plus aucune carte
    #         print('Terminé !') # dans la liste
    #     else:
    #         print(jeu.nom_carte(c)) # valeur et couleur de la carte
