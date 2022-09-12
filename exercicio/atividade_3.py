import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Gerenciador Grid")
        self.janela.geometry("400x230")
        self.janela.resizable(0, 0)
        self.but1 = tk.Button(self.janela, text='1')
        self.but1.grid(column=5, row=0, stick=tk.N,  padx=3, pady=0, columnspan=3)

        self.but2 = tk.Button(self.janela, text='2')
        self.but2.grid(column=2, row=1,stick=tk.N, padx=0)

        self.but3 = tk.Button(self.janela, text='3')
        self.but3.grid(column=3, row=1,stick=tk.N, padx=0, pady=0)

        self.but4 = tk.Button(self.janela, text='4')
        self.but4.grid(column=0, row=2,stick=tk.N, padx=0, pady=0)

        self.but5 = tk.Button(self.janela, text='5')
        self.but5.grid(column=2, row=2,stick=tk.N, padx=0, pady=0)

        self.but6 = tk.Button(self.janela, text='6')
        self.but6.grid(column=2, row=2,stick=tk.N, padx=0, pady=0)


janelaPrincipal = tk.Tk()
Tela(janelaPrincipal)
janelaPrincipal.mainloop()