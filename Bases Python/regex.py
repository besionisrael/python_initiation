
import re

def motCommencantParCaractere(string, c):
    pattern = r"\b" + c + r"\w+"
    return re.findall(pattern, string)

def motDeNCaractere(string, n):
    pattern = r"\b\w{" + str(n) + r"}\b"
    return re.findall(pattern, string)



if __name__ == "__main__":
    texte1 = "Bonjour? Bibiche je suis là sur place"
    print(motCommencantParCaractere(texte1, "B" ))