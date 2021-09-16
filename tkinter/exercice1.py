
#Jusqu’à présent, nous avons utilisé Python exclusivement
#« en mode texte ». Nous avons procédé ainsi parce qu’il 
#nous fallait absolument d’abord dégager un certain nombre
#de concepts élémentaires ainsi que la structure de base du 
#langage, avant d’envisager des expériences impliquant des 
#objets informatiques plus élaborés (fenêtres, images, sons, etc.).
#Nous pouvons maintenant nous permettre ....
from tkinter import *

fen1 = Tk() 
#Ainsi la classe Tk(), qui est l’une des classes 
#les plus fondamentales de la bibliothèque tkinter, contient
#tout ce qu’il faut pour engendrer différents types de fenêtres
#d’application, de tailles ou de couleurs diverses, avec ou sans
#barre de menus, etc. Nous nous en servons ici pour créer notre 
#objet graphique de base, à savoir la fenêtre qui contiendra tout
#le reste


tex1 = Label(fen1, text='Bonjour tout le monde !', fg='red')
#nous créons un autre objet (un widget), cette fois à partir de 
#la classe Label(). Comme son nom l’indique, cette classe définit 
#toutes sortes d’étiquettes (ou de libellés). 
#Le premier argument transmis (fen1), indique que le nouveau 
#widget que nous sommes en train de créer sera contenu dans un 
#autre widget préexistant, que nous désignons donc ici comme 
#son « maître » : l’objet fen1 est le widget maître de l’objet tex1.
#On pourra dire aussi que l’objet tex1 est un widget esclave de l’objet fen1. 


tex1.pack()

#La méthode pack() fait partie d’un ensemble de 
#méthodes qui sont applicables non seulement aux widgets
#de la classe Label(), mais aussi à la plupart des autres 
#widgets tkinter, et qui agissent sur leur disposition géométrique 
#dans la fenêtre
#la méthode pack() réduit automatiquement la taille de la 
#fenêtre « maître » afin qu’elle soit juste assez grande 
#pour contenir les widgets « esclaves » définis au préalable. 

bou1 = Button(fen1, text='Quitter', command = fen1.destroy)
#nous créons notre second widget « esclave » : un bouton. 
#Comme nous l’avons fait pour le widget précédent, nous appelons
#la classe Button() en fournissant entre parenthèses un certain
#nombre d’arguments. Étant donné qu’il s’agit cette fois d’un 
#objet interactif, nous devons préciser avec l’option command 
#ce qui devra se passer lorsque l’utilisateur effectuera un clic 
#sur le bouton. Dans ce cas précis, nous actionnerons la méthode 
#destroy associée à l’objet fen1, ce qui devrait provoquer l’effacement de la fenêtre41

bou1.pack()

fen1.mainloop()

#parce que c’est elle qui provoque le démarrage du réceptionnaire
#d’événements associé à la fenêtre. Cette instruction est nécessaire 
#pour que notre application soit « à l’affût » des clics de souris,
#des pressions exercées sur les touches du clavier, etc. C’est 

