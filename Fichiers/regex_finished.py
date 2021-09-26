#Import
import re
#Utilisation
texte = "Je m'appelle Paul"

print("Paul" in texte)

pseudo = re.findall(r"kevin\d+", texte)
print(pseudo)
texte = "Je m'appelle Paul Paul33 Paul444 Paul9"
pseudo = re.findall(r"kevin[0-9]+", texte)
print(pseudo)



#Reconnaitre email
#Test if the email saisi is ok
user_input = input()
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|org|net)"
if(re.search(pattern, user_input)): print("Email valide")
else: print("Email non valide")


#Trouver toutes les dates
texte = "On est le 15-03-2020"
pattern = r"\d{2}-\d{2}-\d{4}" #pattern = r"\d{2}[-/]\d{2}[-/]\d{4}"
pt = re.compile(pattern)
pt.findall(texte)




#écrire un programme Python qui match  une chaîne de caractères comportant un a suivi 
# de zéro ou plusieurs de b


def text_match(text):
        patterns = 'ab*?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))

#Écrivez un programme Python pour supprimer les zéros de tête d'une adresse IP.
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)

#Write a Python program to find the substrings within a string.
#Ecrire un programme python pour trouver un mot dans une chaine de caractère
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)


#Écrivez un programme Python pour vérifier qu'une chaîne de caractères ne 
# contient qu'un certain ensemble de caractères (dans ce cas, a-z, A-Z et 0-9).

def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))


#Écrivez un programme Python pour faire correspondre une chaîne de caractères qui ne contient
#  que des lettres majuscules et minuscules, des chiffres et des caractères de soulignement.

def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))


#Écrivez un programme Python pour rechercher certaines chaînes littérales dans une chaîne de caractères.
patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print('Matched!')
    else:
        print('Not Matched!')


#Écrivez un programme Python pour insérer des espaces entre les mots commençant par une majuscule.
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))


#EXErcice 4

#Retrouvez tous les mots dans une chaine de caractères

def words(string):
	pattern = r"\b(\w+)\b"
	return re.findall(pattern, string)

#Retrouver tous les mots qui se terminent par un caractère donné
def wordsStartingBy(string, c):
    #pattern = r"\b^" + c + r"\w+\b"
    pattern = r"\b(" + c +"\w+)\b"
    return re.findall(pattern, string)

#Retrouver tous les mots qui se commencent par un caractère donné
def wordsEndingBy(string, c):
	pattern = r"\b(\w+" + c + r")\b"
	return re.findall(pattern, string)

#Retrouver tous les mots qui contiennent au moins un caractère
def wordsHavingAtLeastOneCharacter(string):
    pattern = r"\b\w+\b"
    return re.findall(pattern, string)

#Retrouver tous les mots qui possèdent exactement n caractères
def wordsHavingAtLeastNCharacter(string, n):
    pattern = r"\b\w{" + str(n) + r"}\b"
    return re.findall(pattern, string)



if __name__ == "__main__":
    pass



