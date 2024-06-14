import unittest
from flask import Flask
from flask.testing import FlaskClient
from api.cities_api import cities_api
from models.city import City
from persistence.datamanager import DataManager
from unittest.mock import patch, MagicMock
import json

class CitiesApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(cities_api)
        self.app.testing = True
        self.client = self.app.test_client()
        self.client: FlaskClient

    @patch('api.cities_api.DataManager')
    def test_add_city_success(self, MockDataManager):
        mock_datamanager = MockDataManager.return_value
        mock_datamanager.save.return_value = None

        response = self.client.post('/cities', json={
            "id": "1",
            "name": "New York"
        })

        self.assertEqual(response.status_code, 201)
        self.assertIn('City added', response.get_json()['Success'])

    @patch('api.cities_api.DataManager')
    def test_add_city_invalid_data(self, MockDataManager):
        response = self.client.post('/cities', json={})

        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid data', response.get_json()['Error'])

    @patch('api.cities_api.DataManager')
    def test_get_cities(self, MockDataManager):
        response = self.client.get('/cities')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [{"name": "New York"}])

    @patch('api.cities_api.DataManager')
    def test_get_city_by_id(self, MockDataManager):
        mock_datamanager = MockDataManager.return_value
        mock_datamanager.get.return_value = {"name": "New York"}

        response = self.client.get('/cities/1')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"name": "New York"})

    @patch('api.cities_api.DataManager')
    def test_get_city_by_id_not_found(self, MockDataManager):
        mock_datamanager = MockDataManager.return_value
        mock_datamanager.get.return_value = None

        response = self.client.get('/cities/1')

        self.assertEqual(response.status_code, 404)
        self.assertIn('City not found', response.get_json()['Error'])

    @patch('api.cities_api.DataManager')
    def test_update_city(self, MockDataManager):
        mock_datamanager = MockDataManager.return_value
        mock_datamanager.get.return_value = {"name": "New York"}

        response = self.client.put('/cities/1', json={
            "name": "Updated City"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn('City updated', response.get_json()['Success'])

    @patch('api.cities_api.DataManager')
    def test_update_city_not_found(self, MockDataManager):
        mock_datamanager = MockDataManager.return_value
        mock_datamanager.get.return_value = None

        response = self.client.put('/cities/1', json={
            "name": "Updated City"
        })

        self.assertEqual(response.status_code, 404)
        self.assertIn('City not found', response.get_json()['Error'])

    @patch('api.cities_api.DataManager')
    def test_delete_city(self, MockDataManager):
        mock_datamanager = MockDataManager.return_value
        mock_datamanager.get.return_value = {"name": "New York"}

        response = self.client.delete('/cities/1')

        self.assertEqual(response.status_code, 200)
        self.assertIn('City deleted', response.get_json()['Success'])

    @patch('api.cities_api.DataManager')
    def test_delete_city_not_found(self, MockDataManager):
        mock_datamanager = MockDataManager.return_value
        mock_datamanager.get.return_value = None

        response = self.client.delete('/cities/1')

        self.assertEqual(response.status_code, 404)
        self.assertIn('City not found', response.get_json()['Error'])


if __name__ == '__main__':
    unittest.main()
