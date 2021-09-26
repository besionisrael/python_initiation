
from tkinter import *

fen1 = Tk()
text1 = Label(fen1, text="Hello tout le monde !", fg = 'red')
text1.pack()

bouton1 = Button(fen1, text = "Quitter", command=fen1.destroy)
bouton1.pack()

fen1.mainloop()
