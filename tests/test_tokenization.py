import unittest
from services.tokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    
    def test_tokenize_and_clean(self):
        text = "This is a Test! 123"
        text = self.tokenizer.clean(text)
        tokens = self.tokenizer.tokenize(text)
        self.assertEqual(tokens, ['this', 'is', 'a', 'test'])  

    def test_clean_tokenize_and_remove_stopwords(self):
        text = "This is a Test! 123"
        text = self.tokenizer.clean(text)
        tokens = self.tokenizer.tokenize(text)
        tokens = self.tokenizer.remove_stopwords(tokens)
        self.assertEqual(tokens, ['test'])
    
    def test_tokenize(self):
        text = "This is a test"
        text = self.tokenizer.clean(text)
        tokens = self.tokenizer.tokenize(text)
        self.assertEqual(tokens, ['this', 'is', 'a', 'test'])
    
    def test_empty_input(self):
        with self.assertRaises(ValueError):
            self.tokenizer.tokenize("")
    
    def test_none_input(self):
        with self.assertRaises(ValueError):
            self.tokenizer.tokenize(None)
    
    def clean_special_characters(self):
        text = "!@# $%^&* ():-;''"
        text = self.tokenizer.clean(text)
        self.assertEqual(text, "")

    def test_special_characters(self):
        text = "!@# $%^&* ():-;''"
        text = self.tokenizer.clean(text)
        tokens = self.tokenizer.tokenize(text)
        self.assertEqual(tokens, [])  
    
    def test_mixed_input(self):
        text = "Hello, World! 123"
        text = self.tokenizer.clean(text)
        tokens = self.tokenizer.tokenize(text)
        tokens = self.tokenizer.remove_stopwords(tokens)
        self.assertEqual(tokens, ['hello', 'world']) 

    
    def test_mixed_input_with_generic_words(self):
        text = "Hello, the World! 123"
        text = self.tokenizer.clean(text)
        tokens = self.tokenizer.tokenize(text)
        tokens = self.tokenizer.remove_stopwords(tokens)
        self.assertEqual(tokens, ['hello', 'world']) 
    
if __name__ == '__main__':
    unittest.main()
