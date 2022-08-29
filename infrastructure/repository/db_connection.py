# importancias de Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import pymysql

# Se crea el nombre de la base de datos
database_name = 'event_manager'

# Se crea la contraseña de la base de datos
password = '678670'

# Se crea el path de la base de datos
database_path = 'mysql+pymysql://root:{}@localhost:3306/{}'.format(password, database_name)

# Se crea la clase DbConnection, que hereda de la clase SQLAlchemy
DbConnection = SQLAlchemy()

# Funcion para conectar a la base de datos
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DbConnection.app = app
    DbConnection.init_app(app)
    DbConnection.create_all()
