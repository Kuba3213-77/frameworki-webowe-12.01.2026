from flask import Flask, jsonify
import unittest
import json

class UserManagementIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/users', 
                                     data=json.dumps({"name": "Wojciech", "lastname": "Oczkowski"}), 
                                     content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        self.client.post('/users', 
                         data=json.dumps({"name": "Wojciech", "lastname": "Oczkowski"}), 
                         content_type='application/json')
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Wojciech", str(response.data))

    def test_get_user(self):
        self.client.post('/users', 
                         data=json.dumps({"name": "Wojciech", "lastname": "Oczkowski"}), 
                         content_type='application/json')
        response = self.client.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Oczkowski", str(response.data))

    def test_patch_user(self):
        self.client.post('/users', 
                         data=json.dumps({"name": "Wojciech", "lastname": "Oczkowski"}), 
                         content_type='application/json')
        response = self.client.patch('/users/1', 
                                      data=json.dumps({"name": "Jan"}), 
                                      content_type='application/json')
        self.assertEqual(response.status_code, 204)

    def test_put_user(self):
        self.client.post('/users', 
                         data=json.dumps({"name": "Wojciech", "lastname": "Oczkowski"}), 
                         content_type='application/json')
        response = self.client.put('/users/1', 
                                    data=json.dumps({"name": "Jan", "lastname": "Kowalski"}), 
                                    content_type='application/json')
        self.assertEqual(response.status_code, 204)

    def test_delete_user(self):
        self.client.post('/users', 
                         data=json.dumps({"name": "Wojciech", "lastname": "Oczkowski"}), 
                         content_type='application/json')
        response = self.client.delete('/users/1')
        self.assertEqual(response.status_code, 204)

    def test_delete_nonexistent_user(self):
        response = self.client.delete('/users/999')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()