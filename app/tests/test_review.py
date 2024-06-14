import unittest
from flask import Flask
from flask.testing import FlaskClient
from api.review_api import review_api
from models.review import Review
from persistence.datamanager import DataManager
from unittest.mock import patch, MagicMock
import json

class ReviewApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(review_api)
        self.app.testing = True
        self.client = self.app.test_client()
        self.client: FlaskClient

    @patch('api.review_api.DataManager')
    def test_add_review_success(self, MockDataManager):
        mock_datamanager = MockDataManager.return_value
        mock_datamanager.save.return_value = None

        response = self.client.post('/places/1/reviews', json={
            "user_id": "1",
            "rating": 5,
            "comment": "Great place!"
        })

        self.assertEqual(response.status_code, 201)
        self.assertIn('Review added', response.get_json()['Success'])

    @patch('api.review_api.DataManager')
    def test_add_review_invalid_data(self, MockDataManager):
        response = self.client.post('/places/1/reviews', json={})

        self.assertEqual(response.status_code, 400)
        self.assertIn('Problem during review creation', response.get_json()['Error'])