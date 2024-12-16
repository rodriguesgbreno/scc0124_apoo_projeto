# Gerenciador de Estoque

Este é um sistema de gerenciamento de estoque com interface gráfica desenvolvida em **Tkinter**. O programa permite a administração de produtos, lotes e controle de acesso, oferecendo diferentes níveis de permissão para usuários.

---

## **Requisitos**

Para rodar o programa, você precisa ter o **Python 3** instalado. A biblioteca **Tkinter** geralmente já vem incluída, mas, caso encontre problemas, instale-a com o comando:

- **Ubuntu/Debian**:
  ```bash
  sudo apt-get install python3-tk
  ```

Além disso, antes de rodar o programa, é necessário compilar os seguintes arquivos localizados na pasta `gerenciador_de_estoque/repositorios`:

1. **`funcionarios.py`**: Gera e salva os dados dos usuários cadastrados no sistema.
2. **`produtos_exemplos.py`**: Gera e salva os dados iniciais de produtos e lotes para o sistema.

---

## **Como Rodar o Programa**

1. **Compile os arquivos necessários**:
   Certifique-se de compilar os arquivos mencionados acima para gerar os dados iniciais:
   ```bash
   python3 gerenciador_de_estoque/repositorios/funcionarios.py
   python3 gerenciador_de_estoque/repositorios/produtos_exemplos.py
   ```

2. **Execute o arquivo principal**:
   Rode o seguinte comando no diretório `gerenciador_de_estoque/ui`:
   ```bash
   python3 main.py
   ```

---

## **Usuários de Login Disponíveis**

Aqui estão os usuários cadastrados para teste, com diferentes níveis de acesso:

| **Login**            | **Senha**   | **Nível de Acesso**          |
|-----------------------|-------------|------------------------------|
| `admin`              | `admin`     | Gerente de Supermercado      |
| `joao.silva`         | `senha123`  | Gerente de Supermercado      |
| `maria.oliveira`     | `senha456`  | Gerente de Estoque           |
| `carlos.andrade`     | `senha789`  | Atendente de Caixa           |

---

## **Funcionalidades por Nível de Acesso**

O programa possui várias abas com permissões diferentes, dependendo do tipo de login:

| **Função**               | **Gerente de Supermercado** | **Gerente de Estoque** | **Atendente de Caixa** | **Todos os Usuários**   |
|--------------------------|-----------------------------|-------------------------|-------------------------|-------------------------|
| Entrada de Produto       | ✅                          | ✅                      | ❌                      | ❌                      |
| Registro de Lote         | ✅                          | ✅                      | ❌                      | ❌                      |
| Saída de Produtos        | ✅                          | ❌                      | ✅                      | ❌                      |
| Relatórios               | ✅                          | ❌                      | ❌                      | ❌                      |
| Consulta                 | ✅                          | ✅                      | ✅                      | ✅                      |

- A **aba de Consulta** pode ser acessada por qualquer usuário ou diretamente compilando o arquivo:
  ```bash
  python3 tela_consulta.py
  ```

---

## **Status do Projeto**

- A funcionalidade de **Saída de Produtos** ainda **não foi implementada**.

---
