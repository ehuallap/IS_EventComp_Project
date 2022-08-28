# Creacion de la clase Speaker
class Speaker:
    # Constructor de la clase
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    
    # Metodo para representar el objeto en un diccionario
    def __repr__(self):
        return "<Speaker('%s','%s','%s','%s')>" % (self.id, self.name, self.email, self.password)
    
    # Metodo para representar el objeto en una tupla
    def __str__(self):
        return "Speaker [id=%s, name=%s, email=%s, password=%s]" % (self.id, self.name, self.email, self.password)
    
    # Metodo para verificar speakers repetidos
    def __eq__(self, other):
        return self.id == other.id
    
    # Metodo para obtener el id del speaker (ENCAPSULAMIENTO)
    def getId(self):
        return self.id
    
    # Metodo para obtener el nombre del speaker (ENCAPSULAMIENTO)
    def getName(self):
        return self.name
    
    # Metodo para obtener el email del speaker (ENCAPSULAMIENTO)
    def getEmail(self):
        return self.email
    
    # Metodo para obtener el password del speaker (ENCAPSULAMIENTO)
    def getPassword(self):
        return self.password
    
    # Metodo para asignar el id del speaker (ENCAPSULAMIENTO)
    def setId(self, id):
        self.id = id
    
    # Metodo para asignar el nombre del speaker (ENCAPSULAMIENTO)
    def setName(self, name):
        self.name = name
    
    # Metodo para asignar el email del speaker (ENCAPSULAMIENTO)
    def setEmail(self, email):
        self.email = email
    
    # Metodo para asignar el password del speaker (ENCAPSULAMIENTO)
    def setPassword(self, password):
        self.password = password
    
    # Metodo para obtener el objeto en formato JSON
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
