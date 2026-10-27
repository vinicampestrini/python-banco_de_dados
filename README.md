# Sistema de gerenciamento de pets desenvolvido em Python, integrado ao Oracle Database para realizar operações de cadastro, consulta, atualização e exclusão de registros.

## Funcionalidades

- **Cadastrar pets:** registra o tipo, o nome e a idade do pet.
- **Listar pets:** exibe os pets cadastrados em formato de tabela.
- **Alterar pets:** permite atualizar os dados de um pet pelo ID.
- **Excluir pets:** remove um pet específico do banco de dados.
- **Excluir todos os registros:** permite apagar todos os pets cadastrados.

## Tecnologias utilizadas

- Python
- Oracle Database
- Pandas
- SQL

## Estrutura do banco de dados

O projeto utiliza uma tabela chamada `petshop`, com os seguintes campos:

| Campo      | Tipo         | Descrição            |
| ---------- | ------------ | -------------------- |
| `id`       | INT          | Identificador do pet |
| `tipo_pet` | VARCHAR2(30) | Tipo do animal       |
| `nome_pet` | VARCHAR2(30) | Nome do pet          |
| `idade`    | INT          | Idade do pet         |

O campo `id` deve ser configurado no Oracle Database para gerar identificadores automaticamente.

## Como executar o projeto

### 1. Pré-requisitos

- Python instalado.
- Oracle Database disponível e acessível.
- Dependências instaladas.

### 2. Clone o repositório

```bash
git clone https://github.com/vinicampestrini/python-banco_de_dados.git
```

Entre na pasta do projeto:

```bash
cd python-banco_de_dados
```

### 3. Instale as dependências

```bash
python -m pip install oracledb pandas
```

### 4. Configure a conexão com o banco de dados

No arquivo `principal.py`, configure os dados de conexão com o Oracle Database:

- Usuário do banco de dados.
- Senha.
- DSN de conexão.

### 5. Execute o programa

```bash
python principal.py
```

O sistema exibirá um menu interativo no terminal para selecionar as operações disponíveis.

## Objetivo do projeto

Praticar conceitos de programação em Python, manipulação de dados, integração com banco de dados relacional e execução de comandos SQL em um sistema CRUD.

##
