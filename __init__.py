from flask import Flask
from .models import Database
from .routes import init_routes


def create_app():
  app = Flask(__name__)

  # Configurações do banco de dados
  db_config = {
      'user': 'root',
      'password': '',
      'host': 'localhost',
      'database': 'DBAUTOCAR',
  }
  db = Database(db_config)

  # Inicializa as rotas
  init_routes(app, db)

  return app
