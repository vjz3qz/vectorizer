from flask import Flask
from routes import setup_routes

app = Flask(__name__)

# Setup routes
setup_routes(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
