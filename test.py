
# Ecrire un programme qui demande à l’utilisateur de saisir une liste d’entiers puis à l’aide de parcours successifs de la liste effectuer les actions suivantes:
# 1.Afficher la liste
# 2. Afficher la liste en colonne de manière à afficher l’index et le contenu
# 3. Créer une nouvelle liste qui sera le multiple (3) de tous les éléments de la liste en utilisant une fonction lambda
# 4. Obtenir le plus grand nombre de la liste
# 5. Obtenir le plus petit nombre de la liste 
# 6. Compter le nombre des nombres pairs présents dans la liste
# 7. Calculer la somme de tous les nombres impairs de la liste
# NB: le programme doit gérer les exceptions au niveau de la saisie des données de l’utilisateur

print("*************Bienvenue*************")
print("***********************************")

print("Veuillez saisir vos entiers et terminer par OK")
reponse = 0
ma_liste = []
compteur = 0
somme = 0

while(reponse != "OK"):
    try:
        valeur = input("Saisir la valeur ...")
        ma_liste.append(int(valeur))
    except Exception as e:        
        if valeur == "OK": reponse = "OK"
        else: print("La valeur saisie n'est pas correcte, Réessayez!")
print("--1. Liste obtenue", ma_liste)
print("--2A.")
for i, d in enumerate(ma_liste):
    print("index {} ; valeur {}".format(i, d))
    #Compte & Somme
    if(d % 2 == 0):compteur += 1
    else: somme += d

print("--2B.")
for x in range(0,len(ma_liste)):
    print("index {} ; valeur {}".format(x, ma_liste[x]))

ma_liste_2 = list(map(lambda z: z*3, ma_liste))
print("--3, Nouvelle Liste", ma_liste_2)
print("--4, Le plus grand", max(ma_liste))
print("--5, Le plus petit", min(ma_liste))
print("--6, Le nombre des nombres pairs", compteur)
print("--7, La somme de tous les nombres impairs", somme)



f = open("monfichier.txt", "w+")

for x in range(2,31):
	f.write("Table de multiplication par %d\n" % x)
	for y in range(1,21):
		f.write("{} fois {} = {}\n".format(x, y, x*y))

f.close()