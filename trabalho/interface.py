import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from trabalho.banco import Banco
from trabalho.cliente import Cliente
from trabalho.contaCorrente import ContaCorrente
from trabalho.contaPoupanca import ContaPoupanca
import sys

class Tela(ContaCorrente, ContaPoupanca, Cliente, Banco):
    def cliente(self):
        self.cliente = tk.Toplevel()
        self.cliente.title("Cliente")
        self.cliente.geometry("412x300")

        self.frm_cli_botoes = tk.Frame(self.cliente)
        self.frm_cli_botoes.pack(side=tk.TOP)

        # Treeview
        colunas = ['id', 'nome', 'cpf', 'endereco']
        self.tvw_cliente = ttk.Treeview(self.cliente, columns=colunas, show="headings")
        self.tvw_cliente.pack(side=tk.LEFT, fill=tk.BOTH)

        # Cabeçalho
        self.tvw_cliente.heading(colunas[0], text='Id')
        self.tvw_cliente.heading(colunas[1], text='Nome')
        self.tvw_cliente.heading(colunas[2], text='CPF')
        self.tvw_cliente.heading(colunas[3], text='Endereço')

        # Tamanho
        self.tvw_cliente.column(colunas[0], minwidth=0, width=20)
        self.tvw_cliente.column(colunas[0], minwidth=0, width=106)
        self.tvw_cliente.column(colunas[1], minwidth=0, width=160)
        self.tvw_cliente.column(colunas[2], minwidth=0, width=106)

        #Conteúdo
        cliente = Cliente("Elias Cacau", "024.631.012-02", "Rua Ametista")
        Cliente.adicionar_clientes(self, cliente)
        self.tvw_cliente.insert("", tk.END, values=(cliente.id, cliente.nome, cliente.cpf, cliente.endereco))

        #Scrollbar
        self.scr_cliente = ttk.Scrollbar(self.cliente, command=self.tvw_cliente.yview)
        self.scr_cliente.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw_cliente.configure(yscroll=self.scr_cliente.set)

        #Botões
        self.btn_cli_cadastrar = tk.Button(self.frm_cli_botoes, text="Cadastrar", command=self.cadastrar_cliente)
        self.btn_cli_cadastrar.pack(side=tk.LEFT)

        # self.btn_cli_editar = tk.Button(self.frm_cli_botoes, text="Editar", command=self.editar_cliente)
        # self.btn_cli_editar.pack(side=tk.LEFT, padx=5)

        self.btn_cli_excluir = tk.Button(self.frm_cli_botoes, text="Excluir", command=self.excluir_cliente)
        self.btn_cli_excluir.pack(side=tk.LEFT)


    def cadastrar_cliente(self):
        self.cadastrar_cliente = tk.Toplevel()
        self.cadastrar_cliente.title("Cadastrar Banco")
        self.cadastrar_cliente.geometry("200x100")

        self.btn_nome_cli = tk.Label(self.cadastrar_cliente, text="Nome")
        self.btn_nome_cli.grid(column=0, row=0)
        self.ent_nome_cli = tk.Entry(self.cadastrar_cliente)
        self.ent_nome_cli.grid(column=1, row=0)

        self.btn_cpf_cli = tk.Label(self.cadastrar_cliente, text="CPF")
        self.btn_cpf_cli.grid(column=0, row=1)
        self.ent_cpf_cli = tk.Entry(self.cadastrar_cliente)
        self.ent_cpf_cli.grid(column=1, row=1)

        self.btn_end_cli = tk.Label(self.cadastrar_cliente, text="Endereço")
        self.btn_end_cli.grid(column=0, row=2)
        self.ent_end_cli = tk.Entry(self.cadastrar_cliente)
        self.ent_end_cli.grid(column=1, row=2)

        self.btn_salvar_cli = tk.Button(self.cadastrar_cliente, text="Salvar", command=self.confirmar_cadastrar_cliente)
        self.btn_salvar_cli.grid(column=1, row=3, columnspan=2)

    def confirmar_cadastrar_cliente(self):
        Cliente.adicionar_clientes(self, Cliente(self.ent_nome_cli.get(), self.ent_cpf_cli.get(), self.ent_end_cli.get()))
        self.tvw_cliente.insert("", tk.END, values=(self.ent_nome_cli.get(), self.ent_cpf_cli.get(), self.ent_end_cli.get()))
        self.cadastrar_cliente.destroy()

    def excluir_cliente(self):
        selecionado = self.tvw_cliente.selection()
        lista = self.tvw_cliente.item(selecionado, "values")
        if lista != ():
            messagem = messagebox.askyesno("Cuidado!", "Tem certeza que deseja apagar o(s) itens selecionado(s)?")
            if messagem:
                for l in lista:
                    for cli in Cliente.clientes:
                        if l == cli.nome:
                            Cliente.clientes.remove(cli)
                for s in selecionado:
                    self.tvw_cliente.delete(s)
            self.cliente.deiconify()

    def editar_cliente(self):
        self.top_editar_cliente = tk.Toplevel()
        self.top_editar_cliente.title("Editar banco")
        self.top_editar_cliente.geometry("200x100")

        selecionado = self.tvw_cliente.selection()
        lista = self.tvw_cliente.item(selecionado, "values")

        self.btn_nome_cli = tk.Label(self.top_editar_cliente, text="Nome:")
        self.btn_nome_cli.grid(column=0, row=0)
        self.ent_nome_cli = tk.Entry(self.top_editar_cliente)
        self.ent_nome_cli.grid(column=1, row=0)
        self.ent_nome_cli.insert(0, lista[0])

        self.btn_cpf_cli = tk.Label(self.top_editar_cliente, text="CPF:")
        self.btn_cpf_cli.grid(column=0, row=1)
        self.ent_cpf_cli = tk.Entry(self.top_editar_cliente)
        self.ent_cpf_cli.grid(column=1, row=1)
        self.ent_cpf_cli.insert(0, lista[1])

        self.btn_end_cli = tk.Label(self.top_editar_cliente, text="Endereço:")
        self.btn_end_cli.grid(column=0, row=2)
        self.ent_end_cli = tk.Entry(self.top_editar_cliente)
        self.ent_end_cli.grid(column=1, row=2)
        self.ent_end_cli.insert(0, lista[2])

        self.btn_confirmar = tk.Button(self.top_editar_cliente, text='Confirmar', command=self.confirmar_edicao_cliente)
        self.btn_confirmar.grid(column=1, row=3, columnspan=1)

    def confirmar_edicao_cliente(self):
        nome = self.ent_nome_cli.get()
        cpf = self.ent_cpf_cli.get()
        end = self.ent_end_cli.get()
        selecionado = self.tvw_cliente.selection()
        lista = self.tvw_cliente.item(selecionado, "values")

        for i in Cliente.clientes:
            if nome == i.nome:
                i.nome = nome
                i.cpf = cpf
                i.endereco = end

        if nome == lista[0] and cpf == lista[1] and end == lista[2]:
            mensagem = messagebox.askyesno('Nenhuma modificação feita!', 'Você tem certeza que não deseja fazer nenhuma modificação?', parent=self.cliente)
            if mensagem:
                self.top_editar_cliente.destroy()
            else:
                self.top_editar_cliente.deiconify()
        else:
            mensagem = messagebox.askyesno('Modificação feita!', 'Você tem certeza que deseja confirmar as alterações?', parent=self.cliente)
            if mensagem:
                self.tvw_cliente.item(selecionado, values=(nome, cpf, end))
                self.top_editar_cliente.destroy()
            else:
                self.top_editar_cliente.deiconify()

    def conta(self):
        self.conta = tk.Toplevel()
        self.conta.title("Contas")
        self.conta.geometry("500x312")
        self.btn_conta_corrente = tk.Button(self.conta, font=("Verdana", 12), text="Conta Corrente", bg="#9cd7ff", command=self.conta_corrente)
        self.btn_conta_corrente.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.btn_conta_poupanca = tk.Button(self.conta, font=("Verdana", 12), text="Conta Popuança", bg="#6695fa")
        self.btn_conta_poupanca.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def conta_corrente(self):
        self.conta_corrente = tk.Toplevel()
        self.conta_corrente.title("Conta Corrente")
        self.conta_corrente.geometry("412x300")

        self.frm_cc = tk.Frame(self.conta_corrente)
        self.frm_cc.pack(side=tk.BOTTOM)

        print(Cliente.clientes)
        self.selecionado = tk.StringVar()
        self.cbx_conta_corrente = ttk.Combobox(self.conta_corrente, textvariable=self.selecionado)
        self.cbx_conta_corrente['values'] = Cliente.clientes
        self.cbx_conta_corrente['state'] = 'readonly'
        self.cbx_conta_corrente.current(0)
        self.cbx_conta_corrente.pack()

        self.btn_selecionar = tk.Button(self.conta_corrente, text="Selecionar")
        self.btn_selecionar.pack()

        colunas = ['numero', 'titular', 'saldo']
        self.tvw_conta_corrente = ttk.Treeview(self.conta_corrente, columns=colunas, show="headings")
        self.tvw_conta_corrente.pack(side=tk.LEFT, fill=tk.BOTH)

        # Cabeçalho
        self.tvw_conta_corrente.heading(colunas[0], text='Número')
        self.tvw_conta_corrente.heading(colunas[1], text='Titular')
        self.tvw_conta_corrente.heading(colunas[2], text='Saldo')

        # Tamanho
        self.tvw_conta_corrente.column(colunas[0], minwidth=0, width=111)
        self.tvw_conta_corrente.column(colunas[1], minwidth=0, width=170)
        self.tvw_conta_corrente.column(colunas[2], minwidth=0, width=111)

        # Conteúdo
        self.tvw_conta_corrente.insert("", tk.END, values=(123, "Elias Cacau", 1500))

        # Scrollbar
        self.scr_cliente = ttk.Scrollbar(self.conta_corrente, command=self.tvw_conta_corrente.yview)
        self.scr_cliente.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw_conta_corrente.configure(yscroll=self.scr_cliente.set)

        # Botões
        self.btn_cc_cadastrar = tk.Button(self.frm_cc, text="Depositar")
        #self.btn_cc_cadastrar = tk.Button(self.frm_cc_botoes, text="Cadastrar", command=self.cadastrar_conta_corrente)
        self.btn_cc_cadastrar.pack(side=tk.LEFT)

        # self.btn_cli_editar = tk.Button(self.frm_cli_botoes, text="Editar", command=self.editar_cliente)
        # self.btn_cli_editar.pack(side=tk.LEFT, padx=5)

        self.btn_cc_encerrar = tk.Button(self.frm_cc, text="Sacar")
        #self.btn_cc_encerrar = tk.Button(self.frm_cc_botoes, text="Excluir", command=self.encerrar_conta_corrente)
        self.btn_cc_encerrar.pack(side=tk.LEFT)

    def conta_corrente_selecionada(self):
        valor = self.selecionado.get()
        for i in Cliente.clientes:
            if valor == i.nome:
                cliente_selecionado = i
        todos = self.tvw_conta_corrente.get_children()
        for i in todos:
            self.tvw_conta_corrente.delete(i)
        #self.tvw_conta_corrente.insert("", tk.END, values=(cliente_selecionado.num, cliente_selecionado.num))
    #
    # def encerrar_conta_corrente(self):
    #     pass

    def __init__(self, master):
        self.janela = master
        self.janela.title("Menu")
        self.janela.geometry("500x312")

        # botões
        self.btn_cliente = tk.Button(self.janela, text="Cliente", font=("Verdana", 12), height=5, bg='#9cd7ff', command=self.cliente)
        self.btn_cliente.pack(fill=tk.BOTH)

        self.btn_conta = tk.Button(self.janela, text="Conta", font=("Verdana", 12), height=5, bg='#6695fa', command=self.conta)
        self.btn_conta.pack(fill=tk.BOTH)

        self.btn_banco = tk.Button(self.janela, text="Banco", font=("Verdana", 12), height=5, bg='#375898')
        self.btn_banco.pack(fill=tk.BOTH)

sys.setrecursionlimit(1500)
app = tk.Tk()
Tela(app)
app.mainloop()