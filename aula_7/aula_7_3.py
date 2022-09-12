import tkinter as tk
from PIL import Image, ImageTk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("800x600")
        self.janela.title("Imagem")
        self.img = Image.open("imagem1.jpeg")
        self.minha_imagem = ImageTk.PhotoImage(self.img)
        self.lbl = tk.Label(self.janela, image=self.minha_imagem)
        self.lbl.image = self.minha_imagem
        self.lbl.pack(fill=tk.BOTH, expand=True)

app = tk.Tk()
Tela(app)
app.mainloop()