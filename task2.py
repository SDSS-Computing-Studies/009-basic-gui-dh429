#!python3
import tkinter as tk
from tkinter import *
from tkinter import ttk



window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("690x170")

DogPhoto = PhotoImage(file="dog.png")
DPhoto = tk.Label(window, image=DogPhoto)
TitleText = tk.Label(text = "Client Database")
TkSearch = tk.Entry(window, width = 30)
TkButton = tk.Button(window, text = "Search by Name")
TkName = tk.Label(text = "Name")
TkType = tk.Label(text = "Type")
TkBreed = tk.Label(text = "Breed")
TkOwner = tk.Label(text = "Owner")
TkBday = tk.Label(text = "Birthdate")
TkSearch1 = tk.Entry(window, width = 20)
TkSearch2 = tk.Entry(window, width = 20)
TkSearch3 = tk.Entry(window, width = 20)
TkSearch4 = tk.Entry(window, width = 20)
TkSearch5 = tk.Entry(window, width = 20)
TkPrevious = tk.Button(window, text = "Previous")
TkSave = tk.Button(window, text = "Save Entry")
TkNext = tk.Button(window, text = "Next")

DPhoto.grid(row = 1, column = 1)
TitleText.grid(row = 1, column = 2, columnspan = 3, rowspan = 2)
TkButton.grid(row = 1, column = 4, sticky = N)
TkSearch.grid(row = 1, column = 5, sticky = NE)
TkName.grid(row = 2, column = 1)
TkType.grid(row = 2, column = 2)
TkBreed.grid(row = 2, column = 3)
TkOwner.grid(row = 2, column = 4)
TkBday.grid(row = 2, column = 5)
TkSearch1.grid(row = 3, column = 1)
TkSearch2.grid(row = 3, column = 2)
TkSearch3.grid(row = 3, column = 3)
TkSearch4.grid(row = 3, column = 4)
TkSearch5.grid(row = 3, column = 5)
TkPrevious.grid(row = 4, column = 1, sticky = W)
TkSave.grid(row = 4, column = 3)
TkNext.grid(row = 4, column = 5, sticky = E)
window.mainloop()


