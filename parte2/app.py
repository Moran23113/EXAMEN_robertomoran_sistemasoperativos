from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    respuesta = {
        "mensaje": "Examen Docker - revisión personal Moran",
        "estudiante": "Moran",
        "comentario": "Validación manual 2025-11-15"
    }
    return jsonify(respuesta)

@app.route('/salud')
def salud():
    return jsonify({"status": "ok", "nota": "Chequeo rápido antes de entrega"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Aplicación iniciada en puerto {port}")
    app.run(host='0.0.0.0', port=port)