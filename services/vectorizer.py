import gensim.models # should use FastText instead
# can also use Transformer models from HuggingFace
import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(dir_path, '../model/GoogleNews-vectors-negative300.bin')

class Vectorizer:
    def __init__(self, path = model_path):
        self.model = gensim.models.KeyedVectors.load_word2vec_format(path, binary=True)
    
    def vectorize(self, tokens):
        """
        Vectorizes the input tokens.
        :param tokens: List of word tokens.
        :return: A list of vectors representing the input tokens.
        """
        if tokens is None:
            raise ValueError("Input tokens should not be None")
        vectors = []
        for token in tokens:
            try:
                vector = self.model[token] 
                vectors.append(vector)
            except KeyError:
                vectors.append(np.zeros(300,))
        return vectors
