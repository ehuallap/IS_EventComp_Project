from registered_person import Registered_person

# Creacion de la clase Administrator
class Administrator(Registered_person):
    # Constructor de la clase
    def __init__(self, id, name, email, password):
        super().__init__(self, id, name, email, password)
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
