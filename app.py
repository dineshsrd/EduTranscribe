from flask import Flask
from apigenerator import api_blueprint

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(api_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
