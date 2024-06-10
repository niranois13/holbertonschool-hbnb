import uuid
import datetime
import json

class BaseModel:
    """ Base class for all models """
    def __init__(self):
        """ Constructor for BaseModel """
        self.user_id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def save(self):
        """ Updates the updated_at attribute """
        self.updated_at = datetime.datetime.now()

    def update(self, key, value):
        """ Updates an attribute """
        setattr(self, key, value)
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime.datetime):
                result[key] = value.isoformat()
            else:
                result[key] = value
        return result