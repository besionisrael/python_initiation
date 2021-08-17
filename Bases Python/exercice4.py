

# 4. Définissez une fonction maximum(n1,n2,n3) qui renvoie le plus grand de 3 nombres n1, n2,
# n3 fournis en arguments. Par exemple, l’exécution de l’instruction :
# print(maximum(2,5,4)) doit donner le résultat : 5.



def maximum(n1, n2, n3):
    ma_liste = [n1, n2, n3]
    pg = ma_liste[0]
    for x in ma_liste:
        if x > pg:
            pg = x
    return pg



print(maximum(115,60,45))