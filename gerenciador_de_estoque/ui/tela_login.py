import tkinter as tk
from tkinter import messagebox
import json
import os

from app_icone import set_icon
from tela_funcionario import abrir_janela_funcionario

# Caminho absoluto para o arquivo funcionarios.json
arquivo_funcionario = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "repositorios", "funcionarios.json")
)

# Carregar os funcionários do arquivo JSON
with open(arquivo_funcionario, "r") as arquivo:
    funcionarios = json.load(arquivo)

# Função para mostrar a tela de login novamente
def mostrar_login():
    global root
    root.deiconify()

    # Limpa os campos de entrada
    entrada_usuario.delete(0, tk.END)
    entrada_senha.delete(0, tk.END)

# Função para verificar login
def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    # Verifica as credenciais no arquivo de funcionários
    for funcionario in funcionarios:
        if funcionario["login"] == usuario and funcionario["senha"] == senha:
            messagebox.showinfo("Login bem-sucedido", f"Bem-vindo, {funcionario['nome']}!")
            root.withdraw()
            
            # Abre a janela do funcionário com os dados dele
            abrir_janela_funcionario(root, mostrar_login, funcionario)
            return

    # Mensagem de erro se o login falhar
    messagebox.showerror("Erro de Login", "Usuário ou senha incorretos.")

# Função para centralizar a janela
def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Função principal
def main():
    global root, entrada_usuario, entrada_senha
    root = tk.Tk()
    root.title("Tela de Login")

    # Ícone da aplicação
    set_icon(root)

    # Configura o tamanho da janela
    largura_janela = 300
    altura_janela = 150

    # Centraliza a janela
    centralizar_janela(root, largura_janela, altura_janela)

    # Configuração do layout
    tk.Label(root, text="Usuário").grid(row=0, column=0, padx=10, pady=10)
    entrada_usuario = tk.Entry(root)
    entrada_usuario.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Senha").grid(row=1, column=0, padx=10, pady=10)
    entrada_senha = tk.Entry(root, show="*")
    entrada_senha.grid(row=1, column=1, padx=10, pady=10)

    botao_login = tk.Button(root, text="Login", command=verificar_login)
    botao_login.grid(row=2, column=0, columnspan=2, pady=10)

    # Inicia o loop principal da interface gráfica
    root.mainloop()

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
