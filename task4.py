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

DPhoto.place(x = 70, y = 0)
Pochacco.place(x = 140, y = 40)
Descript.place(x = 0, y = 100)

window.mainloop()