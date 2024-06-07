import json

class DataManager():
    """Defines the subclass DataManager that inherits from IPersistenceManager"""
    def save(self, entity, flag):
        """
        Methdod used to save data(entity) into a JSON file
        """
        if flag == 1:
            file_path = "User.json"
        
        data = []
        try:
            with open(file_path, 'r', encoding='UTF-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            pass
        data.append(entity)

        with open(file_path, 'w', encoding='UTF-8') as f:
            json.dump(data,f, indent=4)        
    def get(self, entity,id, flag):
        """
        Method used to get data(entity) from a JSON file
        """
        """ data = []
        if flag ==1:
            file_path = "User.json"
        try:
            with open(file_path, 'r', encoding='UTF-8') as f:
                data = json.load(f)
            if id
        except FileNotFoundError:
            pass
        return data"""
