##README para Rodar o Projeto DBAUTOCAR em Linux, no DBeavor

1. Baixando o Projeto
   Acesse o repositório do projeto no GitHub.
   Clique no botão Code e selecione Download ZIP.
   Após o download, extraia o arquivo ZIP em um diretório de sua escolha.
2. Abrindo o Projeto no VS Code
   Abra o VS Code.
   No menu, clique em File > Open Folder....
   Selecione a pasta onde você extraiu o projeto.

Agora, certifique-se de ter os seguintes pré-requisitos instalados dentro do ambiente virtual no VS Code:

Crie o ambiente virtual: python -m venv ./venv
Ative o ambiente virtual no Linux: source venv/bin/activate
Python (preferencialmente a versão 3.7 ou superior)
pip (gerenciador de pacotes do Python)
MySQL (pip install mysql-connector-python)
Flask (pip install flask)
Depois, aperte CTRL + SHIFT + P e selecione o interpretador do ambiente virtual e de um realod no VS Code
Por fim, no terminal, digite: python app.py e passe a rota /index no local


3. Configurando o Banco de Dados no DBeavor
Conecte-se ao labdatabase, substituindo o nome do banco de dados por DBAUTOCAR e seus respectivos campos conforme no arquivo app.py, depois teste a conexão e rode os scripts para criar as tabelas e fazer os inserts de carros e clientes.


