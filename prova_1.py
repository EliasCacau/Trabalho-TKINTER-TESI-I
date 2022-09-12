import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title("Calculadora")
        self.janela.geometry("155x195")
        self.lbl = tk.Label(self.janela, height=2)
        self.lbl.grid(column=0, row=0, columnspan=4)

        self.t1 = tk.Button(self.janela, text="7")
        self.t1.grid(column=0, row=1)

        self.t2 = tk.Button(self.janela, text="8")
        self.t2.grid(column=1, row=1)

        self.t3 = tk.Button(self.janela, text="9")
        self.t3.grid(column=2, row=1)

        self.t4 = tk.Button(self.janela, text="4")
        self.t4.grid(column=0, row=2)

        self.t5 = tk.Button(self.janela, text="5")
        self.t5.grid(column=1, row=2)

        self.t6 = tk.Button(self.janela, text="6")
        self.t6.grid(column=2, row=2)

        self.t7 = tk.Button(self.janela, text="3")
        self.t7.grid(column=0, row=3)

        self.t8 = tk.Button(self.janela, text="2")
        self.t8.grid(column=1, row=3)

        self.t9 = tk.Button(self.janela, text="1")
        self.t9.grid(column=2, row=3)

        self.t10 = tk.Button(self.janela, text="0")
        self.t10.grid(column=0, row=4, rowspan=2, sticky=tk.NS)

        self.t12 = tk.Button(self.janela, text="=")
        self.t12.grid(column=2, row=5, columnspan=2, sticky=tk.EW)

        self.t13 = tk.Button(self.janela, text="/")
        self.t13.grid(column=3, row=1)

        self.t14 = tk.Button(self.janela, text="x")
        self.t14.grid(column=3, row=2)

        self.t15 = tk.Button(self.janela, text="-")
        self.t15.grid(column=3, row=3)

        self.t16 = tk.Button(self.janela, text="/")
        self.t16.grid(column=3, row=1)

        self.t17 = tk.Button(self.janela, text="x")
        self.t17.grid(column=3, row=2)

        self.t18 = tk.Button(self.janela, text=".")
        self.t18.grid(column=1, row=4)

        self.t19 = tk.Button(self.janela, text="%")
        self.t19.grid(column=2, row=4)

        self.t20 = tk.Button(self.janela, text="C")
        self.t20.grid(column=1, row=5)

        self.t21 = tk.Button(self.janela, text="+")
        self.t21.grid(column=3, row=4)

app = tk.Tk()
Tela(app)
app.mainloop()