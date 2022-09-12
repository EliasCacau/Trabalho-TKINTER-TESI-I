import tkinter as tk
from tkinter import ttk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Treeview")
        self.janela.geometry("800x600")

        self.tvw = ttk.Treeview(self.janela)
        self.tvw.pack()
        self.tvw.insert("", 0, text="Aluno")
        self.tvw.insert("", 1, text="Vida")
        id_humor =self.tvw.insert("", "end", text="Humor")
        self.tvw.insert(id_humor, 'end', text="Rogério")
        self.tvw.insert(id_humor, 'end', text="Christopher")


app = tk.Tk()
Tela(app)
app.mainloop()