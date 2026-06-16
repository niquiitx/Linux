from flask import Flask, request, jsonify
from datetime import datetime
import socket
import os
app = Flask(__name__)

# Inventario inventado
registros = {
    "servidor": "ruiz-server",
    "hora_servidor": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "inventario": [
        {
            "placa": "ABC123",
            "modelo": "Yamaha FZ",
            "color": "Negro"
        },
        {
            "placa": "XYZ789",
            "modelo": "Honda CB190R",
            "color": "Rojo"
        }
    ]
}

# Lista de peritajes
peritajes = [
    {
        "placa": "NSRS3057"
    }
]

# Ruta GET inventario
@app.route('/api/registros', methods=['GET'])
def obtener_registros():
    return jsonify(registros)

# Ruta GET peritajes
@app.route('/api/peritajes', methods=['GET'])
def obtener_peritajes():
    return jsonify(peritajes)

# NUEVA RUTA INVENTARIO
@app.route('/api/inventario', methods=['GET'])
def inventario():
    return jsonify({
        "mensaje": "Inventario en desarrollo",
        "repuestos": [
            "Aceite",
            "Bujias",
            "Filtros"
        ]
    })

# RUTA FACTURAS CON ERROR 500 INTENCIONAL
@app.route('/api/facturas', methods=['GET'])
def obtener_facturas():

   

    return jsonify({
        "facturas": [
            {
                "cliente": "Nicolas Ruiz",
                "moto": "Yamaha FZ",
                "valor": 350000
            },
            {
                "cliente": "Laura Gomez",
                "moto": "Honda CB190R",
                "valor": 420000
            }
        ]
    })

# Ruta POST peritajes
@app.route('/api/peritajes', methods=['POST'])
def registrar_peritaje():
    data = request.json

    nueva_moto = {
        "placa": data["placa"].upper()
    }

    peritajes.append(nueva_moto)

    return jsonify({
        "mensaje": "Moto registrada correctamente",
        "datos": nueva_moto
    }), 201

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
    