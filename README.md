# EVENTCOMP
CAMBIAR CONTRASEÑA DE LA BASE DE DATOS EN EL ARCHIVO db_connecion.py
COMANDO PARA CREAR ENTORNO VIRTUAL: python -m venv project_env
COMANDO PARA ACTIVAR EL ENTORNO VIRTUAL: .\project_env\Scripts\activate
PARA INSTALAR LOS REQUISITOS: pip install -r requirements.txt
PARA LEVANTAR EL SERVIDOR: python app.py

# practicas de programacion
* Indentacion consistente
* Comentarios
* Variables
* Tipos de datos
* Operadores

```python
class Registered_repository(DbConnection.Model, Registered_person):
    __tablename__ = 'registred_person'
    id = DbConnection.Column(DbConnection.Integer, primary_key=True)
    name = DbConnection.Column(DbConnection.String(50), nullable=False)
    email = DbConnection.Column(DbConnection.String(50), nullable=False)
    password = DbConnection.Column(DbConnection.String(50), nullable=False)
```
Aporte de cada integrante:
* Juan Pablo: aajsdnasd 
