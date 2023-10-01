# given clean text, tokenize

import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def tokenize(text):
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