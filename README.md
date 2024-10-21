###ainda vou mexer

README para Rodar o Projeto DBAUTOCAR em Linux
Pré-requisitos
Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados:

Python (preferencialmente a versão 3.7 ou superior)
pip (gerenciador de pacotes do Python)
VS Code
MySQL (ou outro banco de dados que você está utilizando)
Passo a Passo

1. Baixando o Projeto
   Acesse o repositório do projeto no GitHub.
   Clique no botão Code e selecione Download ZIP.
   Após o download, extraia o arquivo ZIP em um diretório de sua escolha.
2. Abrindo o Projeto no VS Code
   Abra o VS Code.
   No menu, clique em File > Open Folder....
   Selecione a pasta onde você extraiu o projeto.
3. Ativando o Ambiente Virtual
   Abra o terminal do VS Code (você pode abrir o terminal pressionando Ctrl + `).

Navegue até a pasta do projeto:

bash
Copiar código
cd /caminho/para/o/projeto
Ative o ambiente virtual:

No Linux:
source venv/bin/activate

5. Configurando o Banco de Dados
   Certifique-se de que o MySQL esteja em execução. Acesse o MySQL e crie o banco de dados:
   CREATE DATABASE DBAUTOCAR;
   Execute o script SQL para criar as tabelas conforme descrito no seu código.

6. Rodando o Projeto
   Para rodar o projeto, execute o arquivo principal (por exemplo, app.py):
   python app.py

7. Acessando a Aplicação
   Abra o navegador e acesse a aplicação no endereço especificado (geralmente http://127.0.0.1:5000 ou outro conforme sua configuração).

Configurando um Servidor e Conectando ao Banco de Dados MySQL no MySQL Workbench

1. Criar uma Nova Conexão no MySQL Workbench
   Abra o MySQL Workbench.

No painel inicial, clique no ícone + ao lado de MySQL Connections.

Na janela que aparecer, preencha as informações da sua conexão:

Connection Name: Dê um nome à sua conexão (por exemplo, "DBAUTOCAR").
Connection Method: Escolha Standard (TCP/IP).
Hostname: Normalmente é localhost se o MySQL estiver rodando localmente. Se for um servidor remoto, insira o endereço IP ou hostname do servidor.
Port: O padrão é 3306, mas ajuste se o seu MySQL estiver rodando em outra porta.
Username: Insira o nome de usuário do MySQL (por exemplo, root ou outro usuário criado).
Password: Clique em Store in Vault... para armazenar sua senha, ou você será solicitado a inseri-la toda vez que se conectar.
Clique em Test Connection para garantir que tudo está configurado corretamente. Se a conexão for bem-sucedida, clique em OK.

2. Criar o Banco de Dados e Tabelas
   Após conectar-se ao MySQL no Workbench:

No painel esquerdo (Navigator), clique com o botão direito no campo Schemas e selecione Create Schema.
Nomeie o banco de dados como DBAUTOCAR e clique em Apply.
Agora, você pode rodar o script SQL para criar suas tabelas. No editor de consultas, copie e cole o código SQL.
