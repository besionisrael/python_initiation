
from tkinter import *

class Application:
    
    def __init__(self):
        self.root = Tk()
        self.dessineResistance()
        Label(self.root, text = "Saisissez la valeur de la resistance").grid(row=4,column=2, columnspan=6)
        Button(self.root, text = "Quitter", command=self.root.destroy).grid(row=6, column=2)
        Button(self.root, text= "Montrer", command=self.montrerCouleur).grid(row = 6, column=6)
        self.entree = Entry(self.root, width= 28)
        self.entree.grid(row=6, column=4)
        self.couleur = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', "grey", "white"]

        self.root.mainloop()
    
    def dessineResistance(self):
        self.can = Canvas(self.root, width=500, height=200, bg="ivory")
        self.can.pack()
        self.can.grid(row =2, column=2, columnspan=6, pady=10, padx=10)
        self.can.create_line(20,100,480,100, width=10)
        self.can.create_rectangle(130,60,370,140, fill="light grey", width = 4)
        self.ligne = []
        for x in range(170, 300, 48):
            self.ligne.append(self.can.create_rectangle(x, 60, x + 24, 140, fill="black", width=0 ))
    
    def montrerCouleur(self):
        self.valeur = self.entree.get()
        print("Valeur saisie........", self.valeur)
        isFailed = False

        try:
            val = float(self.valeur)
        except Exception as e:
            isFailed = True
        if isFailed:
            self.signaleEntree()
        
        self.can.itemconfigure(self.ligne[0], fill=self.couleur[8])
        
        


        
    
    def signaleEntree(self):
        self.entree.configure(bg= "red")
        self.root.after(1000, self.videEntree)

    def videEntree(self):
        self.entree.config(bg = "white")
        self.entree.delete(0, len(self.valeur))
        

        #self.can.itemconfigure(self.ligne[0], fill = "red") 
        






if __name__ == "__main__":
    f = Application()