#Exercice


# 1. Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. Par
# exemple, si on l’appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15], ce programme devrait afficher :
# le plus grand élément de cette liste a la valeur 75.





def main():
    ma_liste = [32, 5, 12, 8, 3, 75, 2, 15]
    pg = ma_liste[0]
    for unelement in ma_liste:
        if (unelement > pg):
            pg = unelement
    print("le plus grand élément de cette liste a la valeur", pg)


if __name__ == "__main__":
    main()