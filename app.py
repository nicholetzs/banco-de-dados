from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'user': 'root',
    'password': 'cafe123456',
    'host': 'localhost',
    'database': 'DBAUTOCAR',
}

# Função para obter conexão
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Rota para listar carros
@app.route('/index')
def list_carros():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM CARROS')
    carros = cursor.fetchall()

    # Adicionando clientes
    cursor.execute('SELECT * FROM CLIENTES')
    clientes = cursor.fetchall()

    cursor.close()
    connection.close()

    # Passe a lista de carros para o template
    return render_template('index.html', carros=carros, clientes=clientes) 

# Rota para adicionar um carro
@app.route('/add_carro', methods=['POST'])
def add_carro():
    # Agora o ID será gerado automaticamente
    modelo = request.form['modelo']
    ano = request.form['ano']
    marca = request.form['marca']
    disponibilidade = request.form.get('disponibilidade', 'off') == 'on'  # Checa se o checkbox está marcado

    connection = get_db_connection()
    cursor = connection.cursor()

    # Inserção sem o ID, já que será gerado automaticamente
    cursor.execute(
        'INSERT INTO CARROS (MODELO, ANO, MARCA, DISPONIBILIDADE) VALUES (%s, %s, %s, %s)',
        (modelo, ano, marca, disponibilidade)
    )
    connection.commit()  # Confirma a transação
    cursor.close()  # Fecha o cursor
    connection.close()  # Fecha a conexão

    return redirect(url_for('list_carros'))  # Redireciona para a lista de carros

@app.route('/delete_carro/<int:carro_id>', methods=['POST'])
def delete_carro(carro_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM CARROS WHERE ID = %s', (carro_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('list_carros'))

@app.route('/edit_carro/<int:carro_id>', methods=['GET', 'POST'])
def edit_carro(carro_id):
    if request.method == 'POST':
        modelo = request.form['modelo']
        ano = request.form['ano']
        marca = request.form['marca']
        disponibilidade = request.form.get('disponibilidade', 'off') == 'on'  # Obtém o status do checkbox

        connection = get_db_connection()
        cursor = connection.cursor()

        # Atualiza os dados do carro no banco de dados
        cursor.execute(
            'UPDATE CARROS SET MODELO = %s, ANO = %s, MARCA = %s, DISPONIBILIDADE = %s WHERE ID = %s',
            (modelo, ano, marca, disponibilidade, carro_id)
        )
        connection.commit()  # Confirma a transação
        cursor.close()
        connection.close()

        return redirect(url_for('list_carros'))  # Redireciona para a lista de carros

    # Método GET: busca os detalhes do carro
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM CARROS WHERE ID = %s', (carro_id,))
    carro = cursor.fetchone()
    cursor.close()
    connection.close()
    
    return render_template('edit.html', carro=carro)
    
@app.route('/alugar_carro/<string:carro_id>', methods=['GET', 'POST'])
def alugar_carro(carro_id):
    # Verifica o método da requisição
    if request.method == 'POST':
        print(f"Carro ID recebido: {carro_id}")  # Verifica se o ID está correto
        
        # Captura os dados do formulário enviado
        cliente_id = request.form.get('id_cliente')  # Obtém o ID do cliente selecionado
        data_locacao = request.form.get('data_locacao')  # Data de locação do form
        data_retorno = request.form.get('data_retorno')  # Data de retorno do form
        valor_diaria = request.form.get('valor_diaria')  # Valor da diária do form

        # Conecta ao banco de dados
        connection = get_db_connection()
        cursor = connection.cursor()

        try:
            # Verifica se o carro está disponível
            cursor.execute("SELECT DISPONIBILIDADE FROM CARROS WHERE ID = %s", (carro_id,))
            disponibilidade = cursor.fetchone()[0]

            if not disponibilidade:  # Se o carro não estiver disponível
                return "O carro já está alugado ou indisponível."

            # Insere a locação na tabela LOCACAO
            cursor.execute(""" 
                INSERT INTO LOCACAO (ID_CARRO, ID_CLIENTE, DATA_LOCACAO, DATA_RETORNO, VALOR_DIARIA) 
                VALUES (%s, %s, %s, %s, %s) 
            """, (carro_id, cliente_id, data_locacao, data_retorno, valor_diaria))
            connection.commit()

            # Atualiza a disponibilidade do carro para FALSE (Indisponível)
            cursor.execute(""" 
                UPDATE CARROS SET DISPONIBILIDADE = FALSE WHERE ID = %s 
            """, (carro_id,))
            connection.commit()

            return redirect(url_for('list_carros'))  # Redireciona para a lista de carros

        except Exception as e:
            connection.rollback()  # Desfaz qualquer alteração em caso de erro
            return f"Ocorreu um erro: {str(e)}"
        
        finally:
            cursor.close()
            connection.close()
    
    elif request.method == 'GET':
        print(f"Requisição GET para o carro ID: {carro_id}")
        # Aqui você pode retornar um template ou outra lógica se precisar tratar a requisição GET
        return "Acesso à página de aluguel de carro. Preencha o formulário abaixo."  # Exemplo de resposta para GET
    
@app.route('/rent_car/<int:carro_id>', methods=['GET'])
def rent_car(carro_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    #Obter os dados do carro
    cursor.execute('SELECT * FROM CARROS WHERE ID = %s', (carro_id,))
    carros = cursor.fetchall()

    # Obtenha os clientes
    cursor.execute('SELECT * FROM CLIENTES')
    clientes = cursor.fetchall()

    cursor.close()
    connection.close()

    # Passe o `carro_id` para o template
    return render_template('index.html',carros=carros, carro_id=carro_id, clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)
