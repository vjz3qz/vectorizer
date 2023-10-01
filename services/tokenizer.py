# given  text, clean and tokenize
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

class Tokenizer:
    def __init__(self):
        self.stopwords = set(stopwords.words('english'))
    
    def clean(self, text):
        """
        Cleans the input text by removing special characters and numbers.
        :param text: Input text string.
        :return: Cleaned text string.
        """
        # Check if text is not None and is not an empty string
        if not text:
            raise ValueError("Input text should not be None or empty.")
        # clean the text. rn no numbers, no punctuation
        text = re.sub('[^A-Za-z]', ' ', text)
        text = text.lower()
        return text
    
    def tokenize(self, text):
        """
        Tokenizes the input text.
        :param text: Input text string.
        :return: List of word tokens.
        """
        # Check if text is not None and is not an empty string
        if not text:
            raise ValueError("Input text should not be None or empty.")
        
        # Tokenize the text
        tokens = word_tokenize(text)

        return tokens
    
    def remove_stopwords(self, tokens):
        """
        Removes stopwords from the input list of tokens.
        :param tokens: List of word tokens.
        :return: List of tokens with stopwords removed.
        """
        # Check if tokens is not None and is not an empty list
        if not tokens:
            raise ValueError("Input tokens should not be None or empty.")
        
        # Remove stopwords
        tokens = [token for token in tokens if token not in self.stopwords]

        return tokens