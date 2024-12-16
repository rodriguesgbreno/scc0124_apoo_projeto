import tkinter as tk
from tkinter import ttk
from datetime import datetime

import tela_funcoes
import tela_consulta
import tela_relatorios

from app_icone import set_icon

# funcao para atualizar a hora no painel
def atualizar_hora(painel_hora, root):
    agora = datetime.now().strftime("%H:%M:%S")
    painel_hora.config(text=f"Hora: {agora}")
    root.after(1000, atualizar_hora, painel_hora, root)  # atualiza a cada segundo

# funca com os dados do funcionarios
def infos_funcionario(frame_funcionario, dados_usuario):
    # adiciona informacoes do funcionarios
    tk.Label(frame_funcionario, text="Nome do Funcionário:", bg='lightgrey').pack(anchor=tk.W, pady=(10, 0))
    tk.Label(frame_funcionario, text=dados_usuario.get("nome"), bg='lightgrey').pack(anchor=tk.W)

    tk.Label(frame_funcionario, text="Função do Funcionário:", bg='lightgrey').pack(anchor=tk.W, pady=(10, 0))
    tk.Label(frame_funcionario, text=dados_usuario.get("funcao"), bg='lightgrey').pack(anchor=tk.W)



# funcao para criar a janela com as permissoes que apenas o funcionario tem
def abrir_janela_funcionario(root, mostrar_login, dados_usuario):
    janela_funcionario = tk.Toplevel(root)
    janela_funcionario.title("Janela do Funcionário")

    # ícone da aplicação
    set_icon(janela_funcionario)
    
    largura_janela = 800
    altura_janela = 500

    # centraliza a nova janela
    centralizar_janela(janela_funcionario, largura_janela, altura_janela)

    frame_funcionario = tk.Frame(janela_funcionario, padx=10, pady=10, width=300, bg='lightgrey')
    frame_funcionario.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # adiciona informações do funcionário
    infos_funcionario(frame_funcionario, dados_usuario)

    # adiciona o botão "Desconectar" logo abaixo da hora
    painel_hora = tk.Label(frame_funcionario, text="Hora: ", bg='lightgrey')
    painel_hora.pack(anchor=tk.W, pady=(10, 0))
    tk.Button(frame_funcionario, text="Desconectar", command=lambda: desconectar(root, janela_funcionario, mostrar_login)).pack(pady=(10, 0), anchor=tk.W)

    # criação do Notebook (abas)
    notebook = ttk.Notebook(janela_funcionario)

    # Determina o nível de acesso do funcionário
    nivel_acesso = dados_usuario.get("nivel_acesso")

    # Adiciona abas conforme o nível de acesso
    if nivel_acesso == 3:  # Acesso total
        aba_entrada = tk.Frame(notebook)
        aba_lotes = tk.Frame(notebook)
        aba_saida = tk.Frame(notebook)
        aba_relatorios = tk.Frame(notebook)
        notebook.add(aba_entrada, text="Entrada de Produtos")
        notebook.add(aba_lotes, text="Registro de Lote")
        notebook.add(aba_saida, text="Saída de Produtos")
        notebook.add(aba_relatorios, text="Relatórios")
        tela_funcoes.aba_entrada_produtos(aba_entrada)
        tela_funcoes.aba_entrada_lotes(aba_lotes)
        tela_funcoes.aba_saida_produtos(aba_saida)
        tela_relatorios.relatorio_produtos(aba_relatorios)
    elif nivel_acesso == 2:  # Apenas entrada de produtos
        aba_entrada = tk.Frame(notebook)
        aba_lotes = tk.Frame(notebook)
        notebook.add(aba_entrada, text="Entrada de Produtos")
        notebook.add(aba_lotes, text="Registro de Lote")
        tela_funcoes.aba_entrada_produtos(aba_entrada)
        tela_funcoes.aba_entrada_lotes(aba_lotes)
    elif nivel_acesso == 1:  # Apenas saída de produtos
        aba_saida = tk.Frame(notebook)
        notebook.add(aba_saida, text="Saída de Produtos")
        tela_funcoes.aba_saida_produtos(aba_saida)
    
    aba_consulta = tk.Frame(notebook)
    notebook.add(aba_consulta, text="Consulta de Produtos")
    tela_consulta.aba_consulta(aba_consulta)

    # Exibe o Notebook
    notebook.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Ajusta o grid para que as colunas se expandam igualmente
    janela_funcionario.grid_columnconfigure(0, weight=1)
    janela_funcionario.grid_columnconfigure(1, weight=3)

    # Atualiza a hora
    atualizar_hora(painel_hora, janela_funcionario)

def centralizar_janela(janela, largura, altura):
    # obtem as dimensoes da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # calcula as coordenadas para centralizar a janela
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)

    # define o tamanho e a posicao da janela
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

# funcao para fechar a janela do funcionario e abrir a tela de login
def desconectar(root, janela_funcionario, mostrar_login):
    janela_funcionario.destroy() 
    mostrar_login()
