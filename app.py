from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configurando a conexão com o MySQL
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="Nichole",
        password="cafe123456",
        database="nome_do_banco"
    )
    return conn

# Rota principal (homepage)
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Consulta ao banco de dados
    cursor.execute("SELECT * FROM USERS")  # Alterar conforme sua tabela
    users = cursor.fetchall()
    
    cursor.close()
    conn.close()

    # Renderiza o template e passa os dados do banco
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
