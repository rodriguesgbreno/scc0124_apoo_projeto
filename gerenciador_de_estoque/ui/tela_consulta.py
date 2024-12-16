import tkinter as tk
from tkinter import ttk
import sys
import os

from app_icone import set_icon

# Adicionar o caminho relativo para a pasta 'repositorios'
caminho_repositorios = os.path.join(os.path.dirname(__file__), "..", "repositorios")
sys.path.append(caminho_repositorios)

from produtos_utils import carregar_produtos_de_json, carregar_lotes_de_json

# Carregar os dados existentes
produtos = carregar_produtos_de_json()
lotes = carregar_lotes_de_json()

# Função para realizar a consulta
def realizar_consulta(tipo_busca, valor_busca, lista_resultados):
    # Limpa a lista de resultados
    lista_resultados.delete(0, tk.END)

    # Busca produtos correspondentes
    resultados = []
    for produto in produtos:
        if tipo_busca == "ID" and str(produto.id) == valor_busca:
            resultados.append(produto)
        elif tipo_busca == "Nome" and valor_busca.lower() in produto.nome.lower():
            resultados.append(produto)
        elif tipo_busca == "Categoria" and valor_busca.lower() in produto.categoria.lower():
            resultados.append(produto)

    # Exibe os resultados
    if resultados:
        for produto in resultados:
            # Adiciona as informações do produto
            lista_resultados.insert(tk.END, f"ID: {produto.id}")
            lista_resultados.insert(tk.END, f"Nome: {produto.nome}")
            lista_resultados.insert(tk.END, f"Categoria: {produto.categoria}")
            
            # Verifica se há lotes associados ao produto
            lotes_produto = [lote for lote in lotes if lote.produto_id == produto.id]
            if lotes_produto:
                lista_resultados.insert(tk.END, "Lotes Disponíveis:")
                for i, lote in enumerate(lotes_produto, start=1):
                    lista_resultados.insert(tk.END, f"  Lote {i}:")
                    lista_resultados.insert(tk.END, f"    Quantidade: {lote.quantidade}")
                    lista_resultados.insert(tk.END, f"    Preço: R$ {lote.preco:.2f}")
                    lista_resultados.insert(tk.END, f"    Data Validade: {lote.data_validade}")
            else:
                lista_resultados.insert(tk.END, "Sem lotes disponíveis.")
            lista_resultados.insert(tk.END, "-" * 50)
    else:
        lista_resultados.insert(tk.END, "Nenhum resultado encontrado.")

# Função para centralizar a janela
def centralizar_janela(janela):
    janela.update_idletasks() 
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def aba_consulta(frame):
    # Tipo de busca
    tk.Label(frame, text="Buscar por:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    tipo_busca = ttk.Combobox(frame, values=["ID", "Nome", "Categoria"])
    tipo_busca.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
    tipo_busca.current(0)

    # Entrada de valor para busca
    tk.Label(frame, text="Valor:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    entrada_valor = tk.Entry(frame)
    entrada_valor.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

    # Botão para realizar a consulta
    lista_resultados = tk.Listbox(frame, width=50, height=10)
    lista_resultados.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky=tk.NSEW)

    tk.Button(
        frame,
        text="Consultar",
        command=lambda: realizar_consulta(tipo_busca.get(), entrada_valor.get(), lista_resultados)
    ).grid(row=2, column=0, columnspan=3, pady=10)

    # Botão para sair
    tk.Button(frame, text="Fechar", command=frame.quit).grid(row=4, column=0, columnspan=3, pady=10)

# Função para criar a tela de consulta
def tela_consulta():
    janela = tk.Tk()
    janela.title("Consulta de Produtos")
    
    # Ícone da aplicação
    set_icon(janela)

    # Configuração do layout da janela
    janela.rowconfigure(3, weight=1)  # Permitir que a lista de resultados expanda verticalmente
    janela.columnconfigure(1, weight=1)  # Permitir que os widgets se expandam horizontalmente

    # Cria o frame principal e passa para aba_consulta
    frame = tk.Frame(janela)
    frame.pack(fill=tk.BOTH, expand=True)
    aba_consulta(frame)

    # Ajusta o tamanho ideal da janela com base nos widgets
    janela.update_idletasks()
    janela.geometry("")
    centralizar_janela(janela)

    janela.mainloop()

# Executar a tela de consulta
if __name__ == "__main__":
    tela_consulta()
