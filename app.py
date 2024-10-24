
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

class Database:
    def __init__(self, config):
        self.config = config

    def get_connection(self):
        return mysql.connector.connect(**self.config)


class CarroApp:
    def __init__(self, db):
        self.db = db
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/index')
        def list_carros():
            connection = self.db.get_connection()
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

        @self.app.route('/add_carro', methods=['POST'])
        def add_carro():
            modelo = request.form['modelo']
            ano = request.form['ano']
            marca = request.form['marca']
            disponibilidade = request.form.get('disponibilidade', 'off') == 'on'

            connection = self.db.get_connection()
            cursor = connection.cursor()

            cursor.execute(
                'INSERT INTO CARROS (MODELO, ANO, MARCA, DISPONIBILIDADE) VALUES (%s, %s, %s, %s)',
                (modelo, ano, marca, disponibilidade)
            )
            connection.commit()
            cursor.close()
            connection.close()

            return redirect(url_for('list_carros'))

        @self.app.route('/delete_carro/<int:carro_id>', methods=['POST'])
        def delete_carro(carro_id):
            connection = self.db.get_connection()
            cursor = connection.cursor()
            cursor.execute('DELETE FROM CARROS WHERE ID = %s', (carro_id,))
            connection.commit()
            cursor.close()
            connection.close()
            return redirect(url_for('list_carros'))

        @self.app.route('/edit_carro/<int:carro_id>', methods=['GET', 'POST'])
        def edit_carro(carro_id):
            if request.method == 'POST':
                modelo = request.form['modelo']
                ano = request.form['ano']
                marca = request.form['marca']
                disponibilidade = request.form.get('disponibilidade', 'off') == 'on'

                connection = self.db.get_connection()
                cursor = connection.cursor()

                cursor.execute(
                    'UPDATE CARROS SET MODELO = %s, ANO = %s, MARCA = %s, DISPONIBILIDADE = %s WHERE ID = %s',
                    (modelo, ano, marca, disponibilidade, carro_id)
                )
                connection.commit()
                cursor.close()
                connection.close()

                return redirect(url_for('list_carros'))

            connection = self.db.get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM CARROS WHERE ID = %s', (carro_id,))
            carro = cursor.fetchone()
            cursor.close()
            connection.close()

            return render_template('edit.html', carro=carro)

        @self.app.route('/alugar_carro/<int:carro_id>', methods=['POST'])
        def alugar_carro(carro_id):
            connection = self.db.get_connection()
            cursor = connection.cursor(dictionary=True)

            cliente_id = request.form.get('id_cliente')
            data_locacao = request.form.get('data_locacao')
            data_retorno = request.form.get('data_retorno')
            valor_diaria = request.form.get('valor_diaria')

            try:
                cursor.execute("SELECT DISPONIBILIDADE FROM CARROS WHERE ID = %s", (carro_id,))
                disponibilidade = cursor.fetchone()

                if not disponibilidade:
                    return "O carro não foi encontrado."

                disponibilidade = disponibilidade['DISPONIBILIDADE']

                if not disponibilidade:
                    return "O carro já está alugado ou indisponível."

                cursor.execute(""" 
                    INSERT INTO LOCACAO (ID_CARRO, ID_CLIENTE, DATA_LOCACAO, DATA_RETORNO, VALOR_DIARIA) 
                    VALUES (%s, %s, %s, %s, %s) 
                """, (carro_id, cliente_id, data_locacao, data_retorno, valor_diaria))
                connection.commit()

                cursor.execute(""" 
                    UPDATE CARROS SET DISPONIBILIDADE = FALSE WHERE ID = %s 
                """, (carro_id,))
                connection.commit()

                return redirect(url_for('list_carros'))

            except Exception as e:
                connection.rollback()
                return f"Ocorreu um erro: {str(e)}"

            finally:
                cursor.close()
                connection.close()

        @self.app.route('/devolver_carro/<int:carro_id>', methods=['POST'])
        def devolver_carro(carro_id):
            disponibilidade = request.form.get('disponibilidade') == 'on'

            connection = self.db.get_connection()
            cursor = connection.cursor()

            try:
                # Se o carro for marcado como disponível, remover o cliente associado e devolver o carro
                if disponibilidade:
                    cursor.execute("""
                        UPDATE CARROS 
                        SET DISPONIBILIDADE = TRUE, CLIENTE_ID = NULL
                        WHERE ID = %s
                    """, (carro_id,))
                    connection.commit()
                else:
                    cursor.execute("""
                        UPDATE CARROS 
                        SET DISPONIBILIDADE = FALSE
                        WHERE ID = %s
                    """, (carro_id,))
                    connection.commit()

                return redirect(url_for('list_carros'))

            except Exception as e:
                connection.rollback()
                return f"Ocorreu um erro ao devolver o carro: {str(e)}"

            finally:
                cursor.close()
                connection.close()

    def run(self, debug=True):
        self.app.run(debug=debug)


# Configurações do banco de dados
db_config = {
    'user': 'root',
    'password': 'cafe123456',
    'host': 'localhost',
    'database': 'DBAUTOCAR',
}

db = Database(db_config)
carro_app = CarroApp(db)

if __name__ == '__main__':
    carro_app.run()