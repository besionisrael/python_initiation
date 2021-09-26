#Utilisation

#Import
import re

# texte = "Je m'appelle Paul Paul1 Paul33 Paul545"
# print("Paul" in texte)

# pattern = r"Paul\d+"
# resultat = re.findall(pattern, texte)
# print("resultat", resultat)

user_input = input("Saisissez votre adresse email...")
#pattern =  "[a-zA-Z0-9]+@[a-z]+\.(fr|com|org)"
pattern = ".+@[a-z]+\.(fr|com|org)"

if re.search(pattern, user_input):print("Email valide")
else: print("Email non valide")

#Python_Exercises_1
#Python Exercices 1
#Python Exercice,1

pattern = r"^\d{2}(-|/| )\d{2}(-|/| )(\d{4}|\d{2})"
