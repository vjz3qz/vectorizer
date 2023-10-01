import unittest
from services.tokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    
    def test_tokenize_and_clean(self):
        text = "This is a Test! 123"
        tokens = self.tokenizer.tokenize(text)
        self.assertEqual(tokens, ['this', 'is', 'a', 'test'])  
    
    def test_tokenize(self):
        text = "This is a test"
        tokens = self.tokenizer.tokenize(text)
        self.assertEqual(tokens, ['this', 'is', 'a', 'test'])
    
    def test_empty_input(self):
        text = ""
        tokens = self.tokenizer.tokenize(text)
        self.assertEqual(tokens, [])
    
    def test_none_input(self):
        with self.assertRaises(TypeError):
            tokens = self.tokenizer.tokenize(None)
    
    def test_special_characters(self):
        text = "!@# $%^&* ():-;''"
        tokens = self.tokenizer.tokenize(text)
        self.assertEqual(tokens, [])  
    
    def test_mixed_input(self):
        text = "Hello, World! 123"
        tokens = self.tokenizer.tokenize(text)
        self.assertEqual(tokens, ['hello', 'world']) 
    
if __name__ == '__main__':
    unittest.main()
