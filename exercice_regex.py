import re

def mots(string):
    pattern =  r"\b(\w+)\b"
    return re.findall(pattern, string)

def motsFinissantParCaractere(string, c):
    pattern =  r"\b\w+" + c + r"\b"
    return re.findall(pattern, string)

def main():
    print(mots("Bonjour je suis là"))
    print(motsFinissantParCaractere("Bonjour je suis là pour toi", "s"))

if __name__ == "__main__":
    main()