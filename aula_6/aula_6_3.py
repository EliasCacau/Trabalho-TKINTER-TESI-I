import tkinter as tk

def abrir_toplevel():
    janela_toplevel = tk.Toplevel()
    janela_toplevel.title("JANELA OI")
    janela_toplevel.geometry("150x150")

janela = tk.Tk()
janela.geometry("800x500")
janela.title("JANMELASALALSKMDKNAESJNKJAENSJHASNEHAESHJKLÇNFSKJLSN")

btn = tk.Button(janela, text="CLICA EM MIM ARROMBADO!", font="Verdana, 30", fg="white", bg="red", command=abrir_toplevel).pack(fill=tk.BOTH, expand=True)
janela.mainloop()
