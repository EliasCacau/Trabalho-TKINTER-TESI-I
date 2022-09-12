import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Cadastro")
        self.janela.geometry("300x300")
        self.nom = tk.Label(self.janela, text="nome:")
        self.nom.grid(column=0, row=0)
        self.ent_nom = tk.Entry(self.janela)
        self.ent_nom.grid(column=1, row=0, columnspan=2, sticky=tk.EW)
        self.ema = tk.Label(self.janela, text="Email:")
        self.ema.grid(column=0, row=1)
        self.ent_ema = tk.Entry(self.janela)
        self.ent_ema.grid(column=1, row=1, columnspan=2, sticky=tk.EW)
        self.ide = tk.Label(self.janela, text="Instituição de Ensino:")
        self.ide.grid(column=1, row=2, columnspan=2, sticky=tk.EW)
        self.cbx = ttk.Combobox(self.janela)
        self.cbx['values'] = ('UFAC', 'FAAO', 'U:VERSE')
        self.cbx.current(0)
        self.cbx.grid(column=1, row=2, columnspan=2, sticky=tk.EW)
        self.sep = tk.Label(self.janela, text="Sua experiência com programação?")
        self.sep.grid(column=0, row=4, columnspan=3, sticky=tk.EW)
        self.sct = ScrolledText(self.janela, height=5, width=25)
        self.sct.grid(column=0, row=6, columnspan=3, rowspan=3)

app = tk.Tk()
Tela(app)
app.mainloop()

