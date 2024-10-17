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
    connection = get_db_connection()  # Obtém a conexão
    cursor = connection.cursor(dictionary=True)  # Cria um cursor
    cursor.execute('SELECT * FROM CARROS')  # Executa a consulta SQL
    carros = cursor.fetchall()  # Recupera todos os registros
    cursor.close()  # Fecha o cursor
    connection.close()  # Fecha a conexão
    
    return render_template('index.html', carros=carros)  # Renderiza o template

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



@app.route('/alugar_carro/<int:carro_id>', methods=['POST'])
def alugar_carro(carro_id):
    # Coleta os dados do cliente do formulário
    nome = request.form['nome']
    numero_cnh = request.form['numero_cnh']
    numero_cartao_credito = request.form['numero_cartao_credito']
    telefone = request.form['telefone']
    email = request.form['email']

    # Conexão ao banco de dados
    connection = get_db_connection()
    cursor = connection.cursor()

    # Inserir cliente na tabela CLIENTES
    insert_cliente_query = """
    INSERT INTO CLIENTES (NOME, NUMERO_CNH, NUMERO_CARTAO_CREDITO, TELEFONE, EMAIL)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_cliente_query, (nome, numero_cnh, numero_cartao_credito, telefone, email))
    connection.commit()

    # Obter o ID do cliente recém-inserido
    cliente_id = cursor.lastrowid

    # Atualizar a disponibilidade do carro na tabela CARROS
    update_carro_query = """
    UPDATE CARROS
    SET DISPONIBILIDADE = %s
    WHERE ID = %s
    """
    cursor.execute(update_carro_query, (False, carro_id))
    connection.commit()

    # Fechar a conexão
    cursor.close()
    connection.close()

    return redirect(url_for('list_carros'))  # Redirecionar para a lista de carros

if __name__ == '__main__':
    app.run(debug=True)
