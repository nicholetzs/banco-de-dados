from flask import Flask
from models import Database
import routes  # Importe as rotas diretamente

# Configurações do banco de dados
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'DBAUTOCAR',
}

# Instância do banco de dados e inicialização do app
db = Database(db_config)


def create_app(db):
  app = Flask(__name__)
  app.config['db'] = db  # Armazena a instância do banco no config do app

  # Registra as rotas
  routes.init_app(app, db)

  return app


# Executa o app
app = create_app(db)

if __name__ == '__main__':
  app.run(debug=True)
