import tkinter as tk
from tkinter import ttk

root = tk.Tk()

style = ttk.Style(root)
# set ttk theme to "clam" which support the fieldbackground option
style.theme_use("clam")
style.configure("Treeview", background="black",
                fieldbackground="black", foreground="white")

tree = ttk.Treeview(root)
tree.insert("", 0, "item", text="item")
tree.pack()

root.mainloop()
# def editar_cliente():
        #     self.top_editar_cliente = tk.Toplevel()
        #     self.top_editar_cliente.title("Editar banco")
        #     self.top_editar_cliente.geometry("200x100")
        #
        #     selecionado = self.tvw_cliente.selection()
        #     lista = self.tvw_cliente.item(selecionado, "values")
        #
        #     self.btn_nome_cli = tk.Label(self.top_editar_cliente, text="Nome:")
        #     self.btn_nome_cli.grid(column=0, row=0)
        #     self.ent_nome_cli = tk.Entry(self.top_editar_cliente)
        #     self.ent_nome_cli.grid(column=1, row=0)
        #     self.ent_nome_cli.insert(0, lista[1])
        #
        #     self.btn_cpf_cli = tk.Label(self.top_editar_cliente, text="CPF:")
        #     self.btn_cpf_cli.grid(column=0, row=1)
        #     self.ent_cpf_cli = tk.Entry(self.top_editar_cliente)
        #     self.ent_cpf_cli.grid(column=1, row=1)
        #     self.ent_cpf_cli.insert(0, lista[2])
        #
        #     self.btn_end_cli = tk.Label(self.top_editar_cliente, text="Endereço:")
        #     self.btn_end_cli.grid(column=0, row=2)
        #     self.ent_end_cli = tk.Entry(self.top_editar_cliente)
        #     self.ent_end_cli.grid(column=1, row=2)
        #     self.ent_end_cli.insert(0, lista[3])
        #
        #     self.btn_confirmar = tk.Button(self.top_editar_cliente, text='Confirmar',
        #                                    command=confirmar_edicao_cliente)
        #     self.btn_confirmar.grid(column=1, row=3, columnspan=1)
        #
        # def confirmar_edicao_cliente():
        #     id = ''
        #     nome = self.ent_nome_cli.get()
        #     cpf = self.ent_cpf_cli.get()
        #     end = self.ent_end_cli.get()
        #     selecionado = self.tvw_cliente.selection()
        #     lista = self.tvw_cliente.item(selecionado, "values")
        #
        #     for i in Cliente.clientes:
        #         if nome == i.nome:
        #             id = i.id
        #             i.nome = nome
        #             i.cpf = cpf
        #             i.endereco = end
        #
        #     if nome == lista[1] and cpf == lista[2] and end == lista[3]:
        #         mensagem = messagebox.askyesno('Nenhuma modificação feita!',
        #                                        'Você tem certeza que não deseja fazer nenhuma modificação?')
        #         if mensagem:
        #             self.top_editar_cliente.destroy()
        #         else:
        #             self.top_editar_cliente.deiconify()
        #     else:
        #         mensagem = messagebox.askyesno('Modificação feita!',
        #                                        'Você tem certeza que deseja confirmar as alterações?',
        #                                        parent=self.cliente)
        #         if mensagem:
        #             self.tvw_cliente.item(selecionado, values=(id, nome, cpf, end))
        #             self.top_editar_cliente.destroy()
        #         else:
        #             self.top_editar_cliente.deiconify()