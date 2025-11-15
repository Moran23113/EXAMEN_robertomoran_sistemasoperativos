from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensaje": "Examen Docker", "estudiante": "Moran"})

@app.route('/salud')
def salud():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Aplicación iniciada en puerto {port}")
    app.run(host='0.0.0.0', port=port)