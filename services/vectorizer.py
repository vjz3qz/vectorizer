import gensim.models # should use FastText instead
# can also use Transformer models from HuggingFace
import numpy as np

class Vectorizer:
    def __init__(self, model_path = '../model/GoogleNews-vectors-negative300.bin'):
        self.model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)
    
    def vectorize(self, tokens):
        """
        Vectorizes the input tokens.
        :param tokens: List of word tokens.
        :return: A list of vectors representing the input tokens.
        """
        vectors = []
        for token in tokens:
            try:
                vector = self.model[token] 
                vectors.append(vector)
            except KeyError:
                vectors.append(np.zeros(300,))
        return vectors
