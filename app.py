import os
from flask import Flask, render_template

app = Flask(__name__)

# Base de datos con los detalles y precios
productos = [
    {
        "id": 1,
        "nombre": "Xiaomi Redmi 14C",
        "precio": "$120usd",
        "img": "Xiaomi Redmi 14C.jpg",
        "detalle": """Xiaomi Redmi 14C smartphone 2024.
        
         ✅ 8GB de memoria RAM y 128GB de almacenamiento interno. 
 
         ✅ Especificaciones principales:
   ✔️ Pantalla: LCD de 6,88 pulgadas 120 Hz.
   ✔️ Procesador: MediaTek Helio G81-Ultra.
   ✔️ Cámaras: Trasera 50 MP / Frontal 13 MP.
   ✔️ Batería: 5.160 mAh con carga rápida de 18W.
   ✔️ Sistema: Xiaomi HyperOS (Android 14)."""
    },
    {
        "id": 2,
        "nombre": "Cargador Samsung 45W",
        "precio": "$4200cup",
        "img": "Cargador Samsung 45W.jpg",
        "detalle": "Travel Adapter de 45W con tecnología Super Fast Charging 2.0. Incluye cable USB-C a USB-C."
    },
    {
        "id": 3,
        "nombre": "Cargador Moreka 40W",
        "precio": "$4000cup",
        "img": "Cargador Moreka 40W .jpg",
        "detalle": "Modelo AC111-Carga Superrápida 40W. Puertos 20W PD y 20W QC 3.0. Incluye cable Tipo-C."
    },
    {
        "id": 4,
        "nombre": "Power Bank Solar 30,000mAh",
        "precio": "$18000cup",
        "img": "Cargador Portátil 30000mAh.jpg",
        "detalle": "✅ Capacidad: 30,000 mAh. ✅ Cables Integrados: Tipo-C / V8 / iPhone. ✅ Panel Solar con indicador."
    },
    {
        "id": 5,
        "nombre": "Power Bank Buytiti 10,000mAh",
        "precio": "$7000cup",
        "img": "Cargador Portátil 10000mAh.jpg",
        "detalle": "Cargador Portátil Buytiti. 10000 mAh, cables integrados para todas las conexiones, indicador LCD y linterna LED."
    },
    {
        "id": 6,
        "nombre": "Cargador para Coche",
        "precio": "$3600cup",
        "img": "Cargador para coche.jpg",
        "detalle": "6 puertos de carga rápida (4 USB y 2 Tipo-C). Pantalla digital LED con voltaje en tiempo real."
    },
    {
        "id": 7,
        "nombre": "Cables 1HORA",
        "precio": "$700cup",
        "img": "Cables 1HORA.jpg",
        "detalle": "Disponibles en Tipo C, V8 y iPhone. Soporta carga rápida y transferencia de datos."
    },
    {
        "id": 8,
        "nombre": "Portacelular",
        "precio": "$3200cup",
        "img": "Portacelular.jpg",
        "detalle": "Soporte de seguridad para bicicletas y motos. Diseñado para total estabilidad al conducir."
    }
]

@app.route('/')
def home():
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    # Usamos el puerto que asigne Render o el 8080 por defecto
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
