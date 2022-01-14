
#Import de Tkinter
from tkinter import *



fen1 = Tk()
#initialisation



text1 = Label(fen1, text="Hello tout le monde !", fg = 'red')
#nous créons un autre objet (un widget), cette fois à partir de 
#la classe Label(). Comme son nom l’indique, cette classe définit 
#toutes sortes d’étiquettes (ou de libellés).

text1.pack()
#gestionnaire de geometrie pack


bouton1 = Button(fen1, text = "Quitter", command=fen1.destroy)
#creation d'un bouton avec une commande à executer quand on appuie dessus 

bouton1.pack()

fen1.mainloop()
#Démarrage du réceptionnaire d’événements associé à la fenêtre.