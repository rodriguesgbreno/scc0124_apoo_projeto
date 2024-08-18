1. Introdução

Objetivo:
O sistema de controle de estoque visa auxiliar pequenas empresas na gestão de inventário, registrando a entrada e saída de produtos, controlando o nível de estoque e fornecendo relatórios sobre a movimentação dos itens. O objetivo é melhorar a eficiência e reduzir erros associados ao gerenciamento manual de estoque.

Atores e Stakeholders:

    Funcionário: Utiliza o sistema para registrar entradas e saídas de produtos e consultar o status atual do estoque.
    Gerente: Supervisiona o sistema, gerencia categorias e produtos, e gera relatórios de desempenho e de inventário.
    Administrador: Configura o sistema, gerencia usuários e controla permissões de acesso.

Principais Funcionalidades:

    Cadastro de Produtos: Permite adicionar, editar e remover produtos do inventário.
    Registro de Entrada e Saída: Registra a entrada de novos produtos e a saída de produtos vendidos ou usados.
    Consulta de Estoque: Permite visualizar o estoque atual de produtos, com informações detalhadas como quantidade disponível, local no armazém, e data de validade.
    Relatórios: Gera relatórios sobre o status do estoque, movimentação de produtos e alertas de níveis baixos de inventário.

Resultados Esperados:

    Eficiência: Redução de erros na gestão de inventário e otimização do controle de estoque.
    Visibilidade: Melhoria na visibilidade do status do estoque e na tomada de decisões.
    Relatórios Precisos: Facilitação da análise de desempenho e planejamento de compras.

2. Especificação de Requisitos

2.1 - Histórias de Usuário



2.2 - Personas

    

2.3 - Diagrama de Casos de Uso

    Funcionário: Registrar entrada de produtos, registrar saída de produtos, consultar estoque.
    Gerente: Gerar relatórios, consultar status de estoque.
    Administrador: Configurar sistema, gerenciar usuários e permissões.

2.4 - Especificação de Casos de Uso Textuais Abstratos

    Registrar Entrada de Produtos: O funcionário acessa o sistema, seleciona a opção de entrada de produtos, insere as informações do produto (nome, quantidade, data de validade), e confirma a entrada.
    Gerar Relatórios: O gerente acessa a seção de relatórios, seleciona o tipo de relatório desejado, define o período, e gera o relatório que é exibido.

2.5 - Especificação de Casos de Uso Textuais Estendidos

    Registrar Saída de Produtos (Funcionário): O funcionário seleciona a opção de saída de produtos, insere os detalhes do produto e a quantidade, confirma a saída e o sistema atualiza o inventário em tempo real.

3. Arquitetura do Sistema

Diagrama de Componentes:

    Frontend: Interface de usuário para interação (web ou aplicativo móvel).
    Backend: Servidor que gerencia a lógica de negócios e interage com o banco de dados.
    Banco de Dados: Armazena informações sobre produtos, movimentações e usuários.

Descrição dos Componentes:

    Frontend: Interface para inserção e consulta de dados.
    Backend: Lógica para processamento de entradas/saídas, geração de relatórios e gestão de usuários.
    Banco de Dados: Armazena informações sobre produtos, entradas, saídas e usuários.

4. Modelo de Classes

Diagrama de Classes:


5. Discussões
