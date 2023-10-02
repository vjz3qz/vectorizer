from flask import request, jsonify
from services.tokenizer import Tokenizer
from services.vectorizer import Vectorizer

def setup_routes(app):
    @app.route('/vectorize', methods=['POST'])
    def vectorize():

        vectors = []
        try:
            # we get the text parameter from the request body
            data = request.get_json(force=True)
            text = data.get('text') 

            if not text:
                return jsonify({'error': 'Missing text'}), 400
            
            tokenizer = Tokenizer()
            tokens = tokenizer.tokenize(text)
            vectorizer = Vectorizer()
            vectors = vectorizer.vectorize(tokens)
            vectors = [vector.tolist() for vector in vectors]

            # # URL of the Receiver microservice
            # url = "http://receiver-service-url/receive-vector"
            
            # # Sending vector to the Receiver microservice
            # response = requests.post(url, json={'vector': vector}) # sends as a list

            # # Check if the request was successful
            # if response.status_code != 200:
            #     app.logger.error(f"Failed to send vector to Receiver service. Response: {response.text}")
            #     return jsonify({'error': 'Failed to send vector to Receiver service'}), 500
            
            return jsonify({'message': 'Vector sent successfully', 'vector': vectors}), 200
        
        except ValueError as ve:
            return jsonify({'error': 'Invalid input: ' + str(ve)}), 400     
        except Exception as e:
            return jsonify({'error': str(e)}), 500