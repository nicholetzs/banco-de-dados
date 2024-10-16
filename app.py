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

if __name__ == '__main__':
    app.run(debug=True)
