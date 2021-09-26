#
# Fichier d'Exemple pour les structures conditionnelles
#


def main():
    x, y = 100, 5

    # flow conditionel utilisant if, elif, else
    if(x > y):
        print("X est supérieur à Y")    
    elif(x < y):
        print("X est inferieur à Y")    
    else:
        print("X est égal à Y")    
    
    # conditional statements te permet de  faire "a if C else b"
    st = "X est supérieur à Y" if (x > y) else "X est inferieur ou égal à Y"
    print(st)

    

    
    
    
    

    #Instruction imbriquée
    age1, age2 = 10, 50
    nom1, nom2 = "Paul", "Henry"

    if (age1 == 10):
        if nom1 == "Paul":
            print("Paul a 10 ans")
        elif nom2 == "Henry":
            print("Henry a 10 ans")
    elif (age2 == 50):
        if nom1 == "Paul":
            print("Paul a 50 ans")
        elif nom2 == "Henry":
            print("Henry a 50 ans")
    


    

if __name__ == "__main__":
    main()
