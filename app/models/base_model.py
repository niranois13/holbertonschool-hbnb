import uuid
import datetime

class BaseModel:
    """ Base class for all models """
    def __init__(self):
        """ Constructor for BaseModel """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """ Updates the updated_at attribute """
        self.updated_at = datetime.datetime.now()

    def update(self, key, value):
        """ Updates an attribute """
        setattr(self, key, value)
        self.updated_at = datetime.datetime.now()
