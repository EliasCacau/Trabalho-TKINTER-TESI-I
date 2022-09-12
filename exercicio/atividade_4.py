import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Gerenciador Grid")
        self.janela.geometry("400x200")
        self.janela.configure(background='grey')
        self.janela.resizable(0, 0)
        self.lbl1 = tk.Label(self.janela, text="Número 1:")
        self.lbl1.grid(column=0, row=0)


janelaPrincipal = tk.Tk()
Tela(janelaPrincipal)
janelaPrincipal.mainloop()