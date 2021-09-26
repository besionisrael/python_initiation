
#Import

from cartes import JeuDeCartes

def bataille():
    jeuA = JeuDeCartes()
    jeuB = JeuDeCartes()
    
    jeuA.battre()
    jeuB.battre()

    pointA, pointB = 0, 0

    for i in range(52):
        carteA = jeuA.tirer()
        carteB = jeuB.tirer()        

        if carteA[0] > carteB[0]:
            pointA += 1
        elif carteA[0] < carteB[0]:
            pointB += 1
    print("A obtient {} pts et B obtient {} pts".format(pointA, pointB))
        


if __name__ == "__main__":
    bataille()




