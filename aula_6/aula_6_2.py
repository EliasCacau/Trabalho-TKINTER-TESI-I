import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Exemplo LabelFrame")
        self.janela.geometry("300x300")
        self.lfr = tk.LabelFrame(self.janela, text="Alinhamento", labelanchor=tk.SW)
        self.lfr.pack()

        self.rb1 = tk.Radiobutton(self.lfr, text="LEFT")
        self.rb1.pack(side=tk.LEFT)

        self.rb2 = tk.Radiobutton(self.lfr, text="CENTER")
        self.rb2.pack(side=tk.LEFT)

        self.rb3 = tk.Radiobutton(self.lfr, text="RIGHT")
        self.rb3.pack(side=tk.LEFT)

app = tk.Tk()
Tela(app)
app.mainloop()