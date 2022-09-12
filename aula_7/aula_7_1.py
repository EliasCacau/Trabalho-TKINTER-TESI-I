import tkinter as tk
from tkinter import messagebox

def info():
    messagebox.showinfo("Info", "Informo que você é gay")

def aviso():
    messagebox.showwarning("Aviso", "AVISEI QUE VOCE É GAY!!!!")

def error():
    messagebox.showerror("Error", "Error!!!\nViado detectado!")

def pergunta():
    teste = messagebox.askyesno("Sim ou não?", "Você é gay?")
    if teste:
        top = tk.Toplevel()
        top.geometry("300x200")
        bttop = tk.Label(top, text="SABIA QUE VOCE ERA GAY!", font="20", bg="Red").pack(expand=True, fill=tk.BOTH)

janela = tk.Tk()
janela.title('Messagebox')
janela.geometry('300x200')

btn1 = tk.Button(janela, text='Info', command=info)
btn1.pack()

btn2 = tk.Button(janela, text='Aviso', command=aviso)
btn2.pack()

btn3 = tk.Button(janela, text='Error', command=error)
btn3.pack()

btn4 = tk.Button(janela, text="Tu é?", command=pergunta)
btn4.pack()

janela.mainloop()