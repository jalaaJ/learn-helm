# test_app.py
import unittest
from main import app

class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a test client
        cls.client = app.test_client()

    def test_hello_world(self):
        # Send a GET request to the /hello endpoint
        response = self.client.get('/hello')
        
        # Check if the status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Check if the returned data is correct
        self.assertEqual(response.get_json(), {"data": "Hello World"})

if __name__ == '__main__':
    unittest.main()
