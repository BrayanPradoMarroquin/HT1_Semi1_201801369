from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Endpoint 1: Verificación de estado
@app.route('/check', methods=['GET'])
def check():
    return '', 200

# Endpoint 2: Obtener objeto JSON
@app.route('/', methods=['GET'])
def home():
    data = {
        "Instancia": "Instancia #2 - API #2",
        "Curso": "Seminario de Sistemas 1",
        "Estudiante": "Brayan Hamllelo Estevem Prado Marroquín - 201801369"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
