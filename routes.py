from flask import request, jsonify
from services.tokenizer import Tokenizer
from services.vectorizer import Vectorizer

def setup_routes(app):
    @app.route('/vectorize', methods=['POST'])
    def vectorize():
        try:
            # we get the text parameter from the request body
            data = request.json 
            text = data.get('text') 

            if not text:
                return jsonify({'error': 'Missing text'}), 400
            
            tokenizer = Tokenizer()
            tokens = tokenizer.tokenize(text)
            vectorizer = Vectorizer()
            vector = vectorizer.vectorize(tokens)

            return jsonify({'vector': vector}), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500