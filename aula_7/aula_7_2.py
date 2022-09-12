import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("800x600")
        self.janela.title("Imagem")
        self.minha_imagem = tk.PhotoImage(file="imagem1.png")
        self.lbl_1 = tk.Label(self.janela, text="SIGMA!").pack()
        self.lbl = tk.Label(self.janela, image=self.minha_imagem)
        self.lbl.image = self.minha_imagem
        self.lbl.pack(fill=tk.BOTH, expand=True)

app = tk.Tk()
Tela(app)
app.mainloop()