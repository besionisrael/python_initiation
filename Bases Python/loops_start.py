#
# Fichier d'exemple pour les boucles
#

def main():
  
  
  # Definir une boucle while
  x = 0
  '''while(x < 5):
    print("la valeur de x est {}".format(x))
    x += 1'''
    
  
  

  # Definir une boucle For
  '''for i in range(5,11):
    print ("la valeur i est ", i)  '''
  
    
  # Utiliser For sur une collection
  days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredri", "Samedi", "Dimanche"]

  # for d in days:
  #   print(d)

  
  
  # Utilisation du break and continue statements

  '''for x in range(5,10):
    if(x == 7): break
    print(x)'''

  
  
  #Utiliser la fonction enumerate() pour retrouver l'index
  for i,d in enumerate(days):
    print("Index {}, Contenu {}".format(i,d))
  
  
if __name__ == "__main__":
  main()
