from flask import Blueprint, jsonify, request
from models.country import Country
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
        with open('cities.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for city in data:
                if city == city_data.get('id'):
                    new_city = city_data.get('name')
                    print(new_city)
                    return jsonify({"Success": "City added"}, new_city.to_dict()), 201