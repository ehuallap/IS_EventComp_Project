import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root = file.parents[2]
sys.path.append(str(package_root))

from infrastructure.repository.db_connection import DbConnection
from domain.entities.administrator import Administrator

class Administrator_repository(DbConnection.Model, Administrator):
    __tablename__ = 'administrator'
    id = DbConnection.Column(DbConnection.Integer, primary_key=True)
    
    def __init__(self, id, name, email, password):
        Administrator.__init__(self, id, name, email, password)

    def insert(self):
        try:
            DbConnection.session.add(self)
            DbConnection.session.commit()
        except Exception as e:
            print(e)
            DbConnection.session.rollback()
            return False
        return True
        
    def update(self):
        try:
            DbConnection.session.commit()
        except Exception as e:
            print(e)
            DbConnection.session.rollback()
            return False
        return True

    def delete(self):
        try:
            DbConnection.session.delete(self)
            DbConnection.session.commit()
        except Exception as e:
            print(e)
            DbConnection.session.rollback()
            return False
        return True

    def get(self, id):
        try:
            return DbConnection.session.query(Administrator_repository).filter(Administrator_repository.id == id).first()
        except Exception as e:
            print(e)
            return None

    def getAll(self):
        try:
            return DbConnection.session.query(Administrator_repository).all()
        except Exception as e:
            print(e)
            return None
