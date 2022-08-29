from registered_person import Registered_person

# Creacion de la clase Participante
class Participant(Registered_person):
    # Constructor de la clase
    def __init__(self, id, name, email, password, universidad, ciclo):
        super().__init__(self, id, name, email, password)
        self.universidad = universidad
        self.ciclo = ciclo
    
    def getUniversidad(self):
        return self.universidad
    
    def getCiclo(self):
        return self.ciclo
    
    def setUniversidad(self, universidad):
        self.universidad = universidad
    
    def setCiclo(self, ciclo):
        self.ciclo = ciclo
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'universidad': self.universidad,
            'ciclo': self.ciclo
        }
    