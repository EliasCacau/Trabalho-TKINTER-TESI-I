import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Tela:
    def deletar_selecionado(self):
        selecionado = self.tvw.selection()
        self.tvw.delete(selecionado)

    def tela_cadastrar(self):
        self.top_cadastro = tk.Toplevel()
        self.top_cadastro.title('Cadastro')
        self.top_cadastro.geometry('300x150')
        self.janela.grab_set()
        #self.janela.withdraw()

        self.lbl_nome = tk.Label(self.top_cadastro, text='Nome:')
        self.lbl_nome.grid(column=0, row=0)
        self.lbl_cpf = tk.Label(self.top_cadastro, text='CPF:')
        self.lbl_cpf.grid(column=0, row=1)
        self.lbl_email = tk.Label(self.top_cadastro, text='E-Mail:')
        self.lbl_email.grid(column=0, row=2)

        self.entry_nome = tk.Entry(self.top_cadastro, width=30)
        self.entry_nome.grid(column=1, row=0)
        self.entry_cpf = tk.Entry(self.top_cadastro, width=30)
        self.entry_cpf.grid(column=1, row=1)
        self.entry_email = tk.Entry(self.top_cadastro, width=30)
        self.entry_email.grid(column=1, row=2)

        self.btn_confirmar = tk.Button(self.top_cadastro, text='Confirmar', command=self.confirmar_cadastro)
        self.btn_confirmar.grid(column=1, row=3, columnspan=1)

    def confirmar_cadastro(self):
        if self.entry_nome.get() == '' and self.entry_cpf.get() == '' and self.entry_email.get() == '':
            messagebox.showwarning('CAMPOS VAZIOS!', 'Todos os campos estão vazios!')
            self.tela_cadastrar()
        elif self.entry_nome.get() == '' and self.entry_cpf.get() == '':
            messagebox.showwarning('CAMPOS Nome e CPF VAZIOS!', 'Os campos Nome e CPF estão vazios!')
            self.tela_cadastrar()
        elif self.entry_nome.get() == '' and self.entry_email.get() == '':
            messagebox.showwarning('CAMPOS Nome e E-Mail VAZIOS!', 'Os campos Nome e E-Mail estão vazios!')
            self.tela_cadastrar()
        elif self.entry_cpf.get() == '' and self.entry_email.get() == '':
            messagebox.showwarning('CAMPOS CPF e E-Mail VAZIOS!', 'Os campos CPF e E-Mail estão vazios!')
            self.tela_cadastrar()
        elif self.entry_nome.get() == '':
            messagebox.showwarning('NOME VAZIO!', 'Campo Nome vazio!')
            self.tela_cadastrar()
        elif self.entry_cpf.get() == '':
            messagebox.showwarning('CPF VAZIO!', 'Campo CPF vazio!')
            self.tela_cadastrar()
        elif self.entry_email.get() == '':
            messagebox.showwarning('E-Mail VAZIO!', 'Campo E-Mail vazio!')
            self.tela_cadastrar()
        else:
            self.tvw.insert("", tk.END, values=(self.entry_nome.get(), self.entry_cpf.get(), self.entry_email.get()))

        self.top_cadastro.destroy()
        self.janela.deiconify()

    def __init__(self, master):
        self.janela = master
        self.janela.title("Treeview")
        self.janela.geometry("470x300")
        self.frm_botoes = tk.Frame()
        self.frm_botoes.pack(side=tk.BOTTOM)

        colunas = ['nome', 'cpf', 'email']

        self.tvw = ttk.Treeview(self.janela, columns=colunas, show="headings")
        self.tvw.pack(side=tk.LEFT, fill=tk.BOTH)

        # Cabeçalho
        self.tvw.heading(colunas[0], text='Nome')
        self.tvw.heading(colunas[1], text='CPF')
        self.tvw.heading(colunas[2], text='E-mail')

        # Tamanho
        self.tvw.column(colunas[0], minwidth=0, width=100)
        self.tvw.column(colunas[1], minwidth=0, width=150)
        self.tvw.column(colunas[2], minwidth=0, width=200)

        # Conteudo
        self.tvw.insert("", tk.END, values=("Elias", "00000000000", "eliascacau@gmail.com"))
        self.tvw.insert("", tk.END, values=("Elias", "00000000000", "eliascacau@gmail.com"))
        self.tvw.insert("", tk.END, values=("Elias", "00000000000", "eliascacau@gmail.com"))
        self.tvw.insert("", tk.END, values=("Elias", "00000000000", "eliascacau@gmail.com"))
        self.tvw.insert("", tk.END, values=("Elias", "00000000000", "eliascacau@gmail.com"))
        self.tvw.insert("", tk.END, values=("Elias", "00000000000", "eliascacau@gmail.com"))
        self.tvw.insert("", tk.END, values=("Elias", "00000000000", "eliascacau@gmail.com"))
        self.tvw.insert("", tk.END, values=("Elias", "00000000000", "eliascacau@gmail.com"))
        self.tvw.insert("", tk.END, values=("Elias", "00000000000", "eliascacau@gmail.com"))
        self.tvw.insert("", tk.END, values=("Elias", "00000000000", "eliascacau@gmail.com"))



        self.scr = ttk.Scrollbar(self.janela, command=self.tvw.yview)
        self.scr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw.configure(yscroll=self.scr.set)

        # Botões
        self.btn_cadastrar = tk.Button(self.frm_botoes, text='Cadastrar', command=self.tela_cadastrar)
        self.btn_cadastrar.pack()

        self.btn_deletar = tk.Button(self.frm_botoes, text='Deletar', command=self.deletar_selecionado)
        self.btn_deletar.pack()


app = tk.Tk()
Tela(app)
app.mainloop()