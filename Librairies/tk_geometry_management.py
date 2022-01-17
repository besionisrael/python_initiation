from tkinter import *
from tkinter import ttk        
    
root = Tk()

####1
ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow').pack(fill = BOTH, expand = True)
ttk.Label(root, text = 'Hello, Tkinter!', background = 'blue').pack(fill = BOTH)
label = ttk.Label(root, text = 'Hello, Tkinter!',background = 'green').pack(fill = BOTH, expand = True)



#########GRID

from tkinter import *
from tkinter import ttk        
    
root = Tk()


ttk.Label(root, text = 'Yellow', background = 'yellow').grid(row = 0, column = 0)
ttk.Label(root, text = 'Blue', background = 'Blue').grid(row = 0, column = 1)
ttk.Label(root, text = 'Green', background = 'Green').grid(row = 1, column = 0)
ttk.Label(root, text = 'Orange', background = 'Orange').grid(row = 1, column = 1)


root.mainloop()



 
####GEOMETRY

#Si tu as besoin de la position exacte, use this one
from tkinter import *
from tkinter import ttk        
    
root = Tk()

root.geometry('640x480+200+200')

ttk.Label(root, text = 'Yellow', background = 'yellow').place(x = 100, y = 50, width = 100, height = 50)
root.mainloop()
