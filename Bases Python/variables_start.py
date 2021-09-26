# 
# Fichier d'exemple pour les variables
#

# Declarer une variable et l'initialiser

#Integer
a = 3
print(a)



#Float
b = 3.7
print(b)


#String
nom = "Hermine Lilou"
print(nom)


un_string = '''
Je crois que je suis concentré!
'''
print(un_string)

autre_string = "Hermine \n, Pascaline"
print(autre_string)


# La re-declaration des variables est possible
a = "Je suis un string"
print(a)


#Obtenir le type d'une variable
type(a)
type(autre_string)

#Caster
str(3) #Transformer un nombre 3 en string "3"
int("3")
float("5.3")
bool("True")


# Erreur: Les variables des types différents ne peuvent être combinées

#print ("string type " + 123)
print ("string type " + str(123))


#Operations sur le string
texte1 = "Je suis un developpeur python"

## Concatenation
texte2 = " et j'en suis fière"
texte3 = texte1 + texte2
print("texte Concatené", texte3)

##longueur de la chaine
len(texte1)

## Split Chaine
res = texte1.split(" ")
print(res)


#Mettre texte en majuscule
texte1 = texte1.upper()
texte1.

##Mettre texte en miniscule
texte1 = texte1.lower()

##Remplacer un element dans le texte
texte1 = texte1.replace(" ", "-")



#Collections

#Déclarer une list avec la possibilité de modifier son contenu


# J'accède au 7e élément de la liste (les index commencent à 0)

# Je retire le 5e élément de la liste

# J'ajoute un élément à la fin


#Ou


# J'extrais les éléments de la position 3 jusqu'au bout


# J'extrais les deux premiers éléments


# J'extrais les éléments de la position 4 à 6 (les index commencent à 0)


# Quelle est la longueur de ma liste ?

# Je modifie un élément (celui qui est en 3e position !)

#Serie de fonction


#Copier une liste
##Copie par référence

##Copie par valeur


#Transformation String en liste


#Transformation liste en string


#Extension de liste  



#Déclarer un tuple sans la possibilité de modifier son contenu

#J'accède au 7e élément de la liste (les index commencent à 0)



#On peut pas modifier un tuple




#SET

#Construire un dictionnaire

#Un autre dictionnaire


#Accéder à la valeur rattaché à la clé Nom


#Accéder à la valeur rattaché à la clé Instrument

#Enregistrer un nouvel ensemble clé valeur

#Accéder à une liste dans un dictionnaire


#Effacer une clé et la valeur qui lui est associée


#Récupérer une valeur depuis sa clé



#Supprimer une entrée


#Récupérer la listes des clés


#Récupérer la listes des valeurs



#Récupérer la listes des clés/valeurs




#Copier un dictionnaire par référene


#Copier un dictionnaire par valeur







# Variables locales vs variables globales

def someFunction():
  pass


#Mutiples variables
