# README para Rodar o Projeto DBAUTOCAR em Linux

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados:

- **Python** (preferencialmente a versão 3.7 ou superior)
- **pip** (gerenciador de pacotes do Python)
- **VS Code**
- **MySQL** (ou outro banco de dados que você está utilizando)

## Passo a Passo

### 1. Baixando o Projeto

1. Acesse o repositório do projeto no GitHub.
2. Clique no botão **Code** e selecione **Download ZIP**.
3. Após o download, extraia o arquivo ZIP em um diretório de sua escolha.

### 2. Abrindo o Projeto no VS Code

1. Abra o VS Code.
2. No menu, clique em **File** > **Open Folder...**.
3. Selecione a pasta onde você extraiu o projeto.

### 3. Ativando o Ambiente Virtual

1. Abra o terminal do VS Code (você pode abrir o terminal pressionando `` Ctrl + ` ``).
2. Navegue até a pasta do projeto:
   ```bash
   cd /caminho/para/o/projeto
Ative o ambiente virtual:
No Linux:
bash
Copiar código
source venv/bin/activate
No Windows:
bash
Copiar código
.\venv\Scripts\activate
4. Instalando Dependências
Se houver um arquivo requirements.txt no projeto, instale as dependências necessárias com o seguinte comando:

bash
Copiar código
pip install -r requirements.txt
5. Configurando o Banco de Dados
Certifique-se de que o MySQL esteja em execução.
Acesse o MySQL e crie o banco de dados:
sql
Copiar código
CREATE DATABASE DBAUTOCAR;
Execute o script SQL para criar as tabelas conforme descrito no seu código.
6. Rodando o Projeto
Para rodar o projeto, execute o arquivo principal (por exemplo, app.py):

bash
Copiar código
python app.py
7. Acessando a Aplicação
Abra o navegador e acesse a aplicação no endereço especificado (geralmente http://127.0.0.1:5000 ou outro conforme sua configuração).
