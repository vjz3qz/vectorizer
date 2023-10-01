import unittest
import numpy as np
from services.vectorizer import Vectorizer
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(dir_path, '../model/GoogleNews-vectors-negative300.bin')

class TestVectorizerIntegration(unittest.TestCase):
    def setUp(self):
        self.vectorizer = Vectorizer(path=model_path)

    def test_vectorize_integration(self):
        tokens = ['sample', 'text']
        vectors = self.vectorizer.vectorize(tokens)
        
        # Ensure the method returns the correct number of vectors
        self.assertEqual(len(vectors), len(tokens))
        
        # Ensure each returned object is a numpy array. 
        # This doesn’t check the content of the vectors, just the types.
        self.assertTrue(all(isinstance(vector, np.ndarray) for vector in vectors))

if __name__ == '__main__':
    unittest.main()
