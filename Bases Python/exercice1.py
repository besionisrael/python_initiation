#Exercice


# 1. Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. Par
# exemple, si on l’appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15], ce programme devrait afficher :
# le plus grand élément de cette liste a la valeur 75.


maliste = [32, 5, 12, 8, 3, 75, 2, 15]

pg = maliste[0]
for unelt in maliste:
    if unelt > pg:
        pg = unelt
print("Le plus grand élément est %d" % pg)
print("Le plus grand élément est {}".format(pg))
print("Le plus grand élément est ", pg)

