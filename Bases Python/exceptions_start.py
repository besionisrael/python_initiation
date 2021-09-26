#Lever une exception
# num = input ("Saisissez un nombre...")
# num = int(num)
# print('vous avez saisi', num)


#Traiter une exception

# try:
#     num = input ("Saisissez un nombre...")
#     num = int(num)    
# except ValueError :
#     print("L'élément saisi n'est pas un entier")
# else:
#     print('vous avez saisi', num)
# finally:
#     print("******Fin du programme********")



#Double exception
# try:
#     numerateur = int(input("Numerateur:......"))
#     denominateur = int(input('Denominateur:......'))
#     resultat = numerateur / denominateur
#     print('Le resultat est {0}'.format(resultat))
# except ValueError:
#     print("L'élément saisi n'est pas un entier")
# except ZeroDivisionError:
#     print("On ne peut pas diviser par Zero")




#Récupérer le message d’une exception
# try:
#     num = input ("Saisissez un nombre...")
#     num = int(num)    
#     print('vous avez saisi', num)
# except ValueError as e :
#     print("Mon message", e)



#Clause else
#Le bloc else permet de distinguer la partie du code qui est susceptible de produire une exception de celle qui fait partie du comportement nominal du code mais qui ne produit pas d’exception.


#Post-traitement

# try:
#     numerateur = int(input("Numerateur:......"))
#     denominateur = int(input('Denominateur:......'))
#     resultat = numerateur / denominateur
#     print('Le resultat est {0}'.format(resultat))
# except Exception as e:
#     print("Quelque chose s'est mal passé, msg ", e)



#Lever une exception
x  = input("saisissez un entier")
x = int(x)
if x < 0:
    raise ValueError("vous avez saisi un nombre negatif")

def main():
    pass


if __name__ == "__main__":
    main()

# Ecrire un programme qui demande à l’utilisateur de saisir une liste d’entiers puis à l’aide de parcours successifs de la liste effectuer les actions suivantes:
# 1.Afficher la liste
# 2. Afficher la liste en colonne de manière à afficher l’index et le contenu
# 3. Créer une nouvelle liste qui sera le multiple (3) de tous les éléments de la liste en utilisant une fonction lambda
# 4. Obtenir le plus grand nombre de la liste
# 5. Obtenir le plus petit nombre de la liste 
# 6. Compter le nombre des nombres pairs présents dans la liste
# 7. Calculer la somme de tous les nombres impairs de la liste
# NB: le programme doit gérer les exceptions au niveau de la saisie des données de l’utilisateur
