from models.base_model import BaseModel

class User(BaseModel):
    """ User class """
    def __init__(self, email, first_name, last_name):
        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
