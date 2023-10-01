import unittest
from services import tokenizer

class TestTokenizer(unittest.TestCase):
    def test_tokenize(self):
        text = "This is a test"
        tokens = tokenizer.tokenize(text)
        self.assertEqual(tokens, ['this', 'is', 'a', 'test'])

    def test_empty_input(self):
        text = ""
        tokens = tokenizer.tokenize(text)
        self.assertEqual(tokens, [])
    
    def test_none_input(self):
        with self.assertRaises(TypeError):
            tokens = tokenizer.tokenize(None)

if __name__ == '__main__':
    unittest.main()


