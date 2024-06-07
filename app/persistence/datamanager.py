from flask import jsonify

class DataManager():
    """Defines the subclass DataManager that inherits from IPersistenceManager"""
    def save(self, entity):
        """
        Methdod used to save data(entity) into a JSON file
        """
        return jsonify(entity)

    def get(self, entity_id, entity_type):
        # Logic to retrieve an entity based on ID and type
        pass

    def update(self, entity):
        #Logic to update an entity in storage
        pass

    def delete(self, entity_id, entity_type):
        # Logic to delete an entity from storage
        pass