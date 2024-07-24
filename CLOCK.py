from tkinter import*
from tkinter.ttk import *

from time import strfttime

root = tk()
root.title("CLOCK")

def time():
    string = strftime('%H:%M:%S %P')
    lable.config(text=string)
    lable.after(1000,time)

lable = Lable(root, font=("ds-digital", 80), background ="black" , foreground = "cyan")
lable.pack(anchor='center')
time()

mainloop()
