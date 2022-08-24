import tkinter as tk

class Tela:


    def __init__(self, master):
        self.janela = master
        self.janela.title("CLICK")
        self.janela.geometry("800x600")

        def clicou(event):
            self.lbl = tk.Label(self.janela, text="Você clicou!!!")
            self.lbl.pack()

        self.btn = tk.Button(self.janela, text="Clique")
        self.btn.bind('<Return>', clicou)
        self.btn.bind('<Button-1>', clicou, add='+')
        self.btn.bind('<Button-2>', clicou, add='+')
        self.btn.bind('<BackSpace>', clicou, add='+')
        self.btn.bind('<KeyPress-a>', clicou, add='+')
        self.btn.bind('<BackSpace>', clicou, add='+')
        #self.btn.bind('<Double-Button-1>', clicou, add='+')
        
        self.btn.pack()



app = tk.Tk()
Tela(app)
app.mainloop()