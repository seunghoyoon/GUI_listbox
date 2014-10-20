from Tkinter import *

root = Tk()
listbox = Listbox(root)
listbox.pack()


arr = ['orange','green','sky']  


for i in range(0,len(arr)):   
    listbox.insert(END, arr[i])


mainloop()