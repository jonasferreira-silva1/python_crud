CRUD Flask Application
Este projeto é uma aplicação CRUD desenvolvida com Flask, permitindo a gestão de produtos com atributos de nome e preço. 
A aplicação se conecta a um banco de dados MySQL para armazenar os dados e usa Docker para simplificar o ambiente de desenvolvimento e execução.

Índice
1. Pré-requisitos
2. Estrutura do Projeto
3. Configuração e Execução
4. Rotas da Aplicação
5. Documentação das Funções
   
Pré-requisitos
Para rodar este projeto, você precisará das seguintes ferramentas:

Docker - Para rodar a aplicação e o banco de dados MySQL em containers.
Docker Compose - Para orquestrar os containers do projeto.
Python 3.9 - Recomendado para desenvolvimento local, caso queira rodar sem Docker.
MySQL - Necessário caso opte por rodar o banco de dados localmente (não via Docker).
Nota: As instruções abaixo são para rodar com Docker, mas também é possível configurar o ambiente localmente.

Estrutura do Projeto
O projeto possui a seguinte estrutura de arquivos:

plaintext
Copiar código
|-- app.py                    # Código principal da aplicação Flask
|-- Dockerfile                # Configura o container do serviço Flask
|-- docker-compose.yml        # Orquestra o app Flask e o container MySQL
|-- templates/
|   |-- base.html             # Estrutura base dos templates HTML
|   |-- add.html              # Template para adicionar um novo produto
|   |-- edit.html             # Template para editar um produto existente
|   |-- homepage.html         # Página principal, exibe todos os produtos
|   |-- about.html            # Página 'Sobre'
|   |-- users.html            # Exibe informações de usuários
|-- README.md                 # Documentação do projeto


Configuração e Execução
Para configurar e executar o projeto, siga os passos abaixo.

1. Clone o Repositório 
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Configure as Variáveis de Ambiente
No arquivo docker-compose.yml, verifique a variável SQLALCHEMY_DATABASE_URI. Esta URI será usada para a conexão com o banco de dados MySQL.
Você pode configurar uma senha segura e ajustar os detalhes, conforme necessário.

3. Inicie os Containers
Utilize o Docker Compose para iniciar os containers do banco de dados e da aplicação:

docker-compose up --build

Esse comando vai:
Construir a imagem do Flask com base no Dockerfile.
Iniciar o serviço do MySQL e o serviço Flask.
Disponibilizar a aplicação em http://localhost.

4. Acesse a Aplicação
Depois que os containers estiverem em execução, a aplicação estará disponível em http://localhost. Use um navegador para acessar.

5. Parar os Containers
Para encerrar a execução da aplicação, use o seguinte comando:
docker-compose down

Rotas da Aplicação

GET /: Página inicial, exibe todos os registros de Person.
GET /about: Página "Sobre".
GET /add: Formulário para adicionar um novo registro de Person.
POST /add: Salva um novo registro de Person no banco de dados.
GET /edit/<id>: Formulário para editar um registro existente de Person.
POST /edit/<id>: Atualiza o registro com o id fornecido.
GET /delete/<id>: Exclui o registro de Person com o id fornecido.
GET /persons: Retorna todos os registros em formato JSON.
GET /persons/<id>: Retorna o registro específico em formato JSON.
GET /persons/<user_nome>: Exibe uma página personalizada com o nome do usuário.

Documentação das Funções
Função generate_response: Cria uma resposta JSON customizada.
Classe Person: Representa a tabela Person no banco de dados, contendo id, nome e preco.

Recursos e Dependências
Dependências incluídas:

Flask: Framework principal para a criação de rotas e views.
Flask-SQLAlchemy: ORM para conectar e gerenciar o banco de dados MySQL.
MySQL Connector: Biblioteca para conectar o Flask ao banco de dados MySQL.
