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
        DbConnection.session.add(self)
        DbConnection.session.commit()
        
    def update(self):
        DbConnection.session.commit()

    def delete(self):
        DbConnection.session.delete(self)
        DbConnection.session.commit()

    def get(self, id):
        return DbConnection.session.query(Administrator_repository).filter(Administrator_repository.id == id).first()

    def getAll(self):
        return DbConnection.session.query(Administrator_repository).all()