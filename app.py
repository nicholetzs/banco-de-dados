from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'user': 'root',
    'password': 'cafe123456',
    'host': 'localhost',
    'database': 'DBAUTOCAR',
}

# Função para obter a conexão
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Rota para listar carros
@app.route('/')
def index():
    return render_template('index.html')  # Você pode redirecionar para a rota de listagem de carros, se preferir

def list_carros():
    connection = get_db_connection()  # Obtém a conexão
    cursor = connection.cursor(dictionary=True)  # Cria um cursor
    cursor.execute('SELECT * FROM CARROS')  # Executa a consulta SQL
    carros = cursor.fetchall()  # Recupera todos os registros
    cursor.close()  # Fecha o cursor
    connection.close()  # Fecha a conexão
    
    return render_template('index.html', carros=carros)  # Renderiza o template

if __name__ == '__main__':
    app.run(debug=True)
