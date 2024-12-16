import tkinter as tk
from tkinter import ttk
from datetime import date

import sys
import os

# Caminho relativo para a pasta 'utils' dentro de 'repositorios'
caminho_utils = os.path.join(os.path.dirname(__file__), "..", "repositorios")

# Adiciona o caminho ao PYTHONPATH
sys.path.append(caminho_utils)

# Agora você pode importar o módulo
from produtos_utils import Produto, Lote, salvar_produtos_em_json, salvar_lotes_em_json, carregar_produtos_de_json, carregar_lotes_de_json

# Carregar os dados existentes
produtos = carregar_produtos_de_json()
lotes = carregar_lotes_de_json()

# Função para identificar produtos com baixo estoque com base no limite definido pelo usuário
def gerar_relatorio_baixo_estoque(lista_resultados, entrada_limite):
    lista_resultados.delete(0, tk.END)
    try:
        limite = int(entrada_limite.get())
    except ValueError:
        lista_resultados.insert(tk.END, "Erro: Insira um número válido para o limite mínimo.")
        return

    for lote in lotes:
        if lote.quantidade < limite:
            produto = next((p for p in produtos if p.id == lote.produto_id), None)
            if produto:
                lista_resultados.insert(
                    tk.END,
                    f"Produto: {produto.nome} | Estoque: {lote.quantidade} | Lote: {lote.data_validade}"
                )
    if not lista_resultados.size():
        lista_resultados.insert(tk.END, "Nenhum produto com estoque abaixo do limite.")

# Função para identificar produtos vencidos
def gerar_relatorio_vencidos(lista_resultados):
    lista_resultados.delete(0, tk.END)
    data_atual = date.today()
    for lote in lotes:
        if lote.data_validade < data_atual:
            produto = next((p for p in produtos if p.id == lote.produto_id), None)
            if produto:
                lista_resultados.insert(
                    tk.END,
                    f"Produto: {produto.nome} | Lote: {lote.data_validade} | Estoque: {lote.quantidade}"
                )
    if not lista_resultados.size():
        lista_resultados.insert(tk.END, "Nenhum produto vencido encontrado.")

# Função para criar relatórios dentro da aba de relatórios
def relatorio_produtos(frame):
    # Notebook para abas de relatórios
    notebook = ttk.Notebook(frame)

    # Aba de produtos com baixo estoque
    aba_baixo_estoque = tk.Frame(notebook)
    tk.Label(aba_baixo_estoque, text="Relatório de Produtos com Baixo Estoque").pack(padx=10, pady=5, anchor=tk.W)

    tk.Label(aba_baixo_estoque, text="Limite Mínimo:").pack(padx=10, pady=5, anchor=tk.W)
    entrada_limite = tk.Entry(aba_baixo_estoque, width=10)
    entrada_limite.pack(padx=10, pady=5, anchor=tk.W)
    entrada_limite.insert(0, "50")  # Valor padrão para o limite

    lista_baixo_estoque = tk.Listbox(aba_baixo_estoque, width=50, height=10)
    lista_baixo_estoque.pack(padx=10, pady=10)

    tk.Button(
        aba_baixo_estoque,
        text="Gerar Relatório",
        command=lambda: gerar_relatorio_baixo_estoque(lista_baixo_estoque, entrada_limite)
    ).pack(pady=10)

    # Aba de produtos vencidos
    aba_vencidos = tk.Frame(notebook)
    tk.Label(aba_vencidos, text="Relatório de Produtos Vencidos").pack(padx=10, pady=5, anchor=tk.W)

    lista_vencidos = tk.Listbox(aba_vencidos, width=50, height=10)
    lista_vencidos.pack(padx=10, pady=10)

    tk.Button(
        aba_vencidos,
        text="Gerar Relatório",
        command=lambda: gerar_relatorio_vencidos(lista_vencidos)
    ).pack(pady=10)

    # Adicionar abas ao notebook
    notebook.add(aba_baixo_estoque, text="Baixo Estoque")
    notebook.add(aba_vencidos, text="Vencidos")

    # Exibir o notebook
    notebook.pack(fill=tk.BOTH, expand=True)