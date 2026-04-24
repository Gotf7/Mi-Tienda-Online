from flask import Flask, render_template

app = Flask(__name__)

# Base de datos con los detalles y precios
productos = [
    {
        "id": 1,
        "nombre": "Cargador Samsung 45W",
        "precio": "$4200cup",
        "img": "Cargador Samsung 45W.WebP",
        "detalle": "Travel Adapter de 45W con tecnología Super Fast Charging 2.0. Incluye cable USB-C a USB-C de 5 amperios. Ideal para serie Galaxy S20 Ultra y superiores."
    },
    {
        "id": 2,
        "nombre": "Cargador Moreka 40W",
        "precio": "$4000cup",
        "img": "Cargador Moreka 40W .WebP",
        "detalle": "Modelo AC111-Carga Superrápida 40W. Puertos 20W PD y 20W QC 3.0. Incluye cable Tipo-C a Tipo-C de 1 metro y protección contra sobrecarga."
    },
    {
        "id": 3,
        "nombre": "Power Bank Solar 30,000mAh",
        "precio": "$18000cup",
        "img": "Cargador Portátil 30000mAh.WebP",
        "detalle": """✅Capacidad: 30,000 mAh (111Wh/3.7V), lo que permite múltiples cargas completas para la mayoría de los teléfonos inteligentes.

✅Cables Integrados:
✔️Tipo-C / V8 / (IPhone /iPad)
✔️USB estándar: Para recargar la propia batería.


✅Panel Solar con indicador."""
    },
    {
        "id": 4,
        "nombre": "Power Bank Buytiti 10,000mAh",
        "precio": "$7000cup",
        "img": "Cargador Portátil 10000mAh.WebP",
        "detalle": """Cargador Portátil Buytiti de 10000mAh. 

Capacidad: 10000 mAh, capaz de proporcionar aproximadamente 1.5 a 2 cargas completas para la mayoría de los teléfonos inteligentes modernos. 

Cables integrados: Incluye 4 cables incorporados compatibles con Micro USB/V8, Tipo C, Lightning y USB. 

Pantalla: Cuenta con un indicador LCD para mostrar el nivel de carga. 

Funciones adicionales: Incorpora una linterna LED, un gancho colgante y una entrada USB"""
    },
    {
        "id": 5,
        "nombre": "Cargador para Coche",
        "precio": "$3600cup",
        "img": "Cargador para coche.WebP",
        "detalle": "6 puertos de carga rápida (4 USB y 2 Tipo-C). Pantalla digital LED con voltaje en tiempo real y protección de sobrecarga."
    },
    {
        "id": 6,
        "nombre": "Cables 1HORA",
        "precio": "$700cup",
        "img": "Cables 1HORA.WebP",
        "detalle": "Disponibles en Tipo C, V8 y iPhone. Soporta carga rápida y transferencia de datos de alta velocidad."
    },
    {
        "id": 7,
        "nombre": "Portacelular",
        "precio": "$3200cup",
        "img": "Portacelular.WebP",
        "detalle": "Soporte de seguridad para bicicletas y motos. Diseñado para usar GPS o música con total estabilidad al conducir."
    },
    {
        "id": 8,
        "nombre": "Xiaomi Redmi 14C",
        "precio": "$120usd",
        "img": "Xiaomi Redmi 14C.WebP",
        "detalle": """Xiaomi Redmi 14C, un smartphone de gama de entrada lanzado a finales de agosto de 2024. La versión que muestras en la imagen cuenta con 8GB de memoria RAM y 128GB de almacenamiento interno, como indica la etiqueta de la caja. 
A continuación, te detallo sus especificaciones principales:
Especificaciones Técnicas
Pantalla: LCD de 6,88 pulgadas con resolución HD+ (1640 x 720 px) y una tasa de refresco fluida de 120 Hz.
Procesador: MediaTek Helio G81-Ultra (ocho núcleos hasta 2,0 GHz).
Cámaras:
Trasera principal: Sensor de 50 MP con inteligencia artificial.
Frontal: 13 MP para selfies.
Batería: Capacidad de 5.160 mAh con soporte para carga rápida de 18W.
Sistema Operativo: Xiaomi HyperOS basado en Android 14.
Otras características: Incluye conector jack de 3,5 mm para auriculares, Radio FM, sensor de huellas lateral y soporte para Dual SIM."""
    }
]

@app.route('/')
def home():
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
