from Tkinter import *

master = Tk()
listbox = Listbox(master)
listbox.pack()

x = ["1","2","3","4"] 
y = ["one", "two", "three", "four"]   

for i in range(len(y)):
    z = y[i] + " " + x[i]
    listbox.insert(END, z)

mainloop()