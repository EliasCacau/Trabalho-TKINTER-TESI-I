import tkinter as tk
from tkinter import ttk, messagebox

class Tela:

    def __init__(self, master):
        self.janela = master
        self.janela.title("CLICK")
        self.janela.geometry("800x600")

        def selecionado(event):
            messagebox.showinfo("Info", f'{self.cbx.get()}')
        self.selection = tk.StringVar
        lista = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sexo', 'Sab']
        self.cbx = ttk.Combobox(self.janela, values=lista, )
        self.cbx.bind("<<ComboboxSelected>>", selecionado)
        self.cbx.pack()


app = tk.Tk()
Tela(app)
app.mainloop()