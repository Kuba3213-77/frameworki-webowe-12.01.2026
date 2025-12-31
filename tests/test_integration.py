import unittest
from app import app, users

class UserManagementIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        users.clear()

    def test_create_user(self):
        response = self.client.post('/users', 
                                     json={"name": "Wojciech", "lastname": "Oczkowski"})
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        self.client.post('/users', 
                         json={"name": "Wojciech", "lastname": "Oczkowski"})
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Wojciech", str(response.data))

    def test_get_user(self):
        self.client.post('/users', 
                         json={"name": "Wojciech", "lastname": "Oczkowski"})
        response = self.client.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Oczkowski", str(response.data))

    def test_patch_user(self):
        self.client.post('/users', 
                         json={"name": "Wojciech", "lastname": "Oczkowski"})
        response = self.client.patch('/users/1', 
                                      json={"name": "Jan"})
        self.assertEqual(response.status_code, 204)

    def test_put_user(self):
        self.client.post('/users', 
                         json={"name": "Wojciech", "lastname": "Oczkowski"})
        response = self.client.put('/users/1', 
                                    json={"name": "Jan", "lastname": "Kowalski"})
        self.assertEqual(response.status_code, 204)

    def test_delete_user(self):
        self.client.post('/users', 
                         json={"name": "Wojciech", "lastname": "Oczkowski"})
        response = self.client.delete('/users/1')
        self.assertEqual(response.status_code, 204)

    def test_delete_nonexistent_user(self):
        response = self.client.delete('/users/999')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
