from flask_sqlalchemy import SQLAlchemy
import pymysql

database_name = 'event_manager'
password = '678670'
database_path = 'mysql+pymysql://root:{}@localhost:3306/{}'.format(password, database_name)

DbConnection = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DbConnection.app = app
    DbConnection.init_app(app)
    DbConnection.create_all()
