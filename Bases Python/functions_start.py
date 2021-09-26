#
# Fichier exemple pour les fonctions
#

# Ecrire une fonction basique
def fonction_basique():
    print("Je suis une fonction basique")




# Fonctions qui prennent plusieurs arguments
def fonction_multiple(arg1, arg2):
    print("Je prends {0} et {1}".format(arg1, arg2))


# Fonction qui retourne une valeur
def multiplication(arg1, arg2):
    return arg1 * arg2




# Fonction avec une valeur par défaut dans ses arguments
def puissance(nombre, x = 1):
    return nombre  ** x




# fonction avec un nombre variable des arguments
def multi_addition(*args):
    somme = 0
    for x in args:
        somme += x
    return somme




# Variables locales vs variables globales

if __name__ == "__main__":
    res = multi_addition(5, 2,22,58,98,2,4)
    print("resultat %d" % res)





