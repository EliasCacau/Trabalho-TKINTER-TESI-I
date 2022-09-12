import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Gerenciador Pack")
        self.janela.geometry("400x450")

        self.lbl1 = tk.Label(self.janela, text="Red", bg="red", fg="white")
        self.lbl1.pack(ipadx=10, ipady=15, side=tk.TOP, fill=tk.BOTH)

        self.lbl2 = tk.Label(self.janela, text="Green", bg="green", fg="white")
        self.lbl2.pack(ipadx=10, ipady=15, side=tk.TOP, fill=tk.BOTH)

        self.lbl3 = tk.Label(self.janela, text="Blue", bg="blue", fg="white")
        self.lbl3.pack(ipadx=10, ipady=15, side=tk.TOP, fill=tk.BOTH)

        self.lbl4 = tk.Label(self.janela, text="Grey", bg="gray", fg="white")
        self.lbl4.pack(ipadx=20, side=tk.RIGHT, fill=tk.BOTH)

        self.lbl5 = tk.Label(self.janela, text="Grey", bg="gray", fg="white")
        self.lbl5.pack(ipadx=20, side=tk.LEFT, fill=tk.BOTH)

        self.lbl6 = tk.Label(self.janela, text="Black", bg="black", fg="white")
        self.lbl6.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.lbl7 = tk.Label(self.janela, text="Cyan", bg="cyan")
        self.lbl7.pack(ipady=15, side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.lbl8 = tk.Label(self.janela, text="Magenta", bg="magenta")
        self.lbl8.pack(ipady=15, side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.lbl9 = tk.Label(self.janela, text="Yellow", bg="yellow")
        self.lbl9.pack(ipady=15, side=tk.RIGHT, fill=tk.BOTH, expand=True)




janelaPrincipal = tk.Tk()
Tela(janelaPrincipal)
janelaPrincipal.mainloop()