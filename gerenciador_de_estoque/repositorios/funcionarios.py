import json

class Funcionario:
    def __init__(self, nome, funcao, nivel_acesso, login, senha):
        self.nome = nome
        self.funcao = funcao
        self.nivel_acesso = nivel_acesso
        self.login = login
        self.senha = senha

    def to_dict(self):
        return {
            "nome": self.nome,
            "funcao": self.funcao,
            "nivel_acesso": self.nivel_acesso,
            "login": self.login,
            "senha": self.senha,
        }

# Lista para armazenar os funcionarios
funcionarios = [
    Funcionario("Admin", "Admin", 3, "admin", "admin"),
    Funcionario("Joao Silva", "Gerente de Supermercado", 3, "joao.silva", "senha123"),
    Funcionario("Maria Oliveira", "Gerente de Estoque", 2, "maria.oliveira", "senha456"),
    Funcionario("Carlos Santos", "Atendente de Caixa", 1, "carlos.santos", "senha789")
]

# Salvando em um arquivo JSON
with open("funcionarios.json", "w") as arquivo:
    json.dump([funcionario.to_dict() for funcionario in funcionarios], arquivo, indent=4)

print("Funcionários salvos no arquivo 'funcionarios.json'.")
