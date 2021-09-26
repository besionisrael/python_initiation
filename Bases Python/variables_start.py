# 
# Fichier d'exemple pour les variables
#

# Declarer une variable et l'initialiser

#Integer




#Float



#String



# La re-declaration des variables est possible



#Obtenir le type d'une variable
a = 15
type(a)

#Caster
str(a)
int(a)
float(a)

# Erreur: Les variables des types différents ne peuvent être combinées

#print ("string type " + 123)



#Operations sur le string


## Concatenation


##longueur de la chaine


## Split Chaine


#Mettre texte en majuscule


##Mettre texte en miniscule


##Remplacer un element dans le texte




#Collections

#Déclarer une list avec la possibilité de modifier son contenu
# maliste = [0, 1, 1, 2, 2, 3, 5, 8, 13]
# maliste2 = [1, "Henry", "Paul"]
# print(type(maliste))
# print(type(maliste2))

# J'accède au 7e élément de la liste (les index commencent à 0)
# print(maliste[6])

# Je retire le 5e élément de la liste
# maliste.pop(4)
# print(maliste)

# J'ajoute un élément à la fin
# maliste.append(21)
# print(maliste)
# print(maliste2)
# texte1 = "Texte 1"
# texte2 = texte1.replace(" ", "-")
# print(texte1, texte2)

maliste3 = [[1,2], 3, 4]
# print(maliste3)
# print(maliste3[0])
# print(maliste3[0][1])


# J'extrais les éléments de la position 3 jusqu'au bout
# print("ma liste", maliste)
# print("extraction", maliste[2:])


# J'extrais les deux premiers éléments
# print(maliste[:2])


# J'extrais les éléments de la position 4 à 6 (les index commencent à 0)
# print(maliste[3:5])



# Quelle est la longueur de ma liste ?
# print(len(maliste))
# texte1 = "Ceci est une chaine"
# print("accès elt 2", texte1[1])
# print("extraire", texte1[3:])
# print("longueur", len(texte1))

# Je modifie un élément (celui qui est en 3e position !)
# maliste[0] = 300
# maliste[2] = 200
# print(maliste)

#Serie de fonction


#Copier une liste
##Copie par référence
x = [0, 1, 1, 2, 3, 5, 8, 13]
y = x 


##Copie par valeur

m = [1, 2, 3]
n = m[:]

#Transformation String en liste
ma_chaine = "Nicolas,Patrick,Henry"
print(ma_chaine.split(","))



#Transformation liste en string
ma_liste = ["Nicolas", "Paul", "Gemima"]
res = "-".join(ma_liste)
print(res)


#Extension de liste  
# ma_liste2 = ["Jerome", "Amine"]
# ma_liste.extend(ma_liste2)
# print(ma_liste)
# print(ma_liste.index("Jerome"))

texte1 = "Ceci est un texte"
#print(texte1.index("m"))




#Déclarer un tuple sans la possibilité de modifier son contenu
mon_tuple = (0, 1, 1, 2, 2, 3, 5, 8, 13)
print(mon_tuple)
print(type(mon_tuple))


#J'accède au 7e élément de la liste (les index commencent à 0)
print(mon_tuple[6])


#On peut pas modifier un tuple
#mon_tuple[2] = 100



#SET
# liste_avec_doublons = ["pascal", 'pierre', 'paul', 'pierre', 'paul', 'pierre', 'pascal', 'Hermine']
# print(liste_avec_doublons)
# set_liste = set(liste_avec_doublons)

# print(set_liste)
# print(list(set_liste))
# print(type(set(liste_avec_doublons)))


#Construire un dictionnaire
dico = {}
dico["computer"] = "Ordinateur"
dico["mouse"] = "souris"
print("mon dictionnaire", dico)

print(dico["computer"])
print(maliste3[1])

dico2 = {'computer': "Hp", "mouse": "Compac", "duree":15}
#print(dico2[1])

#Un autre dictionnaire

dico_total = {
    "Johnny":{
            "nom": "Johnny",
            "prenom": "Jean",
            "age": 15,
            "activites": ["manger", "jouer"]
            },
    "Berti":{
            "nom": "Johnny",
            "prenom": "Jean",
            "age": 15,
            "activites": ["manger", "jouer"]
            }
}


berti = { 
        'nom': 'Bertignac', 
        'prenom': 'Louis', 
        'instruments': ['guitare', 'piano'],
        'concerts':
            {
                'opera': "Opera Test",
                'chanteur': ["Presley", "Beattles"]
            } 
        }
# print(berti)
# print(berti["nom"])
# print(berti["instruments"][0])
# print(berti["concerts"]["chanteur"][1])

#Accéder à la valeur rattaché à la clé Nom
print(berti["nom"])

#Accéder à la valeur rattaché à la clé Instrument
print("Instrument", berti["instruments"])

#Enregistrer un nouvel ensemble clé valeur
berti["groupes"] = ["Telephone", "Fax"]
print("ajout",berti)


#Accéder à une liste dans un dictionnaire
print(berti["instruments"][0])

#Effacer une clé et la valeur qui lui est associée
del berti['concerts']
print(berti)

#Récupérer une valeur depuis sa clé
print(berti["nom"])
print(berti.get("nom"))



#Supprimer une entrée


#Récupérer la listes des clés
print(" liste des clés", berti.keys())

#Récupérer la listes des valeurs
print("liste des valeurs", berti.values())


#Récupérer la listes des clés/valeurs
print(berti.items())


#Copier un dictionnaire par référence
un_dico = berti
berti["commentaires"] = "RAS"
print(berti)
print(un_dico)


#Copier un dictionnaire par valeur
deux_dico = berti.copy()
del berti["commentaires"]
print(berti)
print(deux_dico)







# Variables locales vs variables globales


  



#Mutiples variables
