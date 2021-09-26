from tkinter import *
from random import randrange

x1 = 0
def tracer_ligne():
    global x1,x2,y1,y2
    can1.create_line(x1,y1,x2,y2, width=5, fill=couleur)
    y2,y1 = y2 + 20, y1 - 20

def changercouleur():
    global couleur
    liste_couleur = ["red", "green", "yellow", "orange", "purple", "blue"]
    index = randrange(5)
    couleur = liste_couleur[index]

#####Programme principal########

fen1 = Tk()
couleur = "blue"
x1,x2,y1,y2 = 10,490,490,10
can1 = Canvas(fen1, bg="dark grey", height=500, width=500)
can1.pack(side = LEFT)
bouton1 = Button(fen1, text = "Quitter", command = fen1.destroy)
bouton1.pack(side = BOTTOM)

bouton2 = Button(fen1, text = "Tracer une ligne", command=tracer_ligne)
bouton2.pack()
bouton3 = Button(fen1, text="Autre Couleur", command=changercouleur)
bouton3.pack()
fen1.mainloop()