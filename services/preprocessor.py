# given text, clean the text

import re

def clean(text):
    # remove non-alphabetic characters
    text = re.sub('[^A-Za-z]', ' ', text)
    # make all characters lowercase
    text = text.lower()
    # remove whitespaces
    text = text.strip()
    return text