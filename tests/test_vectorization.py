import unittest
import numpy as np
from services.vectorizer import Vectorizer
from unittest.mock import patch, MagicMock
import gensim.models

class TestVectorizer(unittest.TestCase):
    def setUp(self):
        mock_model = MagicMock()
        mock_model.__getitem__.return_value = np.array([1, 2, 3])
        with patch.object(gensim.models.KeyedVectors, 'load_word2vec_format', return_value=mock_model):
            self.vectorizer = Vectorizer()

    def test_vectorize(self):
        tokens = ['sample', 'text']
        vectors = self.vectorizer.vectorize(tokens)
        self.assertEqual(len(vectors), 2)  # Two vectors should be returned
        self.assertTrue(all(isinstance(vec, np.ndarray) for vec in vectors))  # Each vector should be a numpy array

    def test_empty_input(self):
        vectors = self.vectorizer.vectorize([])
        self.assertEqual(vectors, [])

    def test_none_input(self):
        with self.assertRaises(ValueError):
            self.vectorizer.vectorize(None)

if __name__ == '__main__':
    unittest.main()
