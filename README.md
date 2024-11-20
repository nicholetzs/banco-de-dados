README para Rodar o Projeto DBAUTOCAR em Linux, no DBeaver

Copyright: Desenvolvido por Nichole Nicolini, Lucas Ferrari, Marlon Lacerda, Gustavo Trevezani e Fabricio Dias.

1. Baixando o Projeto

	1.	Acesse o repositório do projeto no GitHub.
	2.	Clique no botão Code e selecione Download ZIP.
	3.	Após o download, extraia o arquivo ZIP em um diretório de sua escolha.

2. Abrindo o Projeto no VS Code

	1.	Abra o VS Code.
	2.	No menu, clique em File > Open Folder….
	3.	Selecione a pasta onde você extraiu o projeto.

Agora, certifique-se de ter os seguintes pré-requisitos instalados dentro do ambiente virtual no VS Code:

	•	Crie o ambiente virtual:

python -m venv ./venv


	•	Ative o ambiente virtual no Linux:

source venv/bin/activate


	•	Instale as dependências necessárias:
	•	Python (preferencialmente a versão 3.7 ou superior)
	•	pip (gerenciador de pacotes do Python)
	•	MySQL:

pip install mysql-connector-python


	•	Flask:

pip install flask



	4.	Aperte CTRL + SHIFT + P, selecione o interpretador do ambiente virtual e dê um reload no VS Code.
	5.	No terminal, execute o projeto:

python app.py


	

3. Configurando o Banco de Dados no DBeaver

	1.	Conecte-se ao banco de dados labdatabase.
	2.	Substitua o nome do banco de dados por DBAUTOCAR e ajuste os respectivos campos conforme o arquivo app.py.
	3.	Teste a conexão no DBeaver.
	4.	Rode os scripts para criar as tabelas e inserir os dados de carros e clientes.

Este documento deve ajudá-lo a configurar o projeto DBAUTOCAR corretamente no Linux usando o DBeaver e o VS Code.
