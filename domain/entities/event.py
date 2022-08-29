# Creacion de la clase Event
class Event:
    def __init__(self):
        self.id = None
        self.title = None
        self.theme = None
        self.description = None
        self.date_time = None
        self.platform = None
        self.access_link = None
        self.id_administrator = None
    
    # Constructor de la clase
    def __init__(self, id, title, theme, description, date_time, platform, access_link, id_administrator):
        self.id = id
        self.title = title
        self.theme = theme
        self.description = description
        self.date_time = date_time
        self.platform = platform
        self.access_link = access_link
        self.id_administrator = id_administrator
    
    def getId(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def getTheme(self):
        return self.theme
    
    def getDescription(self):
        return self.description
    
    def getDateTime(self):
        return self.date_time
    
    def getPlatform(self):
        return self.platform
    
    def getAccessLink(self):
        return self.access_link
    
    def getIdAdministrator(self):
        return self.id_administrator
    
    def setId(self, id):
        self.id = id
    
    def setTitle(self, title):
        self.title = title
    
    def setTheme(self, theme):
        self.theme = theme
    
    def setDescription(self, description):
        self.description = description
    
    def setDateTime(self, date_time):
        self.date_time = date_time
    
    def setPlatform(self, platform):
        self.platform = platform
    
    def setAccessLink(self, access_link):
        self.access_link = access_link
    
    def setIdAdministrator(self, id_administrator):
        self.id_administrator = id_administrator
    
    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'theme': self.theme,
            'description': self.description,
            'date_time': self.date_time,
            'platform': self.platform,
            'access_link': self.access_link,
            'id_administrator': self.id_administrator
        }