#
# Lire et écrire dans les fichiers
#

def main():  
  
  #Ouvrir un fichier pour ecriture and le créer si cela n'existe pas
  # f = open("textfile2.txt", 'w')
  # f.close()
  
  
  # Ouvrir un fichier pour ajouter du contenu à la fin
  f = open("textfile.txt", "a")
  
  

  # Ecrire quelques lignes des données dans le fichier
  # for x in range(0,5):
  #   f.write('Ligne {}\n'.format(x + 1))
  
  
  # Fermer le fichier à la fin des opérations
  #f.close()
  
  # Ouvrir le fichier en mode lecture
  f = open("textfile.txt", 'r')
  

  #Lire dans le fichier
  if f.mode == "r":
    #Je peux lire de
    #print(f.read())

    #print(f.readline(5))
    for uneligne in f.readlines():
      print("***", uneligne)


  
    
if __name__ == "__main__":
  main()
