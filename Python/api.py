from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint 1: Verificación de estado
@app.route('/check', methods=['GET'])
def check():
    return '', 200

# Endpoint 2: Obtener objeto JSON
@app.route('/', methods=['GET'])
def home():
    data = {
        "message": "Hello from the Python API!",
        "timestamp": "datetime.now()"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
