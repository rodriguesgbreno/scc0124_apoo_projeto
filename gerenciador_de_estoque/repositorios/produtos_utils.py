import json
import os
from datetime import date

# Contador global para IDs de produtos
contador_id_produto = 1

# Caminho para salvar os arquivos JSON dentro de 'repositorios'
PASTA_REPOSITORIOS = os.path.dirname(__file__)

class Produto:
    def __init__(self, nome, categoria):
        global contador_id_produto
        self.id = contador_id_produto  # Atribui o próximo ID disponível
        contador_id_produto += 1  # Incrementa o contador para o próximo produto
        self.nome = nome
        self.categoria = categoria

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "categoria": self.categoria,
        }

    def __str__(self):
        return f"Produto[ID: {self.id}, Nome: {self.nome}, Categoria: {self.categoria}]"

class Lote:
    def __init__(self, produto_id, quantidade, data_validade, preco):
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.data_validade = data_validade
        self.preco = preco

    def to_dict(self):
        return {
            "produto_id": self.produto_id,
            "quantidade": self.quantidade,
            "data_validade": self.data_validade.strftime("%Y-%m-%d"),
            "preco": self.preco,
        }

    def __str__(self):
        return (f"Lote[Produto ID: {self.produto_id}, Quantidade: {self.quantidade}, "
                f"Validade: {self.data_validade}, Preço: {self.preco:.2f}]")

# Função para salvar os produtos em um arquivo JSON
def salvar_produtos_em_json(produtos, arquivo="produtos.json"):
    caminho_arquivo = os.path.join(PASTA_REPOSITORIOS, arquivo)
    with open(caminho_arquivo, "w") as f:
        json.dump([produto.to_dict() for produto in produtos], f, indent=4)
    print(f"Produtos salvos em {caminho_arquivo}")

# Função para carregar produtos de um arquivo JSON
def carregar_produtos_de_json(arquivo="produtos.json"):
    global contador_id_produto
    caminho_arquivo = os.path.join(PASTA_REPOSITORIOS, arquivo)
    try:
        with open(caminho_arquivo, "r") as f:
            produtos_dict = json.load(f)
            produtos = []
            for produto_data in produtos_dict:
                produto = Produto(produto_data["nome"], produto_data["categoria"])
                produto.id = produto_data["id"]
                produtos.append(produto)
            contador_id_produto = max(produto.id for produto in produtos) + 1
            return produtos
    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo} não encontrado. Criando um novo arquivo.")
        with open(caminho_arquivo, "w") as f:
            json.dump([], f, indent=4)
        return []

# Função para salvar os lotes em um arquivo JSON
def salvar_lotes_em_json(lotes, arquivo="lotes.json"):
    caminho_arquivo = os.path.join(PASTA_REPOSITORIOS, arquivo)
    with open(caminho_arquivo, "w") as f:
        json.dump([lote.to_dict() for lote in lotes], f, indent=4)
    print(f"Lotes salvos em {caminho_arquivo}")

# Função para carregar lotes de um arquivo JSON
def carregar_lotes_de_json(arquivo="lotes.json"):
    caminho_arquivo = os.path.join(PASTA_REPOSITORIOS, arquivo)
    try:
        with open(caminho_arquivo, "r") as f:
            lotes_dict = json.load(f)
            lotes = []
            for lote_data in lotes_dict:
                lote = Lote(
                    produto_id=lote_data["produto_id"],
                    quantidade=lote_data["quantidade"],
                    data_validade=date.fromisoformat(lote_data["data_validade"]),
                    preco=lote_data["preco"],
                )
                lotes.append(lote)
            return lotes
    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo} não encontrado. Criando um novo arquivo.")
        with open(caminho_arquivo, "w") as f:
            json.dump([], f, indent=4)
        return []
