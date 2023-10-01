import unittest
from flask import Flask
from routes import setup_routes  
import json
import numpy as np
from unittest.mock import patch

class IntegrationTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        setup_routes(self.app)
        self.client = self.app.test_client()

    def test_vectorization_flow(self):
        with patch('services.vectorizer.Vectorizer.__init__', return_value=None), \
            patch('services.vectorizer.Vectorizer.vectorize', return_value='some_vector'), \
            patch('requests.post') as mock_post:
            
            # Mock the response from the Receiver microservice
            response = self.client.post('/vectorize', json={'text': 'sample text'})
            
            print("Response Data:", response.data)  # Print response data
            print("Response Status Code:", response.status_code)  # Print response status code
            
            if response.status_code != 200:
                print(f"Error: {response.data}")
                self.fail("The route returned an error.")
            
            self.assertTrue(mock_post.called, "The post method was not called.")



        
if __name__ == '__main__':
    unittest.main()
