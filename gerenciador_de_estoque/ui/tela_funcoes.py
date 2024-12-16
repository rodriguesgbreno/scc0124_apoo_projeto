import tkinter as tk
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

# Lista temporária para armazenar produtos adicionados na execução atual
produtos_adicionados_temporarios = []

# Função para atualizar a lista de produtos na interface com formatação personalizada
def atualizar_lista_produtos(lista_produtos):
    lista_produtos.delete(0, tk.END)
    for produto in produtos_adicionados_temporarios:
        lista_produtos.insert(tk.END, f"ID: {produto.id}")
        lista_produtos.insert(tk.END, f"Nome: {produto.nome}")
        lista_produtos.insert(tk.END, f"Categoria: {produto.categoria}")
        lista_produtos.insert(tk.END, "-" * 50)  # Separador entre produtos

# Lista temporária para armazenar lotes adicionados na execução atual
lotes_adicionados_temporarios = []

# Função para atualizar a lista de lotes na interface com formatação personalizada
def atualizar_lista_lotes(lista_lotes):
    lista_lotes.delete(0, tk.END)
    for lote in lotes_adicionados_temporarios:
        lista_lotes.insert(tk.END, f"Produto ID: {lote.produto_id}")
        lista_lotes.insert(tk.END, "  Lote:")
        lista_lotes.insert(tk.END, f"    Quantidade: {lote.quantidade}")
        lista_lotes.insert(tk.END, f"    Preço: R$ {lote.preco:.2f}")
        lista_lotes.insert(tk.END, f"    Data de Validade: {lote.data_validade}")
        lista_lotes.insert(tk.END, "-" * 50)  # Separador entre lotes

# Função para adicionar um produto
def adicionar_produto(nome, categoria, lista_produtos):
    if nome and categoria:
        novo_produto = Produto(nome=nome, categoria=categoria)
        produtos.append(novo_produto)  # Adiciona ao JSON
        produtos_adicionados_temporarios.append(novo_produto)  # Adiciona à lista temporária
        salvar_produtos_em_json(produtos)  # Atualiza o arquivo JSON com todos os produtos
        atualizar_lista_produtos(lista_produtos)

# Função para adicionar um lote
def adicionar_lote(produto_id, quantidade, preco, validade, lista_lotes):
    try:
        produto_id = int(produto_id)
        quantidade = int(quantidade)
        preco = float(preco)
        validade = date.fromisoformat(validade)  # Validade no formato AAAA-MM-DD
        
        # Verifica se o produto existe no sistema
        if any(produto.id == produto_id for produto in produtos):
            novo_lote = Lote(
                produto_id=produto_id, 
                quantidade=quantidade, 
                data_validade=validade, 
                preco=preco
            )
            lotes.append(novo_lote)  # Adiciona ao JSON
            lotes_adicionados_temporarios.append(novo_lote)  # Adiciona à lista temporária
            salvar_lotes_em_json(lotes)  # Atualiza o arquivo JSON com todos os lotes
            atualizar_lista_lotes(lista_lotes)
        else:
            print(f"Erro: Produto com ID {produto_id} não encontrado.")
    except ValueError:
        print("Erro: Verifique os dados inseridos para o lote.")

# Função para criar a aba de entrada de produtos
def aba_entrada_produtos(frame):
    tk.Label(frame, text="Nome do Produto").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    entrada_nome = tk.Entry(frame)
    entrada_nome.grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(frame, text="Categoria do Produto").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    entrada_categoria = tk.Entry(frame)
    entrada_categoria.grid(row=1, column=1, padx=10, pady=10)
    
    lista_produtos = tk.Listbox(frame, width=50, height=10)
    lista_produtos.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    atualizar_lista_produtos(lista_produtos)

    tk.Button(frame, text="Adicionar Produto", command=lambda: adicionar_produto(entrada_nome.get(), entrada_categoria.get(), lista_produtos)).grid(row=2, column=0, columnspan=2, pady=10)

# Função para criar a aba de entrada de lotes
def aba_entrada_lotes(frame):
    tk.Label(frame, text="Código do Produto").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    entrada_codigo = tk.Entry(frame)
    entrada_codigo.grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(frame, text="Quantidade").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    entrada_quantidade = tk.Entry(frame)
    entrada_quantidade.grid(row=1, column=1, padx=10, pady=10)
    
    tk.Label(frame, text="Preço").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    entrada_preco = tk.Entry(frame)
    entrada_preco.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(frame, text="Data de Validade (AAAA-MM-DD)").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
    entrada_validade = tk.Entry(frame)
    entrada_validade.grid(row=3, column=1, padx=10, pady=10)
    
    lista_lotes = tk.Listbox(frame, width=50, height=10)
    lista_lotes.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    atualizar_lista_lotes(lista_lotes)

    tk.Button(frame, text="Adicionar Lote", command=lambda: adicionar_lote(entrada_codigo.get(), entrada_quantidade.get(), entrada_preco.get(), entrada_validade.get(), lista_lotes)).grid(row=4, column=0, columnspan=2, pady=10)

# Função para criar a aba de saída de produtos
def aba_saida_produtos(frame):
    tk.Label(frame, text="Código do Produto").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    entrada_codigo = tk.Entry(frame)
    entrada_codigo.grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(frame, text="Quantidade").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    entrada_quantidade = tk.Entry(frame)
    entrada_quantidade.grid(row=1, column=1, padx=10, pady=10)
    
    tk.Button(frame, text="Registrar Saída").grid(row=2, column=0, columnspan=2, pady=10)
    
    lista_saida_produtos = tk.Listbox(frame, width=50, height=10)
    lista_saida_produtos.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
