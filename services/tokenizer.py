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
    
    def tokenize(text):
        """
        Tokenizes the input text.
        :param text: Input text string.
        :return: List of word tokens.
        """
        # Check if text is not None and is not an empty string
        if not text:
            raise ValueError("Input text should not be None or empty.")
        # clean the text. rn no numbers, no punctuation
        text = re.sub('[^A-Za-z]', ' ', text)
        text = text.lower()
        
        # Tokenize the text
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word not in self.stopwords]

        return tokens