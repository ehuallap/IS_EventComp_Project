import sys
from pathlib import Path

file = Path(__file__).resolve()
package_root = file.parents[2]
sys.path.append(str(package_root))

from infrastructure.repository.db_connection import DbConnection
from domain.entities.speaker import Speaker

class Speaker_repository(DbConnection.Model, Speaker):
    __tablename__ = 'speaker'
    ac_level = DbConnection.Column(DbConnection.String(50), nullable=False)
    description = DbConnection.Column(DbConnection.String(100), nullable=False)
    especiality = DbConnection.Column(DbConnection.String(50), nullable=False)
    phone = DbConnection.Column(DbConnection.String(50), nullable=False)
    
    def __init__(self, id, name, email, password, ac_level, description, especiality, phone):
        Speaker.__init__(self, id, name, email, password, ac_level, description, especiality, phone)

    def insert(self):
        DbConnection.session.add(self)
        DbConnection.session.commit()
        
    def update(self):
        DbConnection.session.commit()

    def delete(self):
        DbConnection.session.delete(self)
        DbConnection.session.commit()

    def get(self, id):
        return DbConnection.session.query(Speaker_repository).filter(Speaker_repository.id == id).first()

    def getAll(self):
        return DbConnection.session.query(Speaker_repository).all()