import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as ms
from tkinter.scrolledtext import ScrolledText

def mostrar_arquivo():
    nome_arquivo = fd.askopenfilename()
    ms.showinfo("Aviso", f"{nome_arquivo}")

def carregar_arquivo():
    tipos = (("Texto", "*.txt"), ('PNG', '*.png'), ('Python', '*.py'))
    arquivo = fd.askopenfile(initialdir='/home/elias.cacau/Downloads',  filetypes=tipos)

    with open(arquivo.name, "r") as arq:
        for linha in arq:
            sct.insert(tk.END, linha)
        # for linha in arq:
        #     print(linha)

def salvar_arquivo():
    arquivo = fd.asksaveasfile()
    with open(arquivo.name, 'w') as arq:
        arq.write(sct.get('1.0', tk.END))

janela = tk.Tk()
janela.title("Eventos com arquivos")
janela.geometry("500x300")
#janela.configure(bg="black")
btn1 = tk.Button(janela, text="Mostrar arquivo", command=mostrar_arquivo, bg="Black", fg="White")
btn1.pack(fill=tk.BOTH, expand=True)
btn2 = tk.Button(janela, text="Carregar arquivo", command=carregar_arquivo, bg="Gray")
btn2.pack(fill=tk.BOTH, expand=True)

btn3 = tk.Button(janela, text="Salvar arquivo", command=salvar_arquivo, bg="brown")
btn3.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

sct = ScrolledText(janela, height=10)
sct.pack()

janela.mainloop()