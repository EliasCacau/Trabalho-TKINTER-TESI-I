import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from trabalho.banco import Banco
from trabalho.cliente import Cliente
from trabalho.contaCorrente import ContaCorrente
from trabalho.contaPoupanca import ContaPoupanca
import sys

# COLOCAR MENU EM CIMA

class Tela(ContaCorrente, ContaPoupanca, Cliente, Banco):
    def __init__(self, master):
        cliente = Cliente("Elias de Olivera Cacau", "024.631.012-02", "Rua Letícia Rodrigues")
        Cliente.adicionar_clientes(self, cliente)
        banco = Banco(123, "Santander")
        Banco.adicionar_banco(self, banco)
        def cliente(event):
            self.cliente = tk.Toplevel()
            self.cliente.title("Cliente")
            self.cliente.geometry("473x300")

            self.frm_cli_botoes = tk.Frame(self.cliente)
            self.frm_cli_botoes.pack(side=tk.BOTTOM)

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
            self.tvw_cliente.column(colunas[0], minwidth=0, width=25)
            self.tvw_cliente.column(colunas[1], minwidth=0, width=160)
            self.tvw_cliente.column(colunas[2], minwidth=0, width=111)
            self.tvw_cliente.column(colunas[3], minwidth=0, width=160)

            #Conteúdo
            for cliente in Cliente.clientes:
                self.tvw_cliente.insert("", tk.END, values=(cliente.id, cliente.nome, cliente.cpf, cliente.endereco))

            #Scrollbar
            self.scr_cliente = ttk.Scrollbar(self.cliente, command=self.tvw_cliente.yview)
            self.scr_cliente.pack(side=tk.LEFT, fill=tk.BOTH)
            self.tvw_cliente.configure(yscroll=self.scr_cliente.set)

            #Botões
            self.btn_cli_cadastrar = tk.Button(self.frm_cli_botoes, text="Cadastrar", command=cadastrar_cliente, bg="#9cd7ff")
            self.btn_cli_cadastrar.pack(side=tk.LEFT)

            # self.btn_cli_editar = tk.Button(self.frm_cli_botoes, text="Editar", command=editar_cliente)
            # self.btn_cli_editar.pack(side=tk.LEFT, padx=5)

            self.btn_cli_excluir = tk.Button(self.frm_cli_botoes, text="Excluir", command=excluir_cliente, bg="#9cd7ff")
            self.btn_cli_excluir.pack(side=tk.LEFT)

        def cadastrar_cliente():
            self.cadastrar_cliente = tk.Toplevel()
            self.cadastrar_cliente.title("Cadastrar Banco")
            self.cadastrar_cliente.geometry("250x100")

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

            self.btn_salvar_cli = tk.Button(self.cadastrar_cliente, text="Salvar", command=confirmar_cadastrar_cliente)
            self.btn_salvar_cli.grid(column=1, row=3, columnspan=2)

        def confirmar_cadastrar_cliente():
            cliente = Cliente(self.ent_nome_cli.get(), self.ent_cpf_cli.get(), self.ent_end_cli.get())
            Cliente.adicionar_clientes(self, cliente)
            self.tvw_cliente.insert("", tk.END, values=(cliente.id, cliente.nome, cliente.cpf, cliente.endereco))
            self.cadastrar_cliente.destroy()

        def excluir_cliente():
            selecionado = self.tvw_cliente.selection()
            lista = self.tvw_cliente.item(selecionado, "values")
            if lista != ():
                messagem = messagebox.askyesno("Cuidado!", "Tem certeza que deseja apagar o item selecionado?")
                if messagem:
                    for l in lista:
                        for cli in Cliente.clientes:
                            if l == cli.nome:
                                Cliente.clientes.remove(cli)
                    for s in selecionado:
                        self.tvw_cliente.delete(s)
                self.cliente.deiconify()

        def conta():
            self.conta = tk.Toplevel()
            self.conta.title("Contas")
            self.conta.geometry("500x312")
            self.btn_conta_corrente = tk.Button(self.conta, font=("Verdana", 12), text="Conta Corrente", bg="#9cd7ff",
                                                command=conta_corrente)
            self.btn_conta_corrente.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.btn_conta_poupanca = tk.Button(self.conta, font=("Verdana", 12), text="Conta Popuança", bg="#6695fa")
            self.btn_conta_poupanca.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        def conta_corrente():
            self.conta_corrente = tk.Toplevel()
            self.conta_corrente.title("Conta Corrente")
            self.conta_corrente.geometry("412x300")

            self.frm_cc = tk.Frame(self.conta_corrente)
            self.frm_cc.pack(side=tk.BOTTOM)

            colunas = ["id", "cliente", "número", "saldo"]
            self.tvw_conta_corrente = ttk.Treeview(self.conta_corrente, columns=colunas, show="headings")
            self.tvw_conta_corrente.pack(side=tk.LEFT, fill=tk.BOTH)

            # Cabeçalho
            self.tvw_conta_corrente.heading(colunas[0], text='Id')
            self.tvw_conta_corrente.heading(colunas[1], text='Cliente')
            self.tvw_conta_corrente.heading(colunas[2], text='Número')
            self.tvw_conta_corrente.heading(colunas[3], text='Saldo')
            # self.tvw_conta_corrente.heading(colunas[2], text='Banco')

            # Tamanho
            self.tvw_conta_corrente.column(colunas[0], minwidth=0, width=25)
            self.tvw_conta_corrente.column(colunas[1], minwidth=0, width=160)
            self.tvw_conta_corrente.column(colunas[2], minwidth=0, width=105)
            self.tvw_conta_corrente.column(colunas[3], minwidth=0, width=105)

            # Scrollbar
            self.scr_conta_corrente = ttk.Scrollbar(self.conta_corrente, command=self.tvw_conta_corrente.yview)
            self.scr_conta_corrente.pack(side=tk.LEFT, fill=tk.BOTH)
            self.tvw_conta_corrente.configure(yscroll=self.scr_conta_corrente.set)

            self.btn_cc_cadastrar = tk.Button(self.frm_cc, font=("Verdana", 12), text="Cadastrar", bg="#9cd7ff",
                                                command=cadastrar_cc)
            self.btn_cc_cadastrar.pack(side=tk.RIGHT, fill=tk.BOTH)
            self.btn_cc_depositar = tk.Button(self.frm_cc, font=("Verdana", 12), text="Depositar", bg="#9cd7ff",
                                              command=cadastrar_cc)
            self.btn_cc_depositar.pack(side=tk.RIGHT, fill=tk.BOTH)
            self.btn_cc_sacar = tk.Button(self.frm_cc, font=("Verdana", 12), text="Sacar", bg="#9cd7ff",
                                              command=cadastrar_cc)
            self.btn_cc_sacar.pack(side=tk.RIGHT, fill=tk.BOTH)
            self.btn_cc_extrato = tk.Button(self.frm_cc, font=("Verdana", 12), text="Extrato", bg="#9cd7ff",
                                              command=cadastrar_cc)
            self.btn_cc_extrato.pack(side=tk.RIGHT, fill=tk.BOTH)



            #
            # self.btn_selecionar = tk.Button(self.conta_corrente, text="Selecionar")
            # self.btn_selecionar.pack()
            #
            # colunas = ['numero', 'titular', 'saldo']
            # self.tvw_conta_corrente = ttk.Treeview(self.conta_corrente, columns=colunas, show="headings")
            # self.tvw_conta_corrente.pack(side=tk.LEFT, fill=tk.BOTH)
            #
            # # Cabeçalho
            # self.tvw_conta_corrente.heading(colunas[0], text='Número')
            # self.tvw_conta_corrente.heading(colunas[1], text='Titular')
            # self.tvw_conta_corrente.heading(colunas[2], text='Saldo')
            #
            # # Tamanho
            # self.tvw_conta_corrente.column(colunas[0], minwidth=0, width=111)
            # self.tvw_conta_corrente.column(colunas[1], minwidth=0, width=170)
            # self.tvw_conta_corrente.column(colunas[2], minwidth=0, width=111)
            #
            # # Conteúdo
            # self.tvw_conta_corrente.insert("", tk.END, values=(123, "Elias Cacau", 1500))
            #
            # # Scrollbar
            # self.scr_cliente = ttk.Scrollbar(self.conta_corrente, command=self.tvw_conta_corrente.yview)
            # self.scr_cliente.pack(side=tk.LEFT, fill=tk.BOTH)
            # self.tvw_conta_corrente.configure(yscroll=self.scr_cliente.set)
            #
            # # Botões
            # self.btn_cc_cadastrar = tk.Button(self.frm_cc, text="Depositar")
            # # self.btn_cc_cadastrar = tk.Button(self.frm_cc_botoes, text="Cadastrar", command=self.cadastrar_conta_corrente)
            # self.btn_cc_cadastrar.pack(side=tk.LEFT)
            #
            # # self.btn_cli_editar = tk.Button(self.frm_cli_botoes, text="Editar", command=self.editar_cliente)
            # # self.btn_cli_editar.pack(side=tk.LEFT, padx=5)
            #
            # self.btn_cc_encerrar = tk.Button(self.frm_cc, text="Sacar")
            # # self.btn_cc_encerrar = tk.Button(self.frm_cc_botoes, text="Excluir", command=self.encerrar_conta_corrente)
            # self.btn_cc_encerrar.pack(side=tk.LEFT)

        def cadastrar_cc():
            self.cadastrar_cc = tk.Toplevel()
            self.cadastrar_cc.geometry("800x600")
            self.lbl_cadastro_nome = tk.Label(self.cadastrar_cc, text="Selecione o cliente:")
            # self.lbl_cadastro_nome = tk.Label(self.cadastrar_cc, text="Selecione o cliente", font="Verdana, 12", bg="#6695fa")
            self.lbl_cadastro_nome.grid(column=0, row=0)
            self.selecionado_cliente = tk.StringVar()
            self.cbx_cc_cliente = ttk.Combobox(self.cadastrar_cc, textvariable=self.selecionado)
            self.cbx_cc_cliente['values'] = Cliente.clientes
            self.cbx_cc_cliente['state'] = 'readonly'
            self.cbx_cc_cliente.current(0)
            self.cbx_cc_cliente.grid(column=1, row=0)

            self.lbl_cadastro_num = tk.Label(self.cadastrar_cc, text="Número:")
            self.lbl_cadastro_num.grid(column=2, row=0)
            self.ent_cadastro_num = tk.Entry(self.cadastrar_cc)
            self.ent_cadastro_num.grid(column=3, row=0)

            self.selecionado = tk.StringVar()
            self.cbx_cc_banco = ttk.Combobox(self.cadastrar_cc, textvariable=self.selecionado)
            self.cbx_cc_banco['values'] = Banco.bancos
            self.cbx_cc_banco['state'] = 'readonly'
            self.cbx_cc_banco.current(0)
            self.cbx_cc_banco.grid(column=4, row=0)

        def banco():
            #banco1 = Banco("Elias Cacau", 123456)
            # banco2 = Banco("Danone Player", 654789)
            # banco3 = Banco("Luiz Eduardo", 654321)

            #Banco.adicionar_banco(self, banco1)
            # Banco.adicionar_banco(self, banco2)
            # Banco.adicionar_banco(self, banco3)
            self.banco = tk.Toplevel()
            self.banco.title("Banco")
            self.banco.geometry('800x600')
            self.janela.grab_set()

            # Botões
            self.btn_cadastrar = tk.Button(self.banco, text="Cadastrar", command=cadastrar_banco)
            self.btn_cadastrar.grid(column=0, row=0)

            self.selecionado = tk.StringVar()
            self.cbx_mostrar_banco = ttk.Combobox(self.banco, textvariable=self.selecionado)
            self.cbx_mostrar_banco['values'] = Banco.bancos
            self.cbx_mostrar_banco['state'] = 'readonly'
            self.cbx_mostrar_banco.current(0)
            self.cbx_mostrar_banco.grid(column=3, row=0)

            #self.btn_selecionar = tk.Button(self.banco, text="Selecionar", command=banco_selecionado)
            self.btn_selecionar = tk.Button(self.banco, text="Selecionar")
            self.btn_selecionar.grid(column=3, row=1)

            colunas = ["número", "nome"]
            self.tvw_banco_selecionado = ttk.Treeview(self.banco, columns=colunas, show="headings")
            self.tvw_banco_selecionado.grid(column=0, row=2)

            # Cabeçalho
            self.tvw_banco_selecionado.heading(colunas[0], text='Número')
            self.tvw_banco_selecionado.heading(colunas[1], text='Nome')
            # self.tvw_banco_selecionado.heading(colunas[2], text='Contas')

            # Tamanho
            self.tvw_banco_selecionado.column(colunas[0], minwidth=0, width=111)
            self.tvw_banco_selecionado.column(colunas[1], minwidth=0, width=170)
            # self.tvw_banco_selecionado.column(colunas[2], minwidth=0, width=111)

            #Conteudo
            for banco in Banco.bancos:
                self.tvw_banco_selecionado.insert("", tk.END, values=(banco.num, banco.nome))

            #self.tvw_banco_selecionado.insert("", tk.END, values=("Danone Player", 654789))
            #self.tvw_banco_selecionado.insert("", tk.END, values=("Luiz Eduardo", 654321))


        def cadastrar_banco():
            self.cadastro_banco = tk.Toplevel()
            self.cadastro_banco.title("Cadastrar Banco")
            self.cadastro_banco.geometry("250x100")
            self.banco.iconify()

            self.btn_num_bc = tk.Label(self.cadastro_banco, text="Número")
            self.btn_num_bc.grid(column=0, row=0)
            self.ent_num_bc = tk.Entry(self.cadastro_banco)
            self.ent_num_bc.grid(column=1, row=0)

            self.btn_nome_bc = tk.Label(self.cadastro_banco, text="Nome")
            self.btn_nome_bc.grid(column=0, row=1)
            self.ent_nome_bc = tk.Entry(self.cadastro_banco)
            self.ent_nome_bc.grid(column=1, row=1)

            self.btn_salvar_bc = tk.Button(self.cadastro_banco, text="Salvar", command=confirmar_cadastro_banco)
            self.btn_salvar_bc.grid(column=1, row=3, columnspan=2)

        def confirmar_cadastro_banco():
            nome = self.ent_nome_bc.get()
            nome = Banco(self.ent_num_bc.get(), self.ent_nome_bc.get())
            Banco.adicionar_banco(self, nome)
            for i in Banco.bancos:
                print(i.nome)
            self.cbx_mostrar_banco['values'] = Banco.bancos
            self.cbx_mostrar_banco.current(0)
            self.tvw_banco_selecionado.insert("", tk.END, values=(self.ent_num_bc.get(), self.ent_nome_bc.get()))
            self.cadastro_banco.destroy()
            self.banco.deiconify()


        # def banco_selecionado():
        #     valor = self.selecionado.get()
        #     for i in Banco.bancos:
        #         if valor == i.nome:
        #             banco_selecionado = i
        #     todos = self.tvw_banco_selecionado.get_children()
        #     for i in todos:
        #         self.tvw_banco_selecionado.delete(i)
        #     self.tvw_banco_selecionado.insert("", tk.END, values=(banco_selecionado.nome, banco_selecionado.num))

        # def editar_banco():
        #     self.top_editar_banco = tk.Toplevel()
        #     self.top_editar_banco.title("Editar banco")
        #     self.lbl_num = tk.Label(self.top_editar_banco, text='Número:')
        #     self.lbl_num.grid(column=0, row=0)
        #
        #     self.lbl_nome = tk.Label(self.top_editar_banco, text='Nome:')
        #     self.lbl_nome.grid(column=0, row=1)
        #
        #     selecionado = self.tvw_banco_selecionado.selection()
        #     lista = self.tvw_banco_selecionado.item(selecionado, "values")
        #
        #     self.entry_num = tk.Entry(self.top_editar_banco, width=30)
        #     self.entry_num.grid(column=1, row=0)
        #     self.entry_num.insert(0, lista[0])
        #
        #     self.entry_nome = tk.Entry(self.top_editar_banco, width=30)
        #     self.entry_nome.grid(column=1, row=1)
        #     self.entry_nome.insert(0, lista[1])
        #
        #     self.btn_confirmar = tk.Button(self.top_editar_banco, text='Confirmar', command=confirmar_edicao)
        #     self.btn_confirmar.grid(column=1, row=3, columnspan=1)
        #
        # def confirmar_edicao():
        #     num = self.entry_num.get()
        #     nome = self.entry_nome.get()
        #     selecionado = self.tvw_banco_selecionado.selection()
        #     # print(selecionado)
        #     # lista = self.tvw_banco_selecionado.item(selecionado, "values")
        #     # if num == lista[0] and nome == lista[1]:
        #     #     mensagem = messagebox.askyesno('Nenhuma modificação feita!', 'Você tem certeza que não deseja fazer nenhuma modificação?', parent=self.top_atualizar)
        #     #     if mensagem == False:
        #     #         self.banco.deiconify()
        #     #     else:
        #     #         self.top_editar_banco.destroy()
        #     # else:
        #     #     mensagem = messagebox.askyesno('Modificação feita!', 'Você tem certeza que deseja confirmar as alterações?', parent=self.top_atualizar)
        #     #     if mensagem == False:
        #     #         self.banco.deiconify()
        #     #     else:
        #     self.tvw_banco_selecionado.item(selecionado, values=(num, nome))
        #     self.top_editar_banco.destroy()

        self.janela = master
        self.janela.title("Menu")
        self.janela.geometry("500x312")

        # botões
        self.btn_cliente = tk.Button(self.janela, text="Cliente", font=("Verdana", 12), height=5, bg='#9cd7ff')
        self.btn_cliente.bind('<Button-1>', cliente)
        self.btn_cliente.pack(fill=tk.BOTH)

        self.btn_conta = tk.Button(self.janela, text="Conta", font=("Verdana", 12), height=5, bg='#6695fa', command=conta)
        self.btn_conta.pack(fill=tk.BOTH)

        self.btn_banco = tk.Button(self.janela, text="Banco", font=("Verdana", 12), height=5, bg='#375898', command=banco)
        self.btn_banco.pack(fill=tk.BOTH)

        # cliente = Cliente("Elias Cacau", "024.631.012-02", "Rua Ametista")
        # Cliente.adicionar_clientes(self, cliente)

        #banco1 = Banco("Elias Cacau", 123456)
        # banco2 = Banco("Danone Player", 654789)
        # banco3 = Banco("Luiz Eduardo", 654321)
        #Banco.adicionar_banco(self, banco1)
        # Banco.adicionar_banco(self, banco2)
        # Banco.adicionar_banco(self, banco3)



sys.setrecursionlimit(1500)
app = tk.Tk()
Tela(app)
app.mainloop()