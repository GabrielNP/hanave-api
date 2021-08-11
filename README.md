# HACKATHON HANAVE

## Introdução

Este repositório é a conclusão da API desenvolvida durante o hackathon digital promovido pela [HANAVE](https://hanave.com.br/).

Desenvolvemos um chatbot de e-commerce para pós-vendas com a plataforma ALTU e nossa própria base de dados.

### Quem somos
Olá, somos o grupo Friends!

Integrantes:
* Angélica
* Eduardo
* Gabriel
* Lucas

### Desafio

Pense em um assistente que permita o usuário ter uma experiência mais fluida entre os canais físico e digital ao realizar um pedido de suporte pós-vendas.

Alguns requisitos mínimos devem estar presentes no assistente:
* Cliente fictício (criar um perfil de cliente já cadastrado para simular os processos de pós venda)
* Devolução de produto;
* Status do produto;
* Troca de produto;
* Cancelamento;
* Críticas;
* NPS;
* FAQ (NLU)

## A API
Descrição dos requisitos necessários para executar em um sistema operacional Linux. 

S.O. utilizado: Kubuntu

### Dependências 
* build-essential
    
    ```bash
    sudo apt-get install build-essential -y
    ```
* Python
    ```bash
    sudo apt-get install python3.8 -y
    sudo apt-get install python3.8-dev -y
    sudo apt-get install python3.8-venv -y
    sudo apt-get install python3-pip
    ```

### Configurar banco
1. Criei ou tenha uma conexão com banco de dados

    \* Banco utilizado: PostgreSQL

2. Adicione o schema hanave

### Configurar ambiente
1. Crie o arquivo `.env` a partir do `.env.example` e preencha com as informações do seu banco de dados
2. Execute:
    

    ```bash
    # cria as tabelas no schema hanave
    make runcommand command=create-tables
    ```

    ```bash
    # popula as tabelas criadas
    make runcommand command=seed-tables
    ```

    ```bash
    # instala bibliotecas python necessárias
    make setup
    ```

 ### Como rodar
Após instalar as dependências necessárias e realizar as configurações inciais, execute:

```bash
# serve a aplicação Flask na porta :5000
make run
```
