# Creacion de la clase Participante
class Participant:
    # Constructor de la clase
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    
    # Metodo para representar el objeto en un diccionario
    def __repr__(self):
        return "<Participant('%s','%s','%s','%s')>" % (self.id, self.name, self.email, self.password)
    
    # Metodo para representar el objeto en una tupla
    def __str__(self):
        return "Participant [id=%s, name=%s, email=%s, password=%s]" % (self.id, self.name, self.email, self.password)
    
    # Metodo para verificar participantes repetidos
    def __eq__(self, other):
        return self.id == other.id
    
    # Metodo para obtener el id del participante (ENCAPSULAMIENTO)
    def getId(self):
        return self.id
    
    # Metodo para obtener el nombre del participante (ENCAPSULAMIENTO)
    def getName(self):
        return self.name
    
    # Metodo para obtener el email del participante (ENCAPSULAMIENTO)
    def getEmail(self):
        return self.email
    
    # Metodo para obtener el password del participante (ENCAPSULAMIENTO)
    def getPassword(self):
        return self.password
    
    # Metodo para asignar el id del participante (ENCAPSULAMIENTO)
    def setId(self, id):
        self.id = id
    
    # Metodo para asignar el nombre del participante (ENCAPSULAMIENTO)
    def setName(self, name):
        self.name = name
    
    # Metodo para asignar el email del participante (ENCAPSULAMIENTO)
    def setEmail(self, email):
        self.email = email
    
    # Metodo para asignar el password del participante (ENCAPSULAMIENTO)
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
