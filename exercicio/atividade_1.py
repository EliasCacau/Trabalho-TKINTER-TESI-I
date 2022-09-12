import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Pack Simples")
        self.janela.geometry("400x200")
        self.lbl1 = tk.Label(self.janela, text="TOPO", bg="yellow")
        self.lbl1.config(font=("Verdana"))
        self.lbl1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.lbl2 = tk.Label(self.janela, text="RODAPÉ", bg="cyan")
        self.lbl2.config(font=("Verdana"))
        self.lbl2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.lbl3 = tk.Label(self.janela, text="ESQUERDA", bg="red")
        self.lbl3.config(font=("Verdana"))
        self.lbl3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.lbl4 = tk.Label(self.janela, text="DIREITA", bg="green")
        self.lbl4.config(font=("Verdana"))
        self.lbl4.pack(ipadx=1, side=tk.RIGHT, fill=tk.BOTH, expand=True)



janelaPrincipal = tk.Tk()
Tela(janelaPrincipal)
janelaPrincipal.mainloop()