import re
#Write a Python program that matches a string that has an a followed by zero or more b's.
#écrire un programme Python qui match  une chaîne de caractères comportant un a suivi 
# de zéro ou plusieurs de b

#Écrivez un programme Python pour supprimer les zéros de tête d'une adresse IP.


if __name__ == "__main__":
    #string = "Retrouver tous les mots qui se terminent par un caractère donné"
    ip = "016.08.004.196"
    string = re.sub('(^[0]*|\.[0]*)', '.', ip)
    print(string)