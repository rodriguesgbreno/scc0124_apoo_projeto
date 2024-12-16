from datetime import date
from produtos_utils import Produto, Lote, salvar_produtos_em_json, salvar_lotes_em_json, carregar_produtos_de_json, carregar_lotes_de_json

# Verificar ou criar os arquivos caso não existam
produtos = carregar_produtos_de_json()
lotes = carregar_lotes_de_json()

# Se os arquivos estavam vazios, criar exemplos iniciais
if not produtos:
    # Produtos
    exemplos_produtos = [
        Produto(nome="Sabão em Pó", categoria="Limpeza"),
        Produto(nome="Leite", categoria="Alimentos"),
        Produto(nome="Arroz", categoria="Alimentos"),
        Produto(nome="Detergente Líquido", categoria="Limpeza"),
        Produto(nome="Papel Toalha", categoria="Limpeza"),
        Produto(nome="Feijão Preto", categoria="Alimentos"),
        Produto(nome="Macarrão Espaguete", categoria="Alimentos"),
        Produto(nome="Óleo de Soja", categoria="Alimentos"),
        Produto(nome="Açúcar Refinado", categoria="Alimentos"),
        Produto(nome="Café em Pó", categoria="Alimentos"),
        Produto(nome="Shampoo", categoria="Higiene"),
        Produto(nome="Condicionador", categoria="Higiene"),
        Produto(nome="Sabonete Líquido", categoria="Higiene"),
        Produto(nome="Pasta de Dente", categoria="Higiene"),
        Produto(nome="Desodorante", categoria="Higiene"),
        Produto(nome="Refrigerante Cola", categoria="Bebidas"),
        Produto(nome="Refrigerante Guaraná", categoria="Bebidas"),
        Produto(nome="Suco de Laranja", categoria="Bebidas"),
        Produto(nome="Água Mineral", categoria="Bebidas"),
        Produto(nome="Cerveja Lata", categoria="Bebidas"),
        Produto(nome="Amaciante de Roupas", categoria="Limpeza"),
        Produto(nome="Sabão Líquido para Roupas", categoria="Limpeza"),
        Produto(nome="Esponja de Aço", categoria="Limpeza"),
        Produto(nome="Fralda Descartável", categoria="Higiene"),
        Produto(nome="Papel Higiênico", categoria="Higiene"),
        Produto(nome="Queijo Mussarela", categoria="Alimentos"),
        Produto(nome="Manteiga", categoria="Alimentos"),
        Produto(nome="Presunto Fatiado", categoria="Alimentos"),
        Produto(nome="Farinha de Trigo", categoria="Alimentos"),
        Produto(nome="Fermento Biológico", categoria="Alimentos"),
        Produto(nome="Chocolate em Barra", categoria="Alimentos"),
        Produto(nome="Bolacha de Maisena", categoria="Alimentos"),
        Produto(nome="Cereal Matinal", categoria="Alimentos"),
        Produto(nome="Água Sanitária", categoria="Limpeza"),
        Produto(nome="Vassoura", categoria="Limpeza"),
        Produto(nome="Rodo de Limpeza", categoria="Limpeza"),
        Produto(nome="Biscoito Recheado", categoria="Alimentos"),
        Produto(nome="Laranja", categoria="Hortifruti"),
        Produto(nome="Tomate", categoria="Hortifruti"),
        Produto(nome="Cebola", categoria="Hortifruti"),
        Produto(nome="Batata", categoria="Hortifruti"),
        Produto(nome="Alface", categoria="Hortifruti")
    ]
    produtos = exemplos_produtos
    salvar_produtos_em_json(produtos)

if not lotes:
    # Lotes
    exemplos_lotes = [
        Lote(produto_id=1, quantidade=50, data_validade=date(2025, 6, 15), preco=12.5),
        Lote(produto_id=2, quantidade=200, data_validade=date(2024, 12, 31), preco=4.0),
        Lote(produto_id=3, quantidade=100, data_validade=date(2024, 8, 20), preco=20.0),
        Lote(produto_id=3, quantidade=150, data_validade=date(2025, 1, 15), preco=18.5),
        Lote(produto_id=5, quantidade=300, data_validade=date(2025, 3, 10), preco=6.5),
        Lote(produto_id=7, quantidade=120, data_validade=date(2023, 12, 1), preco=3.2),
        Lote(produto_id=7, quantidade=90, data_validade=date(2024, 5, 1), preco=3.5),
        Lote(produto_id=10, quantidade=60, data_validade=date(2023, 10, 10), preco=18.0),
        Lote(produto_id=10, quantidade=150, data_validade=date(2024, 11, 20), preco=17.5),
        Lote(produto_id=12, quantidade=400, data_validade=date(2026, 2, 15), preco=10.0),
        Lote(produto_id=14, quantidade=250, data_validade=date(2025, 9, 30), preco=5.5),
        Lote(produto_id=15, quantidade=50, data_validade=date(2024, 1, 1), preco=8.0),
        Lote(produto_id=18, quantidade=100, data_validade=date(2023, 11, 25), preco=3.8),
        Lote(produto_id=18, quantidade=75, data_validade=date(2024, 7, 15), preco=4.0),
        Lote(produto_id=19, quantidade=500, data_validade=date(2025, 6, 30), preco=2.5),
        Lote(produto_id=19, quantidade=300, data_validade=date(2023, 12, 15), preco=2.0),
        Lote(produto_id=23, quantidade=200, data_validade=date(2024, 5, 10), preco=1.2),
        Lote(produto_id=30, quantidade=150, data_validade=date(2023, 9, 1), preco=1.8),
        Lote(produto_id=30, quantidade=200, data_validade=date(2025, 7, 1), preco=2.0),
        Lote(produto_id=35, quantidade=100, data_validade=date(2025, 12, 31), preco=8.0)
    ]
    lotes = exemplos_lotes
    salvar_lotes_em_json(lotes)

# Mensagem de Sucesso
print("Arquivo Criado")

