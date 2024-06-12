from flask import Blueprint, jsonify, request
from models.city import City
from persistence.datamanager import DataManager
import json
import pycountry
datamanager = DataManager(flag=5)
cities_api = Blueprint("cities_api", __name__)

@cities_api.route("/cities", methods=["POST", 'GET'])
def cities():
    """
    Function used to create a new city, send it to the database datamanager
    """
    if request.method == "POST":
        city_data = request.get_json()
        city_id = city_data.get('id')
        new_city = city_data.get('name')
        citiees = City(city_id, new_city)
        if not city_id or not new_city:
            return jsonify({"Error": "Invalid data"}), 400

        with open('cities.json', 'r+', encoding='utf-8') as f:
            data = json.load(f)
            for entry in data:
                if entry.get('id') == city_id:
                    if new_city in entry['city']:
                        return jsonify({"Error": "City already exists"}), 400
                    entry['city'].append(new_city)
                    f.seek(0)
                    json.dump(data, f, ensure_ascii=False, indent=4)
                    f.truncate()
                    return jsonify({"Success": "City added"}), 201
            return jsonify({"Error": "Country ID not found"}), 404