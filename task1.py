#!python3

import tkinter as tk
from tkinter import *

Window = tk.Tk()
Window.title("tk")
Window.geometry("500x25")

entry1 = tk.Entry(Window, width = 25)
label1 = tk.Label(Window, text="x")
entry2 = tk.Entry(Window, width = 25)
button1 = tk.Button(Window, text="=")
entry3 = tk.Entry(Window, width = 25)




entry1.grid(row = 1, column = 1)
label1.grid(row = 1, column = 2)
entry2.grid(row = 1, column = 3)
button1.grid(row = 1, column = 4)
entry3.grid(row = 1, column = 5)

Window.mainloop()