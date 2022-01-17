######### Label.py

from tkinter import *
from tkinter import ttk        
    
root = Tk()

label = ttk.Label(root, text = "Hello, Tkinter!")
label.pack()
label.config(text = 'Howdy, Tkinter!')
label.config(text = 'Howdy, Tkinter! It\'s been a really long time since we last met.  Great to see you again!')
label.config(wraplength = 150)
label.config(justify = CENTER)
label.config(foreground = 'blue', background = 'yellow')
label.config(font = ('Courier', 18, 'bold'))
label.config(text = 'Howdy, Tkinter!')

# label.img = logo
# label.config(image = label.img)

root.mainloop()


###############Button.py

from tkinter import *
from tkinter import ttk        
    
root = Tk()

button = ttk.Button(root, text = "Click Me")
button.pack()

def callback():
    print('Clicked!')

button.config(command = callback)
button.invoke() #Pour simuler un click sur le bouton

button.state(['disabled'])
print(button.instate(['disabled']))
button.state(['!disabled'])
print(button.instate(['!disabled']))


root.mainloop()


#Entry.py

from tkinter import *
from tkinter import ttk        
    
root = Tk()

entry = ttk.Entry(root, width = 30)
entry.pack()

entry.get()
entry.delete(0, 1)
entry.delete(0, END)
entry.insert(0, 'Enter your password')

entry.config(show = '*')
entry.state(['disabled'])
entry.state(['readonly'])
entry.state(['!disabled'])


#Addenda
montexte = StringVar()
entry = ttk.Entry(root, width = 30, textvariable=montexte)
root.mainloop()


