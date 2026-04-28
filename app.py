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
    },
    {   
        "id": 9,
        "nombre": "Bocina Portátil",
        "precio": "$11500cup",
        "img": "Bocina inalámbrica.jpg",
        "detalle": """Bocina inalámbrica portátil 1Hora BOC242 en color negro. Este altavoz se caracteriza por su diseño compacto y cilíndrico, que incluye un sistema de iluminación RGB ajustable sincronizado con la música. 

Especificaciones y Características
Potencia de sonido: Cuenta con 10W de potencia, ofreciendo un sonido estéreo con agudos claros y graves profundos.
Batería: Tiene una capacidad de 2400 mAh, lo que proporciona aproximadamente 3.5 horas de uso continuo con una sola carga, como se indica en el empaque de la imagen.
Conectividad: Utiliza tecnología Bluetooth 5.1 para una conexión estable. También soporta múltiples entradas como USB, tarjeta micro SD (TF), AUX y cuenta con radio FM integrada.
Tecnología TWS: Permite el emparejamiento de dos bocinas del mismo modelo para obtener un sonido estéreo inalámbrico real."""},
      {
        "id": 10,
        "nombre": "Mouse inhalámbrico 1HORA",
        "precio": "$4500cup",
        "img": "Mouse 1HORA.jpg",
        "detalle": """Mouse Inalámbrico 1Hora, específicamente el modelo RAT001, un dispositivo ergonómico diseñado para ofrecer comodidad y un funcionamiento silencioso. Se caracteriza por ser una opción económica que utiliza una conexión estable de 2.4 GHz mediante un receptor nano USB. 

Características Principales
Silencioso: Sus clics reducen el ruido hasta en un 90%, ideal para entornos tranquilos como bibliotecas u oficinas.
Resolución Ajustable (DPI): Ofrece tres niveles de sensibilidad (800, 1200 y 1600 DPI) para adaptarse a diferentes tareas y pantallas.
Alcance: Funciona a una distancia de hasta 10 metros de la computadora.
Alimentación: Utiliza una pila AA (no incluida en algunos paquetes), con una duración estimada de hasta 18 meses gracias a su modo de ahorro de energía.
Compatibilidad: Funciona con Windows, macOS, Linux, Chrome OS y Android."""},  
     { "id": 11,
        "nombre": "Mouse Inalámbrico Buytiti",
        "precio": "$4300cup",
        "img": "Mouse Buytiti.jpg",
        "detalle": """Mouse inalámbrico recargable con luz LED RGB de la marca Buytiti, específicamente el modelo RF-2835. Es un periférico diseñado tanto para el trabajo diario como para juegos ocasionales, destacando por su diseño ergonómico y delgado que reduce la fatiga durante el uso prolongado. 

Características Principales
Doble Conectividad: Permite conectarse a través de Bluetooth (ideal para laptops y tabletas) o mediante un nano receptor USB de 2.4 GHz (radiofrecuencia) que se guarda en la parte inferior del mouse.
Sensibilidad Ajustable: Cuenta con un botón dedicado para cambiar los DPI (puntos por pulgada), ofreciendo niveles de hasta 1600 DPI o 3200 DPI según la variante del modelo.
Batería Recargable: No requiere pilas externas. Se carga mediante un cable USB (incluido) y una carga completa de aproximadamente 2 horas puede proporcionar energía para varias semanas de uso.
Iluminación RGB: Presenta luces LED que cambian de color automáticamente en el perímetro y la rueda de desplazamiento.
Compatibilidad: Funciona con Windows, macOS, Android y Smart TVs"""}
]

@app.route('/')
def home():
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    # Usamos el puerto que asigne Render o el 8080 por defecto
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
