# Creacion de la clase Event
class Event:
    # Constructor de la clase
    def __init__(self, id, name, description, date, place, administrator):
        self.id = id
        self.name = name
        self.description = description
        self.date = date
        self.place = place
        self.administrator = administrator
    
    # Metodo para representar el objeto en un diccionario
    def __repr__(self):
        return "<Event('%s','%s','%s','%s','%s','%s')>" % (self.id, self.name, self.description, self.date, self.place, self.administrator)
    
    # Metodo para representar el objeto en una tupla
    def __str__(self):
        return "Event [id=%s, name=%s, description=%s, date=%s, place=%s, administrator=%s]" % (self.id, self.name, self.description, self.date, self.place, self.administrator)
    
    # Metodo para verificar eventos repetidos
    def __eq__(self, other):
        return self.id == other.id
    
    # Metodo para obtener el id del evento (ENCAPSULAMIENTO)
    def getId(self):
        return self.id
    
    # Metodo para obtener el nombre del evento (ENCAPSULAMIENTO)
    def getName(self):
        return self.name
    
    # Metodo para obtener la descripcion del evento (ENCAPSULAMIENTO)
    def getDescription(self):
        return self.description
    
    # Metodo para obtener la fecha del evento (ENCAPSULAMIENTO)
    def getDate(self):
        return self.date
    
    # Metodo para obtener la ubicacion del evento (ENCAPSULAMIENTO)
    def getPlace(self):
        return self.place
    
    # Metodo para obtener el administrador del evento (ENCAPSULAMIENTO)
    def getAdministrator(self):
        return self.administrator
    
    # Metodo para asignar el id del evento (ENCAPSULAMIENTO)
    def setId(self, id):
        self.id = id
    
    # Metodo para asignar el nombre del evento (ENCAPSULAMIENTO)
    def setName(self, name):
        self.name = name
    
    # Metodo para asignar la descripcion del evento (ENCAPSULAMIENTO)
    def setDescription(self, description):
        self.description = description
    
    # Metodo para asignar la fecha del evento (ENCAPSULAMIENTO)
    def setDate(self, date):
        self.date = date
    
    # Metodo para asignar la ubicacion del evento (ENCAPSULAMIENTO)
    def setPlace(self, place):
        self.place = place
        
    # Metodo para asignar el administrador del evento (ENCAPSULAMIENTO)
    def setAdministrator(self, administrator):
        self.administrator = administrator
    
    # Metodo para obtener el objeto en formato JSON
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date': self.date,
            'place': self.place,
            'administrator': self.administrator
        }