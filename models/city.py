from models.base_model import BaseModel

class City(BaseModel):
    """ City class """
    def __init__(self, name, country_id):
        super().__init__()
        self.name = name
        self.country_id = country_id
