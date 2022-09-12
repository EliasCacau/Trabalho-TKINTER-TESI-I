import tkinter as tk
janela = tk.Tk()
janela.geometry("350x300")
janela.title('Frames')

frameH = tk.LabelFrame(janela, text="Ratinho")
frameH.pack()
but1 = tk.Button(frameH, text="UEPÁ").pack(side=tk.LEFT)
but2 = tk.Button(frameH, text="RAPAZ").pack(side=tk.LEFT)
but3 = tk.Button(frameH, text="ELE GOSTAAA!!!").pack(side=tk.LEFT)


frameV = tk.LabelFrame(janela, text="Rodrigo Faro")
frameV.pack()
but4 = tk.Button(frameV, text="DANÇA GATINHO").pack(side=tk.BOTTOM)
but5 = tk.Button(frameV, text="UUUUUIIIIIIIII!!!").pack(side=tk.BOTTOM)
but6 = tk.Button(frameV, text="TOME").pack(side=tk.BOTTOM)


janela.mainloop()