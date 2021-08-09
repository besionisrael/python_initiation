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

##Mettre texte en miniscule
texte1 = texte1.lower()

##Remplacer un element dans le texte
texte1 = texte1.replace(" ", "-")



#Collections

#Déclarer une list avec la possibilité de modifier son contenu
list_data = [1, 2, 3, 4]

#Déclarer un tuple sans la possibilité de modifier son contenu
tuple_data = (1, 2, 3, 4)

#Construire un dictionnaire
dico = {}
dico['computer'] = 'ordinateur'
dico['mouse'] ='souris'
dico['keyboard'] ='clavier'
print("dico")
dico = {'computer': 'ordinateur', 'keyboard': 'clavier', 'mouse': 'souris'}



# Variables locales vs variables globales

def someFunction():
  #global a
  a = "deal"
  print (a)



#Mutiples variables
a,b = 7, "Je suis là"
print("a", a)
print("b", b)