import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from trabalho.banco import Banco
from trabalho.cliente import Cliente
from trabalho.contaCorrente import ContaCorrente
from trabalho.contaPoupanca import ContaPoupanca


class Tela(ContaCorrente, ContaPoupanca, Cliente, Banco):
    def banco(self):
        self.banco = tk.Toplevel()
        self.banco.title("Banco")
        self.banco.geometry('300x150')
        self.janela.grab_set()

        #Botões
        self.btn_cadastrar = tk.Button(self.banco, text="Cadastrar", command=self.cadastrar_banco)
        self.btn_cadastrar.grid(column=0, row=0)

        self.btn_mostrar = tk.Button(self.banco, text="Mostrar", command=self.mostrar_banco)
        self.btn_mostrar.grid(column=1, row=0)

        self.btn_atualizar = tk.Button(self.banco, text="Atualizar", command=self.atualizar_banco)
        self.btn_atualizar.grid(column=2, row=0)

    def cadastrar_banco(self):
        self.cadastro_banco = tk.Toplevel()
        self.cadastro_banco.title("Cadastrar Banco")
        self.cadastro_banco.geometry("400x200")
        self.banco.iconify()

        self.btn_num_bc = tk.Label(self.cadastro_banco, text="Número")
        self.btn_num_bc.grid(column=0, row=0)
        self.ent_num_bc = tk.Entry(self.cadastro_banco)
        self.ent_num_bc.grid(column=1, row=0)

        self.btn_nome_bc = tk.Label(self.cadastro_banco, text="Nome")
        self.btn_nome_bc.grid(column=0, row=1)
        self.ent_nome_bc = tk.Entry(self.cadastro_banco)
        self.ent_nome_bc.grid(column=1, row=1)

        self.btn_salvar_bc = tk.Button(self.cadastro_banco, text="Salvar", command=self.confirmar_cadastro_banco)
        self.btn_salvar_bc.grid(column=1, row=3, columnspan=2)

    def confirmar_cadastro_banco(self):
        nome = self.ent_nome_bc.get()
        nome = Banco(self.ent_num_bc.get(), self.ent_nome_bc.get())
        Banco.adicionar_banco(self, nome)
        for i in Banco.bancos:
            print(i.nome)
        self.cadastro_banco.destroy()
        self.banco.deiconify()

    def mostrar_banco(self):
        self.mostrar_banco = tk.Toplevel()
        self.mostrar_banco.title("Bancos")
        self.mostrar_banco.geometry("800x600")
        self.selecionado = tk.StringVar()
        self.cbx_mostrar_banco = ttk.Combobox(self.mostrar_banco, textvariable=self.selecionado)
        self.cbx_mostrar_banco['values'] = Banco.bancos
        self.cbx_mostrar_banco['state'] = 'readonly'
        self.cbx_mostrar_banco.current(0)
        self.cbx_mostrar_banco.pack()

        self.btn_selecionar = tk.Button(self.mostrar_banco, text="Selecionar", command=self.banco_selecionado)
        self.btn_selecionar.pack()

        colunas = ["número", "nome"]
        self.tvw_banco_selecionado = ttk.Treeview(self.mostrar_banco, columns=colunas, show="headings")
        self.tvw_banco_selecionado.pack(side=tk.LEFT, fill=tk.BOTH)

        # Cabeçalho
        self.tvw_banco_selecionado.heading(colunas[0], text='Número')
        self.tvw_banco_selecionado.heading(colunas[1], text='Nome')
        # self.tvw_banco_selecionado.heading(colunas[2], text='Contas')

        # Tamanho
        self.tvw_banco_selecionado.column(colunas[0], minwidth=0, width=111)
        self.tvw_banco_selecionado.column(colunas[1], minwidth=0, width=170)
        # self.tvw_banco_selecionado.column(colunas[2], minwidth=0, width=111)

        self.tvw_banco_selecionado.insert("", tk.END, values=("Elias Cacau", 123456))
        self.tvw_banco_selecionado.insert("", tk.END, values=("Danone Player", 654789))
        self.tvw_banco_selecionado.insert("", tk.END, values=("Luiz Eduardo", 654321))

    def banco_selecionado(self):
        valor = self.selecionado.get()
        for i in Banco.bancos:
            if valor == i.nome:
                banco_selecionado = i
        todos = self.tvw_banco_selecionado.get_children()
        for i in todos:
            self.tvw_banco_selecionado.delete(i)
        self.tvw_banco_selecionado.insert("", tk.END, values=(banco_selecionado.nome, banco_selecionado.num))

    def atualizar_banco(self):
        self.atualizar_banco = tk.Toplevel()
        self.atualizar_banco.title("Atualizar Banco")
        self.atualizar_banco.geometry("800x600")
        self.banco.iconify()

        colunas = ["número", "nome"]
        self.tvw_banco_selecionado = ttk.Treeview(self.atualizar_banco, columns=colunas, show="headings")
        self.tvw_banco_selecionado.pack(side=tk.LEFT, fill=tk.BOTH)

        # Cabeçalho
        self.tvw_banco_selecionado.heading(colunas[0], text='Número')
        self.tvw_banco_selecionado.heading(colunas[1], text='Nome')
        # self.tvw_banco_selecionado.heading(colunas[2], text='Contas')

        # Tamanho
        self.tvw_banco_selecionado.column(colunas[0], minwidth=0, width=111)
        self.tvw_banco_selecionado.column(colunas[1], minwidth=0, width=170)
        # self.tvw_banco_selecionado.column(colunas[2], minwidth=0, width=111)

        for i in Banco.bancos:
            self.tvw_banco_selecionado.insert("", tk.END, values=(i.nome, i.num))

        self.btn_atualizar_banco = tk.Button(self.atualizar_banco, text="Editar", command=self.editar_banco)
        self.btn_atualizar_banco.pack(side=tk.LEFT)

    def editar_banco(self):
        self.top_editar_banco = tk.Toplevel()
        self.top_editar_banco.title("Editar banco")
        self.lbl_num = tk.Label(self.top_editar_banco, text='Número:')
        self.lbl_num.grid(column=0, row=0)

        self.lbl_nome = tk.Label(self.top_editar_banco, text='Nome:')
        self.lbl_nome.grid(column=0, row=1)

        selecionado = self.tvw_banco_selecionado.selection()
        lista = self.tvw_banco_selecionado.item(selecionado, "values")

        self.entry_num = tk.Entry(self.top_editar_banco, width=30)
        self.entry_num.grid(column=1, row=0)
        self.entry_num.insert(0, lista[0])

        self.entry_nome = tk.Entry(self.top_editar_banco, width=30)
        self.entry_nome.grid(column=1, row=1)
        self.entry_nome.insert(0, lista[1])

        self.btn_confirmar = tk.Button(self.top_editar_banco, text='Confirmar', command=self.confirmar_edicao)
        self.btn_confirmar.grid(column=1, row=3, columnspan=1)

    def confirmar_edicao(self):
        num = self.entry_num.get()
        nome = self.entry_nome.get()
        selecionado = self.tvw_banco_selecionado.selection()
        #print(selecionado)
        # lista = self.tvw_banco_selecionado.item(selecionado, "values")
        # if num == lista[0] and nome == lista[1]:
        #     mensagem = messagebox.askyesno('Nenhuma modificação feita!', 'Você tem certeza que não deseja fazer nenhuma modificação?', parent=self.top_atualizar)
        #     if mensagem == False:
        #         self.banco.deiconify()
        #     else:
        #         self.top_editar_banco.destroy()
        # else:
        #     mensagem = messagebox.askyesno('Modificação feita!', 'Você tem certeza que deseja confirmar as alterações?', parent=self.top_atualizar)
        #     if mensagem == False:
        #         self.banco.deiconify()
        #     else:
        self.tvw_banco_selecionado.item(selecionado, values=(num, nome))
        self.top_editar_banco.destroy()

    def cadastro_contaPoupanca(self):
        self.contaPopuanca = tk.Toplevel()
        self.contaPopuanca.geometry("400x200")
        self.btn_nome_cp = tk.Label(self.contaPopuanca, text="Cliente")
        self.btn_nome_cp.grid(column=0, row=0)
        self.ent_nome_cp = tk.Entry(self.contaPopuanca)
        self.ent_nome_cp.grid(column=1, row=0)

        self.btn_num_cp = tk.Label(self.contaPopuanca, text="Número")
        self.btn_num_cp.grid(column=0, row=1)
        self.ent_num_cp = tk.Entry(self.contaPopuanca)
        self.ent_num_cp.grid(column=1, row=1)

        self.btn_saldo_cp = tk.Label(self.contaPopuanca, text="Saldo")
        self.btn_saldo_cp.grid(column=0, row=2)
        self.ent_saldo_cp = tk.Entry(self.contaPopuanca)
        self.ent_saldo_cp.grid(column=1, row=2)

        self.btn_salvar_cp = tk.Button(self.contaPopuanca, text="Salvar")
        self.btn_salvar_cp.grid(column=1, row=3, columnspan=2)

    def conta(self):
        self.conta = tk.Toplevel()
        self.conta.title("Conta")
        self.conta.geometry('800x600')
        self.janela.grab_set()

        # CONTA CORRENTE
        self.nome_contaCorrente = tk.Label(self.conta, text="Conta Corrente")
        self.nome_contaCorrente.pack(side=tk.TOP, fill=tk.X)
        self.frm_contaCorrente = tk.Frame(self.conta)
        self.frm_contaCorrente.pack(side=tk.BOTTOM)
        self.btn_contaCorrente = tk.Button(self.frm_contaCorrente, text="Conta Corrente")
        self.btn_contaCorrente.pack(side=tk.LEFT)

        colunas = ['num', 'cli', 'saldo']

        self.tvw_contaCorrente = ttk.Treeview(self.conta, columns=colunas, show="headings")
        self.tvw_contaCorrente.pack(side=tk.LEFT, fill=tk.BOTH)

        # Cabeçalho
        self.tvw_contaCorrente.heading(colunas[0], text='Número')
        self.tvw_contaCorrente.heading(colunas[1], text='Cliente')
        self.tvw_contaCorrente.heading(colunas[2], text='Saldo')

        # Tamanho
        self.tvw_contaCorrente.column(colunas[0], minwidth=0, width=111)
        self.tvw_contaCorrente.column(colunas[1], minwidth=0, width=170)
        self.tvw_contaCorrente.column(colunas[2], minwidth=0, width=111)


        # CONTA POUPANCA
        self.nome_contaPoupanca = tk.Label(self.conta, text="Conta Poupança")
        self.nome_contaPoupanca.pack(side=tk.TOP)

        self.frm_contaPoupanca = tk.Frame(self.conta)
        self.frm_contaPoupanca.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.btn_contaPoupanca = tk.Button(self.frm_contaCorrente, text="Conta Poupança", command=self.cadastro_contaPoupanca)
        self.btn_contaPoupanca.pack(side=tk.LEFT)


        colunas = ['num', 'cli', 'saldo']

        self.tvw_contaPoupanca = ttk.Treeview(self.conta, columns=colunas, show="headings")
        self.tvw_contaPoupanca.pack(side=tk.LEFT, fill=tk.BOTH)

        # Cabeçalho
        self.tvw_contaPoupanca.heading(colunas[0], text='Número')
        self.tvw_contaPoupanca.heading(colunas[1], text='Cliente')
        self.tvw_contaPoupanca.heading(colunas[2], text='Saldo')

        # Tamanho
        self.tvw_contaPoupanca.column(colunas[0], minwidth=0, width=110)
        self.tvw_contaPoupanca.column(colunas[1], minwidth=0, width=170)
        self.tvw_contaPoupanca.column(colunas[2], minwidth=0, width=110)


    def cliente(self):
        self.btn_cliente = tk.Toplevel()
        self.btn_cliente.title("Banco")
        self.btn_cliente.geometry('300x150')
        self.janela.grab_set()

    def __init__(self, master):
        self.janela = master
        self.janela.title("Menu")
        self.janela.geometry("500x300")
        self.frame_botoes = tk.Frame()
        self.frame_botoes.grid(column=0, row=0)

        #botões
        self.btn_banco = tk.Button(self.janela, text="Banco", command=self.banco)
        self.btn_banco.grid(column=0, row=0)

        self.btn_conta = tk.Button(self.janela, text="Conta", command=self.conta)
        self.btn_conta.grid(column=1, row=0)

        self.btn_cliente = tk.Button(self.janela, text="Cliente", command=self.cliente)
        self.btn_cliente.grid(column=2, row=0)

app = tk.Tk()
Tela(app)
app.mainloop()