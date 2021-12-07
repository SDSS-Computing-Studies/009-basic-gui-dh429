#!Python3

import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Pochacco")
window.geometry("257x135")
window.resizable(False,False)

Photo = PhotoImage(file = "dog.png")
DPhoto = Label(window, image=Photo)
Pochacco = Label(text = "Pochacco!")
Descript = Label(text = "Acuddly little puppy! This is from the same \ncreators who brought you Keropi and Kero Kero", background="#aaffff")

DPhoto.grid(row = 1, column = 1, sticky = E)
Pochacco.grid(row = 1, column = 2, sticky = W)
Descript.grid(row = 2, column = 1, columnspan = 2, rowspan = 2)

window.mainloop()