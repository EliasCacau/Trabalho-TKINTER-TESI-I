import tkinter as tk


class Tela:

    def __init__(self, master):
        self.janela = master
        self.janela.title("CLICK")
        self.janela.geometry("800x600")

        def esquerdo(event):
            self.lbl['bg'] = 'White'
            self.lbl['fg'] = 'Black'
            
        def direito(event):
            self.lbl['bg'] = 'Black'
            self.lbl['fg'] = 'White'

        self.btn = tk.Button(self.janela, text="Direito")
        self.btn.bind('<Enter>', esquerdo)
        self.btn.bind('<Leave>', direito, add='+')
        self.btn.pack(fill=tk.X)

        self.lbl = tk.Label(self.janela, text="ALTERAÇÃO")
        self.lbl.pack(expand=True, fill=tk.BOTH)

app = tk.Tk()
Tela(app)
app.mainloop()