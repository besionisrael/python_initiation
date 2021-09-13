

#Integer
#a = 15
#print(a)


#float
b = 7.5
#print(b)
#print("le type de b", type(b))

#String
#texte1 = 'Ceci est un texte1'
#texte2 = "Ceci est un texte2"
#texte3 = '''
#Ceci est un texte sur plusieurs lignes
#'''

#print(texte1, texte2, texte3)

#Redeclaration des variabes
b = 8
#print(b)
#print("le type de b", type(b))

#Caster
'''age = '14'
print(age, type(age))
age_converti = int(age)
print(age_converti, type(age_converti))
ajout = age_converti + 10
print("resultat", ajout)'''

age = '14'
ajout = int(age) + 10
#print("resultat", ajout)

#Convertir en entier: int()
age = '14'
age = int(age)
#Convertir en string: str()

#taille = 2.5
#print("ma taille est " + taille)


#Convertir en float: float()

#Operations sur le string
texte1 = "Je m'appelle "
texte2 = "Henry"

#Concatenation
texte3 = texte1 + texte2
print("concatenation", texte3)

#longueur de la chaine
print("longueur de la chaine", len(texte3))

#split
print("Split ex ", texte3.split(" "))

#Mettre en majuscule
print("texte en majuscule", texte3.upper())

print("capitalize", texte3.capitalize())
print("lower", texte3.lower())
print("replace", texte3.replace(" ", "-"))