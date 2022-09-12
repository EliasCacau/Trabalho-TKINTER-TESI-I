import tkinter as tk

class TopLevel():
        def abrir_top(self):
            self.janela.withdraw()
            self.top = tk.Toplevel(self.janela)
            self.top.title("Janela Toplevel")
            self.top.geometry("800x600")
            self.top.grab_set()
            self.btn2 = tk.Button(self.top, text="Voltar", command=self.fechar_top).pack()

        def fechar_top(self):
            self.top.destroy()
            self.janela.deiconify()

        def __init__(self, master):
            self.janela = master
            self.janela.title("First Window")
            self.janela.geometry("800x600")
            self.btn = tk.Button(self.janela, text="Abrir", command=self.abrir_top).pack()

app = tk.Tk()
TopLevel(app)
app.mainloop()


