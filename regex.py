texte = "Je m'appelle Paul"

print("Paul" in texte)

pseudo = re.findall(r"kevin\d+", texte)
print(pseudo)
texte = "Je m'appelle Paul Paul33 Paul444 Paul9"
pseudo = re.findall(r"kevin[0-9]+", texte)
print(pseudo)


def words(string):
	regex = r"\b(\w+)\b"
	return re.findall(regex, string)


def wordsEndingBy(string, c):
	regex = r"\b(\w+" + c + r")\b"
	return re.findall(regex, string)