
#Import de Tkinter
from tkinter import *



fen1 = Tk()
#La classe Tk() contient tout ce qu’il faut pour engendrer différents types de fenêtres
#d’application, de tailles ou de couleurs diverses, avec ou sans
#barre de menus, etc. 



text1 = Label(fen1, text="Hello tout le monde !", fg = 'red')
#nous créons un autre objet (un widget), cette fois à partir de 
#la classe Label(). Comme son nom l’indique, cette classe définit 
#toutes sortes d’étiquettes (ou de libellés).

text1.pack()
#la méthode pack() réduit automatiquement la taille de la 
#fenêtre « maître » afin qu’elle soit juste assez grande 
#pour contenir les widgets « esclaves » définis au préalable. 


bouton1 = Button(fen1, text = "Quitter", command=fen1.destroy)
#nous devons préciser avec l’option commande
#ce qui devra se passer lorsque l’utilisateur effectuera un clic 
#sur le bouton. 

bouton1.pack()

fen1.mainloop()
#parce que c’est elle qui provoque le démarrage du réceptionnaire
#d’événements associé à la fenêtre. Cette instruction est nécessaire 
#pour que notre application soit « à l’affût » des clics de souris,
#des pressions exercées sur les touches du clavier, etc. 