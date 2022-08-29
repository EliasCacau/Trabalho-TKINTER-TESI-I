import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from trabalho.banco import Banco
from trabalho.cliente import Cliente
from trabalho.contaCorrente import ContaCorrente
from trabalho.contaPoupanca import ContaPoupanca
#import sys

class Tela(ContaCorrente, ContaPoupanca, Cliente, Banco):
    def __init__(self, master):
        def cliente(event):
            self.cliente = tk.Toplevel()
            self.cliente.title("Cliente")
            self.cliente.geometry("575x300")

            self.frm_cli_botoes = tk.Frame(self.cliente)
            self.frm_cli_botoes.pack(side=tk.BOTTOM)

            # Treeview
            colunas = ['id', 'nome', 'cpf', 'endereco', 'banco']
            self.tvw_cliente = ttk.Treeview(self.cliente, columns=colunas, show="headings")
            self.tvw_cliente.pack(side=tk.LEFT, fill=tk.BOTH)

            # Cabeçalho
            self.tvw_cliente.heading(colunas[0], text='Id')
            self.tvw_cliente.heading(colunas[1], text='Nome')
            self.tvw_cliente.heading(colunas[2], text='CPF')
            self.tvw_cliente.heading(colunas[3], text='Endereço')
            self.tvw_cliente.heading(colunas[4], text='Banco')

            # Tamanho
            self.tvw_cliente.column(colunas[0], minwidth=0, width=25)
            self.tvw_cliente.column(colunas[1], minwidth=0, width=160)
            self.tvw_cliente.column(colunas[2], minwidth=0, width=111)
            self.tvw_cliente.column(colunas[3], minwidth=0, width=160)
            self.tvw_cliente.column(colunas[4], minwidth=0, width=100)

            #Conteúdo
            for cliente in Cliente.clientes:
                self.tvw_cliente.insert("", tk.END, values=(cliente.id, cliente.nome, cliente.cpf, cliente.endereco, cliente.banco))

            #Scrollbar
            self.scr_cliente = ttk.Scrollbar(self.cliente, command=self.tvw_cliente.yview)
            self.scr_cliente.pack(side=tk.LEFT, fill=tk.BOTH)
            self.tvw_cliente.configure(yscroll=self.scr_cliente.set)

            #Botões
            self.btn_cli_cadastrar = tk.Button(self.frm_cli_botoes, text="Cadastrar", command=cadastrar_cliente, bg="White", font="Verdana, 12")
            self.btn_cli_cadastrar.pack(side=tk.LEFT)

            self.btn_cli_editar = tk.Button(self.frm_cli_botoes, text="Editar", command=editar_cliente, bg="#ffdd00", font="Verdana, 12")
            self.btn_cli_editar.pack(side=tk.LEFT)

            self.btn_cli_excluir = tk.Button(self.frm_cli_botoes, text="Excluir", command=excluir_cliente, bg="#d04500", font="Verdana, 12")
            self.btn_cli_excluir.pack(side=tk.LEFT)

            self.btn_cli_desvincular = tk.Button(self.frm_cli_botoes, text="Desvincular", command=desvincular_banco, bg="#9cd7ff", font="Verdana, 12")
            self.btn_cli_desvincular.pack(side=tk.LEFT)

        def cadastrar_cliente():
            self.cadastrar_cliente = tk.Toplevel()
            self.cadastrar_cliente.title("Cadastrar Cliente")
            self.cadastrar_cliente.geometry("270x150")

            self.btn_nome_cli = tk.Label(self.cadastrar_cliente, text="Nome:")
            self.btn_nome_cli.grid(column=0, row=0)
            self.ent_nome_cli = tk.Entry(self.cadastrar_cliente)
            self.ent_nome_cli.grid(column=1, row=0)

            self.btn_cpf_cli = tk.Label(self.cadastrar_cliente, text="CPF:")
            self.btn_cpf_cli.grid(column=0, row=1)
            self.ent_cpf_cli = tk.Entry(self.cadastrar_cliente)
            self.ent_cpf_cli.grid(column=1, row=1)

            self.btn_end_cli = tk.Label(self.cadastrar_cliente, text="Endereço:")
            self.btn_end_cli.grid(column=0, row=2)
            self.ent_end_cli = tk.Entry(self.cadastrar_cliente)
            self.ent_end_cli.grid(column=1, row=2)

            self.lbl_cadastro_banco = tk.Label(self.cadastrar_cliente, text="Selecione o banco:")
            self.lbl_cadastro_banco.grid(column=0, row=3)
            self.selecionado = tk.StringVar()
            self.cbx_cc_banco = ttk.Combobox(self.cadastrar_cliente, textvariable=self.selecionado)
            self.cbx_cc_banco['values'] = Banco.bancos
            self.cbx_cc_banco['state'] = 'readonly'
            self.cbx_cc_banco.current(0)
            self.cbx_cc_banco.grid(column=1, row=3, pady=5)

            self.btn_salvar_cli = tk.Button(self.cadastrar_cliente, text="Salvar", command=confirmar_cadastrar_cliente)
            self.btn_salvar_cli.grid(column=1, row=4, columnspan=2)

        def confirmar_cadastrar_cliente():
            cliente = Cliente(self.ent_nome_cli.get(), self.ent_cpf_cli.get(), self.ent_end_cli.get())
            selecionado = self.selecionado.get()
            for banco in Banco.bancos:
                if selecionado == banco.nome:
                    selecionado = banco
                    cliente.banco = banco
            Cliente.adicionar_clientes(self, cliente)
            self.tvw_cliente.insert("", tk.END, values=(cliente.id, cliente.nome, cliente.cpf, cliente.endereco, cliente.banco))
            self.cadastrar_cliente.destroy()
            self.cliente.deiconify()

        def editar_cliente():
            self.editar_cliente = tk.Toplevel()
            self.editar_cliente.title("Editar cliente")
            self.editar_cliente.geometry("300x150")
            self.lbl_nome = tk.Label(self.editar_cliente, text='Nome:')
            self.lbl_nome.grid(column=0, row=0)

            self.lbl_cpf = tk.Label(self.editar_cliente, text='CPF:')
            self.lbl_cpf.grid(column=0, row=1)

            self.lbl_end = tk.Label(self.editar_cliente, text='Endereço:')
            self.lbl_end.grid(column=0, row=2)

            selecionado = self.tvw_cliente.selection()
            lista = self.tvw_cliente.item(selecionado, "values")

            self.entry_nome_cli = tk.Entry(self.editar_cliente, width=30)
            self.entry_nome_cli.grid(column=1, row=0)
            self.entry_nome_cli.insert(0, lista[1])

            self.entry_cpf_cli = tk.Entry(self.editar_cliente, width=30)
            self.entry_cpf_cli.grid(column=1, row=1)
            self.entry_cpf_cli.insert(0, lista[2])

            self.entry_end_cli = tk.Entry(self.editar_cliente, width=30)
            self.entry_end_cli.grid(column=1, row=2)
            self.entry_end_cli.insert(0, lista[3])

            self.btn_confirmar_cli = tk.Button(self.editar_cliente, text='Confirmar', command=confirmar_edicao_cliente)
            self.btn_confirmar_cli.grid(column=1, row=4, columnspan=1)

        def confirmar_edicao_cliente():
            nome = self.entry_nome_cli.get()
            cpf = self.entry_cpf_cli.get()
            end = self.entry_end_cli.get()
            selecionado = self.tvw_cliente.selection()
            lista = self.tvw_cliente.item(selecionado, "values")

            if nome == lista[1] and cpf == lista[2] and end == lista[3]:
                mensagem = messagebox.askyesno('Nenhuma modificação feita!', 'Você tem certeza que não deseja fazer nenhuma modificação?', parent=self.editar_cliente)
                if mensagem:
                    self.editar_cliente.destroy()
            else:
                mensagem = messagebox.askyesno('Modificação feita!', 'Você tem certeza que deseja confirmar as alterações?', parent=self.editar_cliente)
                if mensagem == False:
                    self.editar_cliente.deiconify()
                else:
                    for cliente in Cliente.clientes:
                        if cliente == lista:
                            cliente.nome = nome
                            cliente.cpf = cpf
                            cliente.endereco = end
                    self.tvw_cliente.item(selecionado, values=(lista[0], nome, cpf, end, lista[4]))
                    self.cliente.deiconify()
                    self.editar_cliente.destroy()

        def excluir_cliente():
            selecionado = self.tvw_cliente.selection()
            lista = self.tvw_cliente.item(selecionado, "values")
            if selecionado != ():
                if lista[4] == '':
                    # Solução para a janela principal não sobreescrever a tela cliente
                    self.janela.iconify()
                    messagem = messagebox.askyesno("Cuidado!", "Tem certeza que deseja apagar o item selecionado?")
                    if messagem == False:
                        self.janela.deiconify()
                        self.cliente.deiconify()
                    else:
                        for l in lista:
                            for cli in Cliente.clientes:
                                if l == cli.nome:
                                    Cliente.clientes.remove(cli)
                        for s in selecionado:
                            self.tvw_cliente.delete(s)
                        self.janela.deiconify()
                        self.cliente.deiconify()
                else:
                    messagebox.showinfo("Não é possivel remover", "Só é permitido a remoção de cliente não vinculado a um banco")

        def desvincular_banco():
            selecionado = self.tvw_cliente.selection()
            lista = self.tvw_cliente.item(selecionado, "values")
            cliente = 0
            if selecionado != ():
                for l in lista:
                    for cli in Cliente.clientes:
                        if l == cli.nome:
                            cli.banco = ''
                            cliente = cli
                self.tvw_cliente.item(selecionado, values=(cliente.id, cliente.nome, cliente.cpf, cliente.endereco, cliente.banco))

        def conta():
            self.conta = tk.Toplevel()
            self.conta.title("Contas")
            self.conta.geometry("500x312")
            self.btn_conta_corrente = tk.Button(self.conta, font=("Verdana", 12), text="Conta Corrente", bg="#9cd7ff",
                                                command=conta_corrente)
            self.btn_conta_corrente.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.btn_conta_poupanca = tk.Button(self.conta, font=("Verdana", 12), text="Conta Popuança", bg="#6695fa", command=conta_poupanca)
            self.btn_conta_poupanca.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        def conta_corrente():
            self.conta_corrente = tk.Toplevel()
            self.conta_corrente.title("Conta Corrente")
            self.conta_corrente.geometry("625x300")
            self.conta.destroy()

            self.frm_cc = tk.Frame(self.conta_corrente)
            self.frm_cc.pack(side=tk.BOTTOM)

            colunas = ["id", "cliente", "número", "saldo", "status", "banco"]
            self.tvw_conta_corrente = ttk.Treeview(self.conta_corrente, columns=colunas, show="headings")
            self.tvw_conta_corrente.pack(side=tk.LEFT, fill=tk.BOTH)

            # Cabeçalho
            self.tvw_conta_corrente.heading(colunas[0], text='Id')
            self.tvw_conta_corrente.heading(colunas[1], text='Cliente')
            self.tvw_conta_corrente.heading(colunas[2], text='Número')
            self.tvw_conta_corrente.heading(colunas[3], text='Saldo')
            self.tvw_conta_corrente.heading(colunas[4], text='Status')
            self.tvw_conta_corrente.heading(colunas[5], text='Banco')

            # Tamanho
            self.tvw_conta_corrente.column(colunas[0], minwidth=0, width=25)
            self.tvw_conta_corrente.column(colunas[1], minwidth=0, width=160)
            self.tvw_conta_corrente.column(colunas[2], minwidth=0, width=105)
            self.tvw_conta_corrente.column(colunas[3], minwidth=0, width=105)
            self.tvw_conta_corrente.column(colunas[4], minwidth=0, width=105)
            self.tvw_conta_corrente.column(colunas[5], minwidth=0, width=105)

            # Conteudo
            for cc in ContaCorrente.contas_cc:
                self.tvw_conta_corrente.insert("", tk.END,
                                               values=(cc.id, cc.titular, cc.numero, cc.saldo, cc.status, cc.banco))

            # Scrollbar
            self.scr_conta_corrente = ttk.Scrollbar(self.conta_corrente, command=self.tvw_conta_corrente.yview)
            self.scr_conta_corrente.pack(side=tk.LEFT, fill=tk.BOTH)
            self.tvw_conta_corrente.configure(yscroll=self.scr_conta_corrente.set)

            self.btn_cc_cadastrar = tk.Button(self.frm_cc, font=("Verdana", 12), text="Cadastrar", bg="white",
                                                command=cadastrar_cc)
            self.btn_cc_cadastrar.pack(side=tk.LEFT, fill=tk.BOTH)
            self.btn_cc_depositar = tk.Button(self.frm_cc, font=("Verdana", 12), text="Depositar", bg="green",
                                              command=depositar_cc)
            self.btn_cc_depositar.pack(side=tk.LEFT, fill=tk.BOTH)
            self.btn_cc_sacar = tk.Button(self.frm_cc, font=("Verdana", 12), text="Sacar", bg="green",
                                              command=sacar_cc)
            self.btn_cc_sacar.pack(side=tk.LEFT, fill=tk.BOTH)
            self.btn_cc_extrato = tk.Button(self.frm_cc, font=("Verdana", 12), text="Extrato", bg="yellow",
                                              command=extrato)
            self.btn_cc_extrato.pack(side=tk.LEFT, fill=tk.BOTH)

            self.btn_cc_encerrar = tk.Button(self.frm_cc, text="Encerrar", font=("Verdana", 12), bg="orange", command=encerrar_conta_corrente)
            self.btn_cc_encerrar.pack(side=tk.LEFT)

        def cadastrar_cc():
            self.cadastrar_cc = tk.Toplevel()
            self.cadastrar_cc.geometry("280x130")
            self.lbl_cadastro_nome = tk.Label(self.cadastrar_cc, text="Selecione o cliente:")
            self.lbl_cadastro_nome.grid(column=0, row=0, pady=5)
            self.selecionado_cliente = tk.StringVar()
            self.cbx_cc_cliente = ttk.Combobox(self.cadastrar_cc, textvariable=self.selecionado_cliente)
            self.cbx_cc_cliente['values'] = Cliente.clientes
            self.cbx_cc_cliente['state'] = 'readonly'
            self.cbx_cc_cliente.current(0)
            self.cbx_cc_cliente.grid(column=1, row=0)

            self.lbl_cadastro_num = tk.Label(self.cadastrar_cc, text="Número:")
            self.lbl_cadastro_num.grid(column=0, row=2)
            self.ent_cadastro_num = tk.Entry(self.cadastrar_cc)
            self.ent_cadastro_num.grid(column=1, row=2, pady=5)

            self.btn_confirmar_cc = tk.Button(self.cadastrar_cc, text="Confirmar", command=confirmar_cadastro_cc)
            self.btn_confirmar_cc.grid(column=1, row=3, columnspan=1)

        def confirmar_cadastro_cc():
            nome = ContaCorrente(self.ent_cadastro_num.get(), self.selecionado_cliente.get())
            selecionado = self.selecionado_cliente.get()
            for cliente in Cliente.clientes:
                if selecionado == cliente.nome:
                    selecionado = cliente
                    nome.banco = cliente.banco
            ContaCorrente.add_conta(self, nome)
            self.tvw_conta_corrente.insert("", tk.END, values=(nome.id, nome.titular, nome.numero, nome.saldo, nome.status, nome.banco))
            self.cadastrar_cc.destroy()
            self.conta_corrente.deiconify()

        def depositar_cc():
            selecionado = self.tvw_conta_corrente.selection()
            lista = self.tvw_conta_corrente.item(selecionado, "values")
            if selecionado != ():
                for conta in ContaCorrente.contas_cc:
                    if int(lista[0]) == conta.id:
                        if conta.status == "Ativo":
                            self.depositar_cc = tk.Toplevel()
                            self.depositar_cc.title("Depositar")
                            self.depositar_cc.geometry("150x100")
                            self.lbl_depositar = tk.Label(self.depositar_cc, text="Valor")
                            self.lbl_depositar.pack()
                            self.ent_depositar = tk.Entry(self.depositar_cc)
                            self.ent_depositar.pack()
                            self.btn_confirmar_deposito = tk.Button(self.depositar_cc, text="Confirmar", command=confirmar_deposito_cc)
                            self.btn_confirmar_deposito.pack(pady=5)
                        else:
                            messagebox.showinfo("Conta encerrada", "Esta conta foi encerrada")
                            self.conta_corrente.deiconify()

        def confirmar_deposito_cc():
            selecionado = self.tvw_conta_corrente.selection()
            lista = self.tvw_conta_corrente.item(selecionado, "values")
            for conta in ContaCorrente.contas_cc:
                if int(lista[0]) == conta.id:
                    conta.deposito(float(self.ent_depositar.get()))
                    self.tvw_conta_corrente.item(selecionado, values=(conta.id, conta.titular, conta.numero, conta.saldo, conta.status, conta.banco))
            self.depositar_cc.destroy()

        def sacar_cc():
            selecionado = self.tvw_conta_corrente.selection()
            lista = self.tvw_conta_corrente.item(selecionado, "values")
            if selecionado != ():
                for conta in ContaCorrente.contas_cc:
                    if int(lista[0]) == conta.id:
                        if conta.status == "Ativo":
                            if selecionado != ():
                                self.sacar_cc = tk.Toplevel()
                                self.sacar_cc.title("Sacar")
                                self.sacar_cc.geometry("150x100")
                                self.lbl_sacar = tk.Label(self.sacar_cc, text="Valor")
                                self.lbl_sacar.pack()
                                self.ent_sacar = tk.Entry(self.sacar_cc)
                                self.ent_sacar.pack()
                                self.btn_confirmar_saque = tk.Button(self.sacar_cc, text="Confirmar", command=confirmar_saque_cc)
                                self.btn_confirmar_saque.pack(pady=5)
                        else:
                            messagebox.showinfo("Conta encerrada", "Esta conta foi encerrada")
                            self.conta_corrente.deiconify()

        def confirmar_saque_cc():
            selecionado = self.tvw_conta_corrente.selection()
            lista = self.tvw_conta_corrente.item(selecionado, "values")
            for conta in ContaCorrente.contas_cc:
                if int(lista[0]) == conta.id:
                    if conta.saldo-1 >= float(self.ent_sacar.get()):
                        conta.saque(float(self.ent_sacar.get()))
                        self.tvw_conta_corrente.item(selecionado, values=(conta.id, conta.titular, conta.numero, conta.saldo, conta.status, conta.banco))
                    else:
                        messagebox.showinfo('Saldo insuficiente!', "Saldo insuficiente!")
                        self.conta_corrente.deiconify()
            self.sacar_cc.destroy()

        def encerrar_conta_corrente():
            selecionado = self.tvw_conta_corrente.selection()
            lista = self.tvw_conta_corrente.item(selecionado, "values")
            if float(lista[3]) == 0 and lista[4] == 'Ativo':
                mensagem = messagebox.askyesno("Encerrar conta", "Você tem certeza que deseja encerrar a conta?")
                if mensagem:
                    for conta in ContaCorrente.contas_cc:
                        if int(lista[0]) == conta.id:
                            conta.status = "Encerrado"
                            self.tvw_conta_corrente.item(selecionado, values=(conta.id, conta.titular, conta.numero, conta.saldo, conta.status, conta.banco))
                            self.conta_corrente.deiconify()
                else:
                    self.conta_corrente.deiconify()
            else:
                messagebox.showinfo("Conta não encerrada", "A conta já foi encerrada ou não está zerada")
                self.conta_corrente.deiconify()

        def extrato():
            selecao = self.tvw_conta_corrente.selection()
            item = self.tvw_conta_corrente.item(selecao, "values")
            if len(selecao) != 1:
                messagebox.showerror("Error", "Selecione 1 conta somente!")
            else:
                toplevel = tk.Toplevel(self.conta_corrente)
                toplevel.minsize(700, 500)
                toplevel.title("Cadastro de Conta Corrente")
                toplevel.grab_set()

                # self.sct = ScrolledText(toplevel)

                colunas = ['Operação', 'Valores', 'Data']
                self.tvw = ttk.Treeview(toplevel, columns=colunas, show="headings")
                self.tvw.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                self.tvw.heading(colunas[0], text="Operação")
                self.tvw.heading(colunas[1], text="Valores")
                self.tvw.heading(colunas[2], text="Data")

                self.tvw.column(column=[0], minwidth=0, width=300)
                self.tvw.column(column=[1], minwidth=0, width=300)
                self.tvw.column(column=[2], minwidth=0, width=150)

                scrollbar = tk.Scrollbar(toplevel, command=self.tvw.yview)
                scrollbar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                self.tvw.configure(yscroll=scrollbar.set)

                for conta in ContaCorrente.contas_cc:
                    if conta.id == int(item[0]):
                        for mov in conta.extrato:
                            frag = [x for x in mov.split("|")]
                            self.tvw.insert('', tk.END, values=(frag[1], frag[2], frag[3]))
                        break

                def gerar_arquivo():
                    for conta in ContaCorrente.contas_cc:
                        if conta.id == int(item[0]):
                            conta.imprimir_extrato()
                            messagebox.showinfo("Extrato gerado!", f"O arquivo com o extrato da conta:'{conta.titular}' foi gerado!")

                self.frmBtns = tk.Frame(toplevel)
                self.frmBtns.pack(side=tk.BOTTOM)
                self.btnS1 = tk.Button(self.frmBtns, text="Gerar arquivo", command=gerar_arquivo)
                self.btnS1.pack(ipady=10)

        def conta_poupanca():
            self.conta_poupanca = tk.Toplevel()
            self.conta_poupanca.title("Conta Poupanca")
            self.conta_poupanca.geometry("625x300")
            self.conta.destroy()

            self.frm_cp = tk.Frame(self.conta_poupanca)
            self.frm_cp.pack(side=tk.BOTTOM)

            colunas = ["id", "cliente", "número", "saldo", "status", "banco"]
            self.tvw_conta_poupanca = ttk.Treeview(self.conta_poupanca, columns=colunas, show="headings")
            self.tvw_conta_poupanca.pack(side=tk.LEFT, fill=tk.BOTH)

            # Cabeçalho
            self.tvw_conta_poupanca.heading(colunas[0], text='Id')
            self.tvw_conta_poupanca.heading(colunas[1], text='Cliente')
            self.tvw_conta_poupanca.heading(colunas[2], text='Número')
            self.tvw_conta_poupanca.heading(colunas[3], text='Saldo')
            self.tvw_conta_poupanca.heading(colunas[4], text='Status')
            self.tvw_conta_poupanca.heading(colunas[5], text='Banco')

            # Tamanho
            self.tvw_conta_poupanca.column(colunas[0], minwidth=0, width=25)
            self.tvw_conta_poupanca.column(colunas[1], minwidth=0, width=160)
            self.tvw_conta_poupanca.column(colunas[2], minwidth=0, width=105)
            self.tvw_conta_poupanca.column(colunas[3], minwidth=0, width=105)
            self.tvw_conta_poupanca.column(colunas[4], minwidth=0, width=105)
            self.tvw_conta_poupanca.column(colunas[5], minwidth=0, width=105)

            # Conteudo
            for cp in ContaPoupanca.contas_cp:
                self.tvw_conta_poupanca.insert("", tk.END, values=(cp.id, cp.titular, cp.numero, cp.saldo, cp.status, cp.banco))

            # Scrollbar
            self.scr_conta_corrente = ttk.Scrollbar(self.conta_poupanca, command=self.tvw_conta_poupanca.yview)
            self.scr_conta_corrente.pack(side=tk.LEFT, fill=tk.BOTH)
            self.tvw_conta_poupanca.configure(yscroll=self.scr_conta_corrente.set)

            self.btn_cc_cadastrar = tk.Button(self.frm_cp, font=("Verdana", 12), text="Cadastrar", bg="white",
                                              command=cadastrar_cp)
            self.btn_cc_cadastrar.pack(side=tk.LEFT, fill=tk.BOTH)
            self.btn_cc_depositar = tk.Button(self.frm_cp, font=("Verdana", 12), text="Depositar", bg="green",
                                              command=depositar_cp)
            self.btn_cc_depositar.pack(side=tk.LEFT, fill=tk.BOTH)
            self.btn_cc_sacar = tk.Button(self.frm_cp, font=("Verdana", 12), text="Sacar", bg="green",
                                          command=sacar_cp)
            self.btn_cc_sacar.pack(side=tk.LEFT, fill=tk.BOTH)
            self.btn_cc_extrato = tk.Button(self.frm_cp, font=("Verdana", 12), text="Extrato", bg="yellow",
                                            command=cadastrar_cp)
            self.btn_cc_extrato.pack(side=tk.LEFT, fill=tk.BOTH)

            self.btn_cc_encerrar = tk.Button(self.frm_cp, text="Encerrar", font=("Verdana", 12), bg="orange",
                                            command=encerrar_conta_poupanca)
            self.btn_cc_encerrar.pack(side=tk.LEFT)

            self.btn_passar_mes = tk.Button(self.frm_cp, text="Passar mês", font=("Verdana", 12), bg="orange", command=passar_mes)
            self.btn_passar_mes.pack(side=tk.LEFT)

        def cadastrar_cp():
            self.cadastrar_cp = tk.Toplevel()
            self.cadastrar_cp.geometry("280x130")
            self.lbl_cadastro_nome = tk.Label(self.cadastrar_cp, text="Selecione o cliente:")
            # self.lbl_cadastro_nome = tk.Label(self.cadastrar_cp, text="Selecione o cliente", font="Verdana, 12", bg="#6695fa")
            self.lbl_cadastro_nome.grid(column=0, row=0, pady=5)
            self.selecionado_cliente = tk.StringVar()
            self.cbx_cc_cliente = ttk.Combobox(self.cadastrar_cp, textvariable=self.selecionado_cliente)
            self.cbx_cc_cliente['values'] = Cliente.clientes
            self.cbx_cc_cliente['state'] = 'readonly'
            self.cbx_cc_cliente.current(0)
            self.cbx_cc_cliente.grid(column=1, row=0)

            self.lbl_cadastro_num = tk.Label(self.cadastrar_cp, text="Número:")
            self.lbl_cadastro_num.grid(column=0, row=2)
            self.ent_cadastro_num = tk.Entry(self.cadastrar_cp)
            self.ent_cadastro_num.grid(column=1, row=2, pady=5)

            self.btn_confirmar_cp = tk.Button(self.cadastrar_cp, text="Confirmar", command=confirmar_cadastro_cp)
            self.btn_confirmar_cp.grid(column=1, row=3, columnspan=1)

        def confirmar_cadastro_cp():
            nome = ContaPoupanca(self.ent_cadastro_num.get(), self.selecionado_cliente.get())
            selecionado = self.selecionado_cliente.get()
            for cliente in Cliente.clientes:
                if selecionado == cliente.nome:
                    selecionado = cliente
                    nome.banco = cliente.banco
            ContaPoupanca.add_conta(self, nome)
            self.tvw_conta_poupanca.insert("", tk.END, values=(nome.id, nome.titular, nome.numero, nome.saldo, nome.status, nome.banco))
            self.cadastrar_cp.destroy()
            self.conta_poupanca.deiconify()

        def depositar_cp():
            selecionado = self.tvw_conta_poupanca.selection()
            lista = self.tvw_conta_poupanca.item(selecionado, "values")
            if selecionado != ():
                for conta in ContaPoupanca.contas_cp:
                    if int(lista[0]) == conta.id:
                        if conta.status == "Ativo":
                            self.depositar_cp = tk.Toplevel()
                            self.depositar_cp.title("Depositar")
                            self.depositar_cp.geometry("150x100")
                            self.lbl_depositar = tk.Label(self.depositar_cp, text="Valor")
                            self.lbl_depositar.pack()
                            self.ent_depositar = tk.Entry(self.depositar_cp)
                            self.ent_depositar.pack()
                            self.btn_confirmar_deposito = tk.Button(self.depositar_cp, text="Confirmar",
                                                                    command=confirmar_deposito_cp)
                            self.btn_confirmar_deposito.pack(pady=5)
                        else:
                            messagebox.showinfo("Conta encerrada", "Esta conta foi encerrada")
                            self.conta_poupanca.deiconify()

        def confirmar_deposito_cp():
            selecionado = self.tvw_conta_poupanca.selection()
            lista = self.tvw_conta_poupanca.item(selecionado, "values")
            for conta in ContaPoupanca.contas_cp:
                if int(lista[0]) == conta.id:
                    conta.deposito(float(self.ent_depositar.get()))
                    self.tvw_conta_poupanca.item(selecionado, values=(conta.id, conta.titular, conta.numero, conta.saldo, conta.status, conta.banco))
            self.depositar_cp.destroy()

        def sacar_cp():
            selecionado = self.tvw_conta_poupanca.selection()
            lista = self.tvw_conta_poupanca.item(selecionado, "values")
            if selecionado != ():
                for conta in ContaPoupanca.contas_cp:
                    if int(lista[0]) == conta.id:
                        if conta.status == "Ativo":
                            if selecionado != ():
                                self.sacar_cp = tk.Toplevel()
                                self.sacar_cp.title("Sacar")
                                self.sacar_cp.geometry("150x100")
                                self.lbl_sacar = tk.Label(self.sacar_cp, text="Valor")
                                self.lbl_sacar.pack()
                                self.ent_sacar = tk.Entry(self.sacar_cp)
                                self.ent_sacar.pack()
                                self.btn_confirmar_saque = tk.Button(self.sacar_cp, text="Confirmar",
                                                                     command=confirmar_saque_cp)
                                self.btn_confirmar_saque.pack(pady=5)
                        else:
                            messagebox.showinfo("Conta encerrada", "Esta conta foi encerrada")
                            self.conta_poupanca.deiconify()

        def confirmar_saque_cp():
            selecionado = self.tvw_conta_poupanca.selection()
            lista = self.tvw_conta_poupanca.item(selecionado, "values")
            for conta in ContaPoupanca.contas_cp:
                if int(lista[0]) == conta.id:
                    if conta.saldo >= float(self.ent_sacar.get()):
                        conta.saque(float(self.ent_sacar.get()))
                        self.tvw_conta_poupanca.item(selecionado, values=(
                        conta.id, conta.titular, conta.numero, conta.saldo, conta.status, conta.banco))
                    else:
                        messagebox.showinfo('Saldo insuficiente!', "Saldo insuficiente!")
                        self.conta_poupanca.deiconify()
            self.sacar_cp.destroy()

        def encerrar_conta_poupanca():
            selecionado = self.tvw_conta_poupanca.selection()
            lista = self.tvw_conta_poupanca.item(selecionado, "values")
            if float(lista[3]) == 0 and lista[4] == 'Ativo':
                mensagem = messagebox.askyesno("Encerrar conta", "Você tem certeza que deseja encerrar a conta?")
                if mensagem:
                    for conta in ContaPoupanca.contas_cp:
                        if int(lista[0]) == conta.id:
                            conta.status = "Encerrado"
                            self.tvw_conta_poupanca.item(selecionado, values=(conta.id, conta.titular, conta.numero, conta.saldo, conta.status, conta.banco))
                            self.conta_poupanca.deiconify()
                else:
                    self.conta_poupanca.deiconify()
            else:
                messagebox.showinfo("Conta não encerrada", "A conta já foi encerrada ou não está zerada")
                self.conta_poupanca.deiconify()

        def passar_mes():
            selecionado = self.tvw_conta_poupanca.selection()
            lista = self.tvw_conta_poupanca.item(selecionado, "values")
            if selecionado != ():
                for conta in ContaPoupanca.contas_cp:
                    if int(lista[0]) == conta.id:
                        if conta.saldo >= conta.taxa:
                            conta.saque(conta.taxa)
                            self.tvw_conta_poupanca.item(selecionado, values=(
                                conta.id, conta.titular, conta.numero, conta.saldo, conta.status, conta.banco))

        def banco():
            self.banco = tk.Toplevel()
            self.banco.title("Banco")
            self.banco.geometry('290x260')
            self.janela.grab_set()
            self.frm_btn_banco = tk.Frame(self.banco)
            self.frm_btn_banco.pack(side=tk.BOTTOM)

            # Botões
            self.btn_cadastrar_banco = tk.Button(self.frm_btn_banco, text="Cadastrar", command=cadastrar_banco, bg="White", font="Verdana, 12")
            self.btn_cadastrar_banco.pack(side=tk.LEFT)

            self.btn_editar_banco = tk.Button(self.frm_btn_banco, text="Editar", command=editar_banco, bg="#ffdd00", font="Verdana, 12")
            self.btn_editar_banco.pack(side=tk.LEFT)

            self.btn_excluir_banco = tk.Button(self.frm_btn_banco, text="Excluir", command=excluir_banco, bg="#d04500", font="Verdana, 12")
            self.btn_excluir_banco.pack(side=tk.LEFT)

            colunas = ["número", "nome"]
            self.tvw_banco_selecionado = ttk.Treeview(self.banco, columns=colunas, show="headings")
            self.tvw_banco_selecionado.pack(side=tk.LEFT, fill=tk.BOTH)

            # Cabeçalho
            self.tvw_banco_selecionado.heading(colunas[0], text='Número')
            self.tvw_banco_selecionado.heading(colunas[1], text='Nome')

            # Tamanho
            self.tvw_banco_selecionado.column(colunas[0], minwidth=0, width=111)
            self.tvw_banco_selecionado.column(colunas[1], minwidth=0, width=170)

            #Conteudo
            for banco in Banco.bancos:
                self.tvw_banco_selecionado.insert("", tk.END, values=(banco.num, banco.nome))

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
            nome = Banco(self.ent_num_bc.get(), self.ent_nome_bc.get())
            Banco.adicionar_banco(self, nome)
            self.tvw_banco_selecionado.insert("", tk.END, values=(self.ent_num_bc.get(), self.ent_nome_bc.get()))
            self.cadastro_banco.destroy()
            self.banco.deiconify()

        def editar_banco():
            self.editar_banco = tk.Toplevel()
            self.editar_banco.title("Editar banco")
            self.lbl_num = tk.Label(self.editar_banco, text='Número:')
            self.lbl_num.grid(column=0, row=0)

            self.lbl_nome = tk.Label(self.editar_banco, text='Nome:')
            self.lbl_nome.grid(column=0, row=1)

            selecionado = self.tvw_banco_selecionado.selection()
            lista = self.tvw_banco_selecionado.item(selecionado, "values")

            self.entry_num = tk.Entry(self.editar_banco, width=30)
            self.entry_num.grid(column=1, row=0)
            self.entry_num.insert(0, lista[0])

            self.entry_nome = tk.Entry(self.editar_banco, width=30)
            self.entry_nome.grid(column=1, row=1)
            self.entry_nome.insert(0, lista[1])

            self.btn_confirmar = tk.Button(self.editar_banco, text='Confirmar', command=confirmar_edicao)
            self.btn_confirmar.grid(column=1, row=3, columnspan=1)

        def confirmar_edicao():
            num = self.entry_num.get()
            nome = self.entry_nome.get()
            selecionado = self.tvw_banco_selecionado.selection()
            lista = self.tvw_banco_selecionado.item(selecionado, "values")
            if num == lista[0] and nome == lista[1]:
                mensagem = messagebox.askyesno('Nenhuma modificação feita!', 'Você tem certeza que não deseja fazer nenhuma modificação?', parent=self.editar_banco)
                if mensagem:
                    self.editar_banco.destroy()
            else:
                mensagem = messagebox.askyesno('Modificação feita!', 'Você tem certeza que deseja confirmar as alterações?', parent=self.editar_banco)
                if mensagem == False:
                    self.editar_banco.deiconify()
                else:
                    for banco in Banco.bancos:
                        if banco.num == lista[0] and banco.nome == lista[1]:
                            banco.num = num
                            banco.nome = nome
                    self.tvw_banco_selecionado.item(selecionado, values=(num, nome))
                    self.banco.deiconify()
                    self.editar_banco.destroy()

        def excluir_banco():
            selecionado = self.tvw_banco_selecionado.selection()
            lista = self.tvw_banco_selecionado.item(selecionado, "values")
            if selecionado != ():
                messagem = messagebox.askyesno("Cuidado!", "Tem certeza que deseja apagar o item selecionado?")
                if messagem == False:
                    self.banco.deiconify()
                else:
                    for l in lista:
                        for banco in Banco.bancos:
                            if l == banco.nome:
                                Banco.bancos.remove(banco)
                    for s in selecionado:
                        self.tvw_banco_selecionado.delete(s)
                    self.banco.deiconify()

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

        banco = Banco(123, "Santander")
        Banco.adicionar_banco(self, banco)
        cliente = Cliente("Elias de Olivera Cacau", "024.631.012-02", "Rua Letícia Rodrigues")
        cliente.banco = banco
        Cliente.adicionar_clientes(self, cliente)

#sys.setrecursionlimit(1500)
app = tk.Tk()
Tela(app)
app.mainloop()