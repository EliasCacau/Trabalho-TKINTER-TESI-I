import tkinter as tk


class Tela:

    def __init__(self, master):
        self.janela = master
        self.janela.title("CLICK")
        self.janela.geometry("800x600")

        def clicou(event):
            self.lbl = tk.Label(self.janela, text=f"{event.keysym}")
            self.lbl.pack(side=tk.LEFT)

        self.btn = tk.Button(self.janela, text="Clique")
        self.btn.bind('<Return>', clicou)
        self.btn.focus()
        #self.btn.bind('<space>', clicou, add='+')
        self.btn.pack()


app = tk.Tk()
Tela(app)
app.mainloop()