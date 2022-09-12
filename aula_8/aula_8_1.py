import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Tela:
    def deletar_selecionado(self):
        selecionado = self.tvw.selection()
        if selecionado != ():
            messagem = messagebox.askyesno("Cuidado!", "Tem certeza que deseja apagar?")
            if messagem:
                self.tvw.delete(selecionado)

    def deletar_todos(self):
        todos = self.tvw.get_children()
        if todos != ():
            messagem = messagebox.askyesno("Cuidado!", "Tem certeza que deseja apagar todos cadastros?")
            if messagem:
                for t in todos:
                    self.tvw.delete(t)

    def deletar_lista(self):
        lista = self.tvw.selection()
        if lista != ():
            messagem = messagebox.askyesno("Cuidado!", "Tem certeza que deseja apagar o(s) itens selecionado(s)?")
            if messagem:
                for l in lista:
                    self.tvw.delete(l)

    def tela_atualizar_click(self):
        selecionado = self.tvw.selection()
        if len(selecionado) == 1:
            self.tela_atualizar()
        elif len(selecionado) >= 1:
            messagebox.showwarning("Aviso!", "Selecione apenas um item")
        elif len(selecionado) < 1:
            messagebox.showwarning("Aviso!", "Selecione um item")


    def tela_atualizar(self):
        self.top_atualizar = tk.Toplevel()
        self.top_atualizar.title('Atualizar')
        self.top_atualizar.geometry('300x150')
        self.janela.grab_set()
        # self.janela.withdraw()

        self.lbl_nome = tk.Label(self.top_atualizar, text='Nome:')
        self.lbl_nome.grid(column=0, row=0)
        self.lbl_cpf = tk.Label(self.top_atualizar, text='CPF:')
        self.lbl_cpf.grid(column=0, row=1)
        self.lbl_email = tk.Label(self.top_atualizar, text='E-Mail:')
        self.lbl_email.grid(column=0, row=2)

        # Selecionando as informações do TreeView
        selecionado = self.tvw.selection()
        lista = self.tvw.item(selecionado, "values")

        self.entry_nome = tk.Entry(self.top_atualizar, width=30)
        self.entry_nome.grid(column=1, row=0)
        self.entry_nome.insert(0, lista[0])

        self.entry_cpf = tk.Entry(self.top_atualizar, width=30)
        self.entry_cpf.grid(column=1, row=1)
        self.entry_cpf.insert(0, lista[1])

        self.entry_email = tk.Entry(self.top_atualizar, width=30)
        self.entry_email.grid(column=1, row=2)
        self.entry_email.insert(0, lista[2])

        self.btn_confirmar = tk.Button(self.top_atualizar, text='Confirmar', command=self.confirmar_atualizacao)
        self.btn_confirmar.grid(column=1, row=3, columnspan=1)

    def confirmar_atualizacao(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()
        selecionado = self.tvw.selection()
        lista = self.tvw.item(selecionado, "values")
        if nome == lista[0] and cpf == lista[1] and email == lista[2]:
            mensagem = messagebox.askyesno('Nenhuma modificação feita!', 'Você tem certeza que não deseja fazer nenhuma modificação?', parent=self.top_atualizar)
            if mensagem == False:
                self.janela.deiconify()
            else:
                self.top_atualizar.destroy()
        else:
            mensagem = messagebox.askyesno('Modificação feita!', 'Você tem certeza que deseja confirmar as alterações?', parent=self.top_atualizar)
            if mensagem == False:
                self.janela.deiconify()
            else:
                self.tvw.item(selecionado, values=(nome, cpf, email))
                self.top_atualizar.destroy()
                self.janela.deiconify()

    def tela_cadastrar(self):
        self.top_cadastro = tk.Toplevel()
        self.top_cadastro.title('Cadastro')
        self.top_cadastro.geometry('300x150')
        self.janela.grab_set()

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
            messagebox.showwarning('CAMPOS VAZIOS!', 'Todos os campos estão vazios!', parent=self.top_cadastro)
        elif self.entry_nome.get() == '' and self.entry_cpf.get() == '':
            messagebox.showwarning('CAMPOS Nome e CPF VAZIOS!', 'Os campos Nome e CPF estão vazios!', parent=self.top_cadastro)
        elif self.entry_nome.get() == '' and self.entry_email.get() == '':
            messagebox.showwarning('CAMPOS Nome e E-Mail VAZIOS!', 'Os campos Nome e E-Mail estão vazios!', parent=self.top_cadastro)
        elif self.entry_cpf.get() == '' and self.entry_email.get() == '':
            messagebox.showwarning('CAMPOS CPF e E-Mail VAZIOS!', 'Os campos CPF e E-Mail estão vazios!', parent=self.top_cadastro)
        elif self.entry_nome.get() == '':
            messagebox.showwarning('NOME VAZIO!', 'Campo Nome vazio!', parent=self.top_cadastro)
        elif self.entry_cpf.get() == '':
            messagebox.showwarning('CPF VAZIO!', 'Campo CPF vazio!', parent=self.top_cadastro)
        elif self.entry_email.get() == '':
            messagebox.showwarning('E-Mail VAZIO!', 'Campo E-Mail vazio!', parent=self.top_cadastro)
        else:
            self.tvw.insert("", tk.END, values=(self.entry_nome.get(), self.entry_cpf.get(), self.entry_email.get()))
            self.top_cadastro.destroy()
            self.janela.deiconify()


    def __init__(self, master):
        self.janela = master
        self.janela.title("Treeview")
        self.janela.geometry("540x300")
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
        self.tvw.column(colunas[0], minwidth=0, width=175)
        self.tvw.column(colunas[1], minwidth=0, width=125)
        self.tvw.column(colunas[2], minwidth=0, width=225)

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
        self.btn_cadastrar.pack(side=tk.LEFT)

        self.btn_deletar = tk.Button(self.frm_botoes, text='Deletar', command=self.deletar_selecionado)
        self.btn_deletar.pack(side=tk.LEFT)

        self.btn_deletar_todos = tk.Button(self.frm_botoes, text='Deletar Todos', command=self.deletar_todos)
        self.btn_deletar_todos.pack(side=tk.LEFT)

        self.btn_deletar_lista = tk.Button(self.frm_botoes, text='Deletar Selecionados', command=self.deletar_lista)
        self.btn_deletar_lista.pack(side=tk.LEFT)

        self.btn_atualizar = tk.Button(self.frm_botoes, text='Atualizar', command=self.tela_atualizar_click)
        self.btn_atualizar.pack(side = tk.LEFT)

app = tk.Tk()
Tela(app)
app.mainloop()