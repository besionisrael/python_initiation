# Cours no 7 : « Programmation Orientée Objet »
# 1. Définir une classe MaClasse possédant les attributs suivants :
# données : deux attributs de classes : x = 23 et y = x + 5.
# méthode : une méthode affiche contenant un attribut d’instance z = 42 et les affichages de y et de z.
# Dans le programme principal, instanciez un objet de la classe MaClasse et invoquez la
# méthode affiche.



# 2. Définir une classe Vecteur2D avec un constructeur fournissant les coordonnées par
# défaut d’un vecteur du plan (par exemple : x = 0 et y = 0).
# Dans le programme principal, instanciez un Vecteur2D sans paramètre, un Vecteur2D
# avec ses deux paramètres, et affichez-les.



# 3. Enrichissez la classe Vecteur2D précédente en lui ajoutant une méthode d’affichage
# et une méthode de surcharge d’addition de deux vecteurs du plan.
# Dans le programme principal, instanciez deux Vecteur2D, affichez-les et affichez leur
# somme.





# Cours no 8 : « Notions de COO et d’encapsulation »
# 1. Définir une classe Rectangle avec un constructeur donnant des valeurs (longueur et
# largeur) par défaut et un attribut nom = "rectangle", une méthode d’affichage et
# une méthode surface renvoyant la surface d’une instance.
# Définir une classe Carre héritant de Rectangle et qui surcharge l’attribut d’instance :
# nom = "carré".
#Dans le programme principal, instanciez un Rectangle et un Carre et affichez-les.



# 2. Définir une classe Point avec un constructeur fournissant les coordonnées par défaut
# d’un point du plan (par exemple : x = 0.0 et y = 0.0).
# Définir une classe Segment dont le constructeur possède quatre paramètres : deux
# pour l’origine et deux pour l’extrémité. Ce constructeur définit deux attributs : orig
# et extrem, instances de la classe Point. De cette manière, vous concevez une classe
# composite : La classe Segment est composée de deux instances de la classe Point.
# Ajouter une méthode d’affichage.
# Enfin écrire un auto-test qui affiche une instance de Segment initialisée par les valeurs
# 1, 2, 3 et 4.



# 3. Définir une fonction fabrique creer_plus renvoyant une fonction fermeture plus. ▹
# cree_plus a un argument ajout. Son code ne renferme que la fonction plus qui,
# elle aussi, possède un argument increment et dont le code se contente de renvoyer
# la somme : (ajout + increment).
# Dans le programme principal, créez deux fonctions, par exemple p = creer_plus(23)
# et p = creer_plus(42), puis affichez les valeurs données par p(100) et q(100).



# 4. Écriture d’une fonction fabrique renvoyant une instance de classe. ▹
# Définir une classe CasNormal contenant une méthode uneMethode qui affiche "normal".
# Définir une classe CasSpecial contenant une méthode uneMethode qui affiche "spécial".
# Enfin définir la fonction fabrique casQuiConvient avec un paramètre estNormal initialisé par défaut à True. Si le paramètre est vérifié, le corps de la fonction renvoie une
# instance de la classe CasNormal, sinon il renvoie une instance de la classe CasSpecial.
# Dans le programme principal, créez l’instance que vous désirez grâce à la fabrique,
# puis vérifiez son type en appelant dessus la méthode uneMethode.