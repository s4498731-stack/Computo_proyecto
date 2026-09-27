import streamlit as st
import random

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

st.set_page_config(
    page_title="StudyGen",
    page_icon="📚",
    layout="centered"
)

st.title("StudyGen")
st.write(
    "Plataforma de estudio que genera preguntas "
    "según la materia, tema y dificultad."
)

st.divider()


# ==========================================================
# BANCO DE PREGUNTAS
# 10 preguntas por cada tema y dificultad
# ==========================================================

banco_preguntas = {

    # ======================================================
    # MATEMÁTICA
    # ======================================================

    "Matemática": {

        "Álgebra": {

            "Fácil": [
                {"pregunta": "¿Qué es una variable?", "respuesta": "Es un símbolo que representa un valor que puede cambiar."},
                {"pregunta": "¿Cuál es el coeficiente de x en 7x + 3?", "respuesta": "7."},
                {"pregunta": "¿Cuál es el término independiente de 4x + 9?", "respuesta": "9."},
                {"pregunta": "¿Cuánto es 5 + 8?", "respuesta": "13."},
                {"pregunta": "¿Cuánto es 12 - 7?", "respuesta": "5."},
                {"pregunta": "¿Cuánto es 6 × 4?", "respuesta": "24."},
                {"pregunta": "¿Cuánto es 36 ÷ 6?", "respuesta": "6."},
                {"pregunta": "¿Qué significa 3x?", "respuesta": "Tres veces el valor de x."},
                {"pregunta": "¿Cuál es el coeficiente de y en 9y - 2?", "respuesta": "9."},
                {"pregunta": "¿Cuánto vale x + 5 si x = 3?", "respuesta": "8."}
            ],

            "Medio": [
                {"pregunta": "Resuelve: 2x + 6 = 18.", "respuesta": "x = 6."},
                {"pregunta": "Resuelve: 3x - 5 = 16.", "respuesta": "x = 7."},
                {"pregunta": "Resuelve: 4x + 8 = 24.", "respuesta": "x = 4."},
                {"pregunta": "Resuelve: 5x - 10 = 20.", "respuesta": "x = 6."},
                {"pregunta": "Resuelve: 7x + 3 = 24.", "respuesta": "x = 3."},
                {"pregunta": "Resuelve: 6x - 12 = 30.", "respuesta": "x = 7."},
                {"pregunta": "Resuelve: 8x = 64.", "respuesta": "x = 8."},
                {"pregunta": "Resuelve: x + 15 = 27.", "respuesta": "x = 12."},
                {"pregunta": "Resuelve: 9x - 18 = 45.", "respuesta": "x = 7."},
                {"pregunta": "Resuelve: 10x + 5 = 55.", "respuesta": "x = 5."}
            ],

            "Difícil": [
                {"pregunta": "Resuelve: 2x + 8 = 4x - 6.", "respuesta": "x = 7."},
                {"pregunta": "Resuelve: 5(x - 2) = 25.", "respuesta": "x = 7."},
                {"pregunta": "Resuelve: 3(x + 4) = 2x + 15.", "respuesta": "x = 3."},
                {"pregunta": "Resuelve: 4(x - 3) + 2 = 18.", "respuesta": "x = 7."},
                {"pregunta": "Resuelve: 2(x + 5) = 3x - 4.", "respuesta": "x = 14."},
                {"pregunta": "Resuelve: 6(x - 1) = 2x + 14.", "respuesta": "x = 5."},
                {"pregunta": "Resuelve: 4(x + 2) = 2x + 18.", "respuesta": "x = 5."},
                {"pregunta": "Resuelve: 7x - 4 = 3x + 20.", "respuesta": "x = 6."},
                {"pregunta": "Resuelve: 9x + 3 = 5x + 27.", "respuesta": "x = 6."},
                {"pregunta": "Resuelve: 3(x - 5) = x + 7.", "respuesta": "x = 11."}
            ]
        },

        "Geometría": {

            "Fácil": [
                {"pregunta": "¿Cuántos lados tiene un triángulo?", "respuesta": "3 lados."},
                {"pregunta": "¿Cuántos lados tiene un cuadrado?", "respuesta": "4 lados."},
                {"pregunta": "¿Cuántos grados mide un ángulo recto?", "respuesta": "90 grados."},
                {"pregunta": "¿Cuántos grados suman los ángulos de un triángulo?", "respuesta": "180 grados."},
                {"pregunta": "¿Cómo se llama un polígono de cinco lados?", "respuesta": "Pentágono."},
                {"pregunta": "¿Cómo se llama un polígono de seis lados?", "respuesta": "Hexágono."},
                {"pregunta": "¿Cuántos lados tiene un octágono?", "respuesta": "8 lados."},
                {"pregunta": "¿Qué figura tiene todos sus lados iguales y cuatro ángulos rectos?", "respuesta": "El cuadrado."},
                {"pregunta": "¿Cómo se llama un ángulo menor de 90 grados?", "respuesta": "Ángulo agudo."},
                {"pregunta": "¿Cómo se llama un ángulo mayor de 90 y menor de 180 grados?", "respuesta": "Ángulo obtuso."}
            ],

            "Medio": [
                {"pregunta": "¿Cuál es el área de un rectángulo de 8 cm por 5 cm?", "respuesta": "40 cm²."},
                {"pregunta": "¿Cuál es el perímetro de un cuadrado de lado 9 cm?", "respuesta": "36 cm."},
                {"pregunta": "¿Cuál es el área de un triángulo de base 10 cm y altura 6 cm?", "respuesta": "30 cm²."},
                {"pregunta": "¿Cuál es el perímetro de un rectángulo de 12 cm por 5 cm?", "respuesta": "34 cm."},
                {"pregunta": "¿Cuál es el área de un cuadrado de lado 7 cm?", "respuesta": "49 cm²."},
                {"pregunta": "¿Cuál es el perímetro de un triángulo cuyos lados miden 5, 6 y 7 cm?", "respuesta": "18 cm."},
                {"pregunta": "¿Cuál es el área de un rectángulo de 15 cm por 4 cm?", "respuesta": "60 cm²."},
                {"pregunta": "¿Cuál es el perímetro de un cuadrado de lado 12 cm?", "respuesta": "48 cm."},
                {"pregunta": "¿Cuál es el área de un triángulo de base 12 cm y altura 8 cm?", "respuesta": "48 cm²."},
                {"pregunta": "¿Cuál es el área de un cuadrado de lado 11 cm?", "respuesta": "121 cm²."}
            ],

            "Difícil": [
                {"pregunta": "¿Cuál es el área de un círculo de radio 5 cm?", "respuesta": "25π cm², aproximadamente 78.54 cm²."},
                {"pregunta": "Un rectángulo tiene un área de 72 cm² y un ancho de 8 cm. ¿Cuál es su largo?", "respuesta": "9 cm."},
                {"pregunta": "¿Cuál es el volumen de un cubo cuyo lado mide 4 cm?", "respuesta": "64 cm³."},
                {"pregunta": "¿Cuál es el área de un trapecio con bases 8 cm y 12 cm y altura 5 cm?", "respuesta": "50 cm²."},
                {"pregunta": "¿Cuál es el volumen de un prisma rectangular de 3 × 4 × 5 cm?", "respuesta": "60 cm³."},
                {"pregunta": "¿Cuál es la hipotenusa de un triángulo rectángulo con catetos 6 y 8 cm?", "respuesta": "10 cm."},
                {"pregunta": "¿Cuál es el área de un círculo de diámetro 10 cm?", "respuesta": "25π cm², aproximadamente 78.54 cm²."},
                {"pregunta": "Un cuadrado tiene un área de 144 cm². ¿Cuánto mide cada lado?", "respuesta": "12 cm."},
                {"pregunta": "Un rectángulo tiene perímetro de 30 cm y ancho de 5 cm. ¿Cuál es su largo?", "respuesta": "10 cm."},
                {"pregunta": "¿Cuál es el volumen de un cubo de lado 6 cm?", "respuesta": "216 cm³."}
            ]
        },

        "Porcentajes": {

            "Fácil": [
                {"pregunta": "¿Cuánto es el 10% de 100?", "respuesta": "10."},
                {"pregunta": "¿Cuánto es el 50% de 80?", "respuesta": "40."},
                {"pregunta": "¿Cuánto es el 20% de 50?", "respuesta": "10."},
                {"pregunta": "¿Cuánto es el 25% de 100?", "respuesta": "25."},
                {"pregunta": "¿Cuánto es el 10% de 500?", "respuesta": "50."},
                {"pregunta": "¿Cuánto es el 5% de 200?", "respuesta": "10."},
                {"pregunta": "¿Cuánto es el 50% de 60?", "respuesta": "30."},
                {"pregunta": "¿Cuánto es el 25% de 40?", "respuesta": "10."},
                {"pregunta": "¿Cuánto es el 10% de 300?", "respuesta": "30."},
                {"pregunta": "¿Cuánto es el 20% de 200?", "respuesta": "40."}
            ],

            "Medio": [
                {"pregunta": "¿Cuánto es el 20% de 250?", "respuesta": "50."},
                {"pregunta": "Un producto cuesta S/200 y tiene 15% de descuento. ¿Cuánto se descuenta?", "respuesta": "S/30."},
                {"pregunta": "¿Cuánto es el 30% de 400?", "respuesta": "120."},
                {"pregunta": "Un producto de S/80 aumenta 10%. ¿Cuál es su nuevo precio?", "respuesta": "S/88."},
                {"pregunta": "¿Cuánto es el 15% de 300?", "respuesta": "45."},
                {"pregunta": "¿Cuánto es el 35% de 200?", "respuesta": "70."},
                {"pregunta": "Un producto de S/100 tiene un descuento del 20%. ¿Cuál es el precio final?", "respuesta": "S/80."},
                {"pregunta": "¿Cuánto es el 12% de 500?", "respuesta": "60."},
                {"pregunta": "Un precio de S/300 aumenta 10%. ¿Cuál es el nuevo precio?", "respuesta": "S/330."},
                {"pregunta": "¿Cuánto es el 40% de 250?", "respuesta": "100."}
            ],

            "Difícil": [
                {"pregunta": "Un producto cuesta S/400 y aumenta 20%. ¿Cuál es su nuevo precio?", "respuesta": "S/480."},
                {"pregunta": "Después de un descuento del 25%, un producto cuesta S/150. ¿Cuál era su precio original?", "respuesta": "S/200."},
                {"pregunta": "Un precio de S/500 aumenta 15%. ¿Cuál es el nuevo precio?", "respuesta": "S/575."},
                {"pregunta": "Un producto de S/800 tiene dos descuentos consecutivos de 10%. ¿Cuál es su precio final?", "respuesta": "S/648."},
                {"pregunta": "Un producto de S/250 aumenta 30%. ¿Cuál es el nuevo precio?", "respuesta": "S/325."},
                {"pregunta": "Un producto de S/600 disminuye 15%. ¿Cuál es el precio final?", "respuesta": "S/510."},
                {"pregunta": "Un producto cuesta S/360 después de un descuento del 20%. ¿Cuál era su precio original?", "respuesta": "S/450."},
                {"pregunta": "Un precio aumenta de S/200 a S/250. ¿Cuál fue el porcentaje de aumento?", "respuesta": "25%."},
                {"pregunta": "Un precio disminuye de S/500 a S/400. ¿Cuál fue el porcentaje de disminución?", "respuesta": "20%."},
                {"pregunta": "Un producto de S/1000 aumenta 10% y luego disminuye 10%. ¿Cuál es el precio final?", "respuesta": "S/990."}
            ]
        }
    },


    # ======================================================
    # CIENCIA Y TECNOLOGÍA
    # ======================================================

    "Ciencia y Tecnología": {

        "Sistema nervioso": {

            "Fácil": [
                {"pregunta": "¿Cuál es el órgano principal del sistema nervioso?", "respuesta": "El cerebro."},
                {"pregunta": "¿Qué células transmiten impulsos nerviosos?", "respuesta": "Las neuronas."},
                {"pregunta": "¿Qué estructura conecta el cerebro con gran parte del cuerpo?", "respuesta": "La médula espinal."},
                {"pregunta": "¿Qué sistema permite responder a estímulos?", "respuesta": "El sistema nervioso."},
                {"pregunta": "¿Dónde se encuentra la médula espinal?", "respuesta": "En el interior de la columna vertebral."},
                {"pregunta": "¿Qué parte de la neurona recibe principalmente señales?", "respuesta": "Las dendritas."},
                {"pregunta": "¿Qué parte de la neurona transmite el impulso nervioso?", "respuesta": "El axón."},
                {"pregunta": "¿Qué órgano participa en el equilibrio y coordinación?", "respuesta": "El cerebelo."},
                {"pregunta": "¿Qué protege al cerebro?", "respuesta": "El cráneo."},
                {"pregunta": "¿Qué protege a la médula espinal?", "respuesta": "La columna vertebral."}
            ],

            "Medio": [
                {"pregunta": "¿Cuál es la función principal del sistema nervioso?", "respuesta": "Coordinar y controlar las funciones del organismo y responder a estímulos."},
                {"pregunta": "¿Qué función cumple la médula espinal?", "respuesta": "Comunica el cerebro con el cuerpo y participa en actos reflejos."},
                {"pregunta": "¿Qué es una neurona?", "respuesta": "Es una célula especializada en recibir y transmitir información nerviosa."},
                {"pregunta": "¿Qué función cumplen las dendritas?", "respuesta": "Reciben señales de otras células."},
                {"pregunta": "¿Qué función cumple el axón?", "respuesta": "Conduce el impulso nervioso hacia otras células."},
                {"pregunta": "¿Qué función cumple el cerebelo?", "respuesta": "Participa en la coordinación de movimientos y el equilibrio."},
                {"pregunta": "¿Qué es un acto reflejo?", "respuesta": "Es una respuesta rápida y automática ante un estímulo."},
                {"pregunta": "¿Qué diferencia existe entre sistema nervioso central y periférico?", "respuesta": "El central incluye encéfalo y médula espinal; el periférico incluye los nervios."},
                {"pregunta": "¿Qué función tiene el cerebro?", "respuesta": "Participa en funciones como pensamiento, memoria, percepción y control voluntario."},
                {"pregunta": "¿Qué son los nervios?", "respuesta": "Son estructuras formadas por fibras nerviosas que comunican el sistema nervioso central con el resto del cuerpo."}
            ],

            "Difícil": [
                {"pregunta": "¿Cómo se comunican las neuronas entre sí?", "respuesta": "Mediante señales eléctricas y sustancias químicas llamadas neurotransmisores."},
                {"pregunta": "¿Qué es la sinapsis?", "respuesta": "Es la comunicación funcional entre una neurona y otra célula."},
                {"pregunta": "¿Cuál es la diferencia entre una respuesta voluntaria y una refleja?", "respuesta": "La voluntaria está bajo control consciente; la refleja ocurre de manera rápida y automática."},
                {"pregunta": "¿Por qué la médula espinal es importante?", "respuesta": "Porque comunica el encéfalo con el cuerpo y participa en respuestas reflejas."},
                {"pregunta": "¿Qué función cumplen los neurotransmisores?", "respuesta": "Permiten transmitir señales químicas entre neuronas y otras células."},
                {"pregunta": "¿Qué relación existe entre estímulo y respuesta?", "respuesta": "Un estímulo es detectado por receptores y desencadena una respuesta coordinada por el sistema nervioso."},
                {"pregunta": "¿Qué podría ocurrir si se daña una parte del sistema nervioso?", "respuesta": "Podrían alterarse funciones como el movimiento, sensibilidad, coordinación o percepción."},
                {"pregunta": "¿Qué función cumple la corteza cerebral?", "respuesta": "Participa en funciones superiores como pensamiento, lenguaje, memoria y percepción."},
                {"pregunta": "¿Por qué las neuronas están especializadas?", "respuesta": "Porque su estructura permite recibir, procesar y transmitir información."},
                {"pregunta": "¿Cómo participa el sistema nervioso en la coordinación del cuerpo?", "respuesta": "Recibe información, la procesa y genera respuestas mediante señales nerviosas."}
            ]
        },

        "Fotosíntesis": {

            "Fácil": [
                {"pregunta": "¿Qué organismos realizan principalmente la fotosíntesis?", "respuesta": "Las plantas, algas y algunos microorganismos."},
                {"pregunta": "¿Qué gas utilizan las plantas?", "respuesta": "Dióxido de carbono."},
                {"pregunta": "¿Qué fuente de energía utiliza la fotosíntesis?", "respuesta": "La luz."},
                {"pregunta": "¿Dónde ocurre principalmente la fotosíntesis?", "respuesta": "En los cloroplastos."},
                {"pregunta": "¿Qué gas se libera durante la fotosíntesis?", "respuesta": "Oxígeno."},
                {"pregunta": "¿Qué pigmento capta la luz?", "respuesta": "La clorofila."},
                {"pregunta": "¿Qué sustancia necesitan las plantas además del dióxido de carbono?", "respuesta": "Agua."},
                {"pregunta": "¿Qué produce la planta como alimento?", "respuesta": "Glucosa."},
                {"pregunta": "¿En qué parte de la planta entra principalmente el dióxido de carbono?", "respuesta": "A través de los estomas de las hojas."},
                {"pregunta": "¿Por qué la fotosíntesis necesita luz?", "respuesta": "Porque la luz proporciona energía para el proceso."}
            ],

            "Medio": [
                {"pregunta": "¿Qué necesitan las plantas para realizar la fotosíntesis?", "respuesta": "Luz, agua y dióxido de carbono."},
                {"pregunta": "¿Qué sustancia producen durante la fotosíntesis?", "respuesta": "Glucosa."},
                {"pregunta": "¿Qué gas se libera como producto?", "respuesta": "Oxígeno."},
                {"pregunta": "¿Qué pigmento permite captar la energía luminosa?", "respuesta": "La clorofila."},
                {"pregunta": "¿Qué función cumplen los cloroplastos?", "respuesta": "Son los organelos donde ocurre principalmente la fotosíntesis."},
                {"pregunta": "¿Por qué las hojas suelen ser verdes?", "respuesta": "Porque la clorofila refleja principalmente la luz verde."},
                {"pregunta": "¿Qué papel cumple el agua?", "respuesta": "Participa como materia prima del proceso fotosintético."},
                {"pregunta": "¿Qué papel cumple el dióxido de carbono?", "respuesta": "Aporta carbono para formar moléculas orgánicas como la glucosa."},
                {"pregunta": "¿Qué importancia tiene la fotosíntesis para los seres humanos?", "respuesta": "Produce oxígeno y materia orgánica que forma parte de las cadenas alimentarias."},
                {"pregunta": "¿Qué relación existe entre fotosíntesis y alimentación?", "respuesta": "La fotosíntesis produce materia orgánica que sirve de base para las cadenas alimentarias."}
            ],

            "Difícil": [
                {"pregunta": "¿Por qué la fotosíntesis es importante para los ecosistemas?", "respuesta": "Porque produce materia orgánica y contribuye a la liberación de oxígeno y al ciclo del carbono."},
                {"pregunta": "¿Cómo participa la fotosíntesis en el ciclo del carbono?", "respuesta": "Incorpora dióxido de carbono de la atmósfera a la materia orgánica."},
                {"pregunta": "¿Qué podría ocurrir si disminuye considerablemente la fotosíntesis mundial?", "respuesta": "Disminuiría la producción primaria y podría alterarse el equilibrio de gases y las cadenas alimentarias."},
                {"pregunta": "¿Cómo influye la intensidad de la luz en la fotosíntesis?", "respuesta": "Hasta cierto límite, un aumento de luz puede aumentar la velocidad fotosintética."},
                {"pregunta": "¿Qué ocurre con el dióxido de carbono durante la fotosíntesis?", "respuesta": "Es incorporado para formar compuestos orgánicos."},
                {"pregunta": "¿Por qué la fotosíntesis es considerada un proceso fundamental?", "respuesta": "Porque transforma energía luminosa en energía química almacenada en materia orgánica."},
                {"pregunta": "¿Qué relación existe entre fotosíntesis y respiración celular?", "respuesta": "La fotosíntesis produce glucosa y oxígeno, mientras la respiración celular utiliza estos productos para obtener energía."},
                {"pregunta": "¿Cómo afecta la deforestación al ciclo del carbono?", "respuesta": "Reduce la cantidad de vegetación disponible para absorber dióxido de carbono."},
                {"pregunta": "¿Qué función cumple la clorofila?", "respuesta": "Absorbe energía luminosa necesaria para la fotosíntesis."},
                {"pregunta": "¿Por qué las plantas son productores?", "respuesta": "Porque producen materia orgánica a partir de sustancias inorgánicas utilizando energía luminosa."}
            ]
        },

        "Física": {

            "Fácil": [
                {"pregunta": "¿Cuál es la unidad de fuerza?", "respuesta": "Newton."},
                {"pregunta": "¿Cuál es la unidad de masa?", "respuesta": "Kilogramo."},
                {"pregunta": "¿Cuál es la unidad de tiempo?", "respuesta": "Segundo."},
                {"pregunta": "¿Qué instrumento mide la temperatura?", "respuesta": "Termómetro."},
                {"pregunta": "¿Qué instrumento mide la masa?", "respuesta": "Balanza."},
                {"pregunta": "¿Qué instrumento mide la fuerza?", "respuesta": "Dinamómetro."},
                {"pregunta": "¿Cuál es la unidad de distancia en el SI?", "respuesta": "Metro."},
                {"pregunta": "¿Qué es el movimiento?", "respuesta": "Es el cambio de posición de un cuerpo respecto a un sistema de referencia."},
                {"pregunta": "¿Qué es la velocidad?", "respuesta": "Es una magnitud que relaciona el desplazamiento con el tiempo."},
                {"pregunta": "¿Qué es una fuerza?", "respuesta": "Es una interacción capaz de modificar el movimiento o deformar un cuerpo."}
            ],

            "Medio": [
                {"pregunta": "¿Cuál es la fórmula de la velocidad?", "respuesta": "v = d/t."},
                {"pregunta": "Un automóvil recorre 100 km en 2 horas. ¿Cuál es su velocidad promedio?", "respuesta": "50 km/h."},
                {"pregunta": "¿Qué es la aceleración?", "respuesta": "Es el cambio de la velocidad respecto al tiempo."},
                {"pregunta": "¿Qué ocurre si aumenta la fuerza y la masa permanece constante?", "respuesta": "La aceleración aumenta."},
                {"pregunta": "¿Cuál es la fórmula de la fuerza?", "respuesta": "F = m × a."},
                {"pregunta": "¿Qué ocurre con la velocidad si aumenta la distancia recorrida en el mismo tiempo?", "respuesta": "La velocidad aumenta."},
                {"pregunta": "Un ciclista recorre 60 km en 3 horas. ¿Cuál es su velocidad promedio?", "respuesta": "20 km/h."},
                {"pregunta": "¿Qué es la masa?", "respuesta": "Es la cantidad de materia de un cuerpo."},
                {"pregunta": "¿Qué es el peso?", "respuesta": "Es la fuerza con que la gravedad atrae a un cuerpo."},
                {"pregunta": "¿Qué sucede cuando una fuerza neta actúa sobre un objeto?", "respuesta": "Puede cambiar su movimiento o producir una aceleración."}
            ],

            "Difícil": [
                {"pregunta": "¿Qué establece la segunda ley de Newton?", "respuesta": "F = m × a."},
                {"pregunta": "Un objeto de 5 kg recibe una fuerza de 20 N. ¿Cuál es su aceleración?", "respuesta": "4 m/s²."},
                {"pregunta": "Un cuerpo de 10 kg acelera a 3 m/s². ¿Qué fuerza neta actúa sobre él?", "respuesta": "30 N."},
                {"pregunta": "Si una fuerza de 50 N actúa sobre una masa de 10 kg, ¿cuál es su aceleración?", "respuesta": "5 m/s²."},
                {"pregunta": "¿Qué ocurre con la aceleración si se duplica la masa y la fuerza permanece igual?", "respuesta": "La aceleración se reduce a la mitad."},
                {"pregunta": "¿Qué ocurre con la aceleración si se duplica la fuerza y la masa permanece igual?", "respuesta": "La aceleración se duplica."},
                {"pregunta": "¿Qué significa que la fuerza neta sea cero?", "respuesta": "Que no existe aceleración neta; el cuerpo puede permanecer en reposo o moverse con velocidad constante."},
                {"pregunta": "¿Qué diferencia existe entre masa y peso?", "respuesta": "La masa es cantidad de materia; el peso es una fuerza causada por la gravedad."},
                {"pregunta": "¿Por qué un objeto cae hacia la Tierra?", "respuesta": "Por la fuerza gravitatoria que ejerce la Tierra sobre él."},
                {"pregunta": "¿Qué relación existe entre fuerza, masa y aceleración?", "respuesta": "La aceleración aumenta con la fuerza neta y disminuye cuando aumenta la masa."}
            ]
        },

        "Química": {

            "Fácil": [
                {"pregunta": "¿Cuál es el símbolo del oxígeno?", "respuesta": "O."},
                {"pregunta": "¿Cuál es el símbolo del hidrógeno?", "respuesta": "H."},
                {"pregunta": "¿Cuál es el símbolo del carbono?", "respuesta": "C."},
                {"pregunta": "¿Cuál es el símbolo del sodio?", "respuesta": "Na."},
                {"pregunta": "¿Cuál es el símbolo del hierro?", "respuesta": "Fe."},
                {"pregunta": "¿Cuál es el símbolo del oro?", "respuesta": "Au."},
                {"pregunta": "¿Cuál es el símbolo de la plata?", "respuesta": "Ag."},
                {"pregunta": "¿Qué partícula tiene carga negativa?", "respuesta": "Electrón."},
                {"pregunta": "¿Qué partícula tiene carga positiva?", "respuesta": "Protón."},
                {"pregunta": "¿Qué partícula no tiene carga eléctrica?", "respuesta": "Neutrón."}
            ],

            "Medio": [
                {"pregunta": "¿Qué es un átomo?", "respuesta": "Es la unidad básica de un elemento químico."},
                {"pregunta": "¿Qué partículas están en el núcleo?", "respuesta": "Protones y neutrones."},
                {"pregunta": "¿Qué partícula tiene carga negativa?", "respuesta": "Electrón."},
                {"pregunta": "¿Qué partícula tiene carga positiva?", "respuesta": "Protón."},
                {"pregunta": "¿Qué indica el número atómico?", "respuesta": "La cantidad de protones del núcleo."},
                {"pregunta": "¿Qué es un elemento químico?", "respuesta": "Una sustancia formada por átomos con el mismo número de protones."},
                {"pregunta": "¿Qué es una molécula?", "respuesta": "Es una agrupación de átomos unidos químicamente."},
                {"pregunta": "¿Qué es un compuesto?", "respuesta": "Es una sustancia formada por elementos diferentes unidos químicamente."},
                {"pregunta": "¿Qué es una reacción química?", "respuesta": "Es un proceso en el que unas sustancias se transforman en otras."},
                {"pregunta": "¿Qué representa una fórmula química?", "respuesta": "La composición de una sustancia mediante símbolos y números."}
            ],

            "Difícil": [
                {"pregunta": "¿Cuál es la diferencia entre elemento y compuesto?", "respuesta": "Un elemento tiene un solo tipo de átomo; un compuesto contiene elementos diferentes unidos químicamente."},
                {"pregunta": "¿Qué indica el número atómico?", "respuesta": "La cantidad de protones del núcleo."},
                {"pregunta": "¿Qué diferencia existe entre cambio físico y químico?", "respuesta": "En el físico no se forma una sustancia nueva; en el químico sí."},
                {"pregunta": "¿Qué son los isótopos?", "respuesta": "Átomos del mismo elemento que tienen igual número de protones y diferente número de neutrones."},
                {"pregunta": "¿Qué ocurre con los átomos durante una reacción química?", "respuesta": "Se reorganizan para formar nuevas sustancias."},
                {"pregunta": "¿Qué es un ion?", "respuesta": "Es un átomo o grupo de átomos que posee carga eléctrica por ganar o perder electrones."},
                {"pregunta": "¿Qué es la valencia de un elemento?", "respuesta": "Es una medida de su capacidad de combinación química."},
                {"pregunta": "¿Qué función cumple la tabla periódica?", "respuesta": "Organiza los elementos químicos según sus propiedades y número atómico."},
                {"pregunta": "¿Qué diferencia existe entre reactivos y productos?", "respuesta": "Los reactivos son las sustancias iniciales y los productos son las sustancias formadas."},
                {"pregunta": "¿Por qué se deben balancear las ecuaciones químicas?", "respuesta": "Para cumplir la conservación de la materia, manteniendo igual cantidad de átomos de cada elemento."}
            ]
        }
    },


    # ======================================================
    # HISTORIA
    # ======================================================

    "Historia": {

        "Independencia del Perú": {

            "Fácil": [
                {"pregunta": "¿En qué año se proclamó la Independencia del Perú?", "respuesta": "1821."},
                {"pregunta": "¿Quién proclamó la Independencia del Perú?", "respuesta": "José de San Martín."},
                {"pregunta": "¿Dónde se proclamó la Independencia?", "respuesta": "En Lima."},
                {"pregunta": "¿En qué año ocurrió la batalla de Ayacucho?", "respuesta": "1824."},
                {"pregunta": "¿Quién fue José de San Martín?", "respuesta": "Un líder de las campañas independentistas sudamericanas."},
                {"pregunta": "¿Quién fue Simón Bolívar?", "respuesta": "Un líder independentista que participó en la consolidación de la independencia sudamericana."},
                {"pregunta": "¿Qué batalla fue decisiva para consolidar la independencia peruana?", "respuesta": "La batalla de Ayacucho."},
                {"pregunta": "¿Qué proceso buscaba terminar con el dominio español?", "respuesta": "El proceso de independencia."},
                {"pregunta": "¿En qué continente se desarrolló la independencia del Perú?", "respuesta": "América del Sur."},
                {"pregunta": "¿Qué país europeo dominaba el Perú antes de la independencia?", "respuesta": "España."}
            ],

            "Medio": [
                {"pregunta": "¿Por qué la proclamación de 1821 no terminó inmediatamente la guerra?", "respuesta": "Porque las fuerzas realistas todavía controlaban territorios importantes."},
                {"pregunta": "¿Qué importancia tuvo la batalla de Ayacucho?", "respuesta": "Contribuyó decisivamente a consolidar la independencia del Perú."},
                {"pregunta": "¿Qué campaña dirigió San Martín en el Perú?", "respuesta": "La campaña libertadora del Perú."},
                {"pregunta": "¿Qué líder ayudó a consolidar la independencia después de San Martín?", "respuesta": "Simón Bolívar."},
                {"pregunta": "¿Qué factores favorecieron la independencia?", "respuesta": "Ideas ilustradas, crisis de la monarquía española, conflictos coloniales y campañas militares."},
                {"pregunta": "¿Qué eran las fuerzas realistas?", "respuesta": "Las fuerzas que defendían el dominio de la monarquía española."},
                {"pregunta": "¿Qué eran las fuerzas patriotas?", "respuesta": "Las fuerzas que apoyaban la independencia."},
                {"pregunta": "¿Por qué Lima era importante durante la independencia?", "respuesta": "Era el centro político y administrativo del poder colonial español en el Perú."},
                {"pregunta": "¿Qué consecuencia política tuvo la independencia?", "respuesta": "El Perú inició la construcción de un Estado republicano."},
                {"pregunta": "¿Qué dificultad enfrentó el Perú después de independizarse?", "respuesta": "La inestabilidad política, problemas económicos y debilidad institucional."}
            ],

            "Difícil": [
                {"pregunta": "¿Por qué la independencia fue un proceso y no un acontecimiento aislado?", "respuesta": "Porque involucró conflictos políticos, sociales y militares desarrollados durante varios años."},
                {"pregunta": "¿Qué factores internos y externos favorecieron la independencia?", "respuesta": "Crisis colonial, ideas ilustradas, revoluciones atlánticas y campañas militares."},
                {"pregunta": "¿Por qué fue importante Ayacucho?", "respuesta": "Porque debilitó decisivamente el poder militar español y contribuyó a consolidar la independencia."},
                {"pregunta": "¿Qué dificultades tuvo el Perú al iniciar la República?", "respuesta": "Problemas económicos, conflictos políticos, instituciones débiles y disputas por el poder."},
                {"pregunta": "¿Cómo influyó la crisis de España en la independencia americana?", "respuesta": "Debilitó el control de la monarquía y favoreció los movimientos autonomistas e independentistas."},
                {"pregunta": "¿Qué papel tuvieron los ejércitos libertadores?", "respuesta": "Contribuyeron militarmente a derrotar a las fuerzas realistas."},
                {"pregunta": "¿Qué relación existió entre independencia y construcción republicana?", "respuesta": "La independencia permitió iniciar la formación de un Estado propio, aunque la consolidación republicana fue posterior y conflictiva."},
                {"pregunta": "¿Por qué la independencia no solucionó inmediatamente los problemas sociales?", "respuesta": "Porque muchas estructuras sociales y económicas heredadas de la colonia continuaron después de 1821."},
                {"pregunta": "¿Qué cambio político produjo la independencia?", "respuesta": "Se pasó del gobierno colonial a la formación de una República independiente."},
                {"pregunta": "¿Por qué el periodo posterior a la independencia fue políticamente inestable?", "respuesta": "Por las disputas entre grupos políticos y militares y la debilidad de las nuevas instituciones."}
            ]
        },

        "Caudillismo": {

            "Fácil": [
                {"pregunta": "¿Qué fue el caudillismo?", "respuesta": "Un fenómeno político caracterizado por el protagonismo de líderes, especialmente militares."},
                {"pregunta": "¿Cuándo tuvo gran importancia el caudillismo peruano?", "respuesta": "Durante las primeras décadas de la República."},
                {"pregunta": "¿Quiénes protagonizaron el caudillismo?", "respuesta": "Principalmente líderes militares y políticos."},
                {"pregunta": "¿Qué problema favoreció el caudillismo?", "respuesta": "La debilidad de las instituciones republicanas."},
                {"pregunta": "¿Qué provocaba la lucha entre caudillos?", "respuesta": "Conflictos y cambios frecuentes de gobierno."},
                {"pregunta": "¿Qué tipo de líderes fueron importantes durante el caudillismo?", "respuesta": "Líderes militares."},
                {"pregunta": "¿Qué institución política estaba en proceso de formación?", "respuesta": "La República peruana."},
                {"pregunta": "¿Qué característica tuvo la política de las primeras décadas republicanas?", "respuesta": "Inestabilidad política."},
                {"pregunta": "¿Qué buscaban muchos caudillos?", "respuesta": "Obtener influencia y poder político."},
                {"pregunta": "¿Qué problema económico heredó la República?", "respuesta": "Una economía debilitada y con dificultades fiscales."}
            ],

            "Medio": [
                {"pregunta": "¿Por qué surgió el caudillismo después de la independencia?", "respuesta": "Por la debilidad institucional, conflictos políticos y protagonismo militar."},
                {"pregunta": "¿Cómo afectó el caudillismo a la estabilidad política?", "respuesta": "Generó conflictos por el poder y frecuentes cambios de gobierno."},
                {"pregunta": "¿Qué problema institucional favoreció el caudillismo?", "respuesta": "La debilidad de las instituciones republicanas."},
                {"pregunta": "¿Qué relación existía entre ejército y política?", "respuesta": "Los militares tuvieron una participación importante en las luchas por el poder."},
                {"pregunta": "¿Qué consecuencia tuvo la inestabilidad política?", "respuesta": "Dificultó la consolidación de instituciones republicanas estables."},
                {"pregunta": "¿Por qué la economía influyó en la política republicana?", "respuesta": "Los problemas fiscales y económicos limitaron la capacidad del nuevo Estado."},
                {"pregunta": "¿Qué grupos competían por el poder?", "respuesta": "Diversos grupos políticos y militares."},
                {"pregunta": "¿Cómo afectaban los cambios frecuentes de gobierno?", "respuesta": "Dificultaban la continuidad de políticas e instituciones."},
                {"pregunta": "¿Qué importancia tuvo el liderazgo militar?", "respuesta": "Los militares contaban con poder e influencia debido a su papel en las guerras de independencia."},
                {"pregunta": "¿Qué dificultad enfrentó la República para consolidarse?", "respuesta": "La construcción de instituciones políticas estables."}
            ],

            "Difícil": [
                {"pregunta": "¿Qué relación existió entre debilidad institucional y caudillismo?", "respuesta": "La debilidad institucional facilitó que líderes militares y políticos adquirieran gran influencia."},
                {"pregunta": "¿Por qué el caudillismo dificultó la consolidación republicana?", "respuesta": "Porque los conflictos por el poder y los cambios de gobierno afectaron la estabilidad institucional."},
                {"pregunta": "¿Cómo influyeron los problemas económicos en el caudillismo?", "respuesta": "Las dificultades fiscales generaron conflictos sobre los recursos y limitaron la capacidad del Estado."},
                {"pregunta": "¿Por qué los militares tuvieron tanto protagonismo político?", "respuesta": "Porque habían adquirido experiencia, prestigio y poder durante las guerras de independencia."},
                {"pregunta": "¿Qué relación hubo entre inestabilidad política y desarrollo institucional?", "respuesta": "Los cambios constantes de gobierno dificultaron la consolidación de instituciones duraderas."},
                {"pregunta": "¿Por qué la formación de la República fue conflictiva?", "respuesta": "Porque distintos grupos tenían proyectos e intereses diferentes sobre la organización del nuevo Estado."},
                {"pregunta": "¿Qué efectos tuvo el caudillismo en la gobernabilidad?", "respuesta": "Generó periodos de inestabilidad y dificultó la continuidad de las políticas públicas."},
                {"pregunta": "¿Cómo puede explicarse el poder de los caudillos?", "respuesta": "Por el prestigio militar, las redes de apoyo y la debilidad de las instituciones."},
                {"pregunta": "¿Por qué el caudillismo no fue únicamente un fenómeno militar?", "respuesta": "Porque también involucró disputas políticas, económicas y sociales por el control del Estado."},
                {"pregunta": "¿Qué problema de fondo refleja el caudillismo?", "respuesta": "La dificultad inicial para establecer instituciones republicanas estables y reglas políticas aceptadas."}
            ]
        },

        "Guerra del Pacífico": {

            "Fácil": [
                {"pregunta": "¿Cuándo comenzó la Guerra del Pacífico?", "respuesta": "1879."},
                {"pregunta": "¿Qué países participaron principalmente?", "respuesta": "Chile, Perú y Bolivia."},
                {"pregunta": "¿Contra quién combatieron Perú y Bolivia?", "respuesta": "Contra Chile."},
                {"pregunta": "¿Qué recurso estuvo relacionado con las disputas económicas?", "respuesta": "El salitre."},
                {"pregunta": "¿En qué año terminó la guerra para el Perú?", "respuesta": "1883."},
                {"pregunta": "¿Qué tratado puso fin a la guerra entre Perú y Chile?", "respuesta": "El Tratado de Ancón."},
                {"pregunta": "¿Qué país ocupó Lima durante la guerra?", "respuesta": "Chile."},
                {"pregunta": "¿Qué territorio peruano fue cedido a Chile mediante el Tratado de Ancón?", "respuesta": "Tarapacá."},
                {"pregunta": "¿Qué país perdió su litoral durante la guerra?", "respuesta": "Bolivia."},
                {"pregunta": "¿Qué tipo de conflicto fue la Guerra del Pacífico?", "respuesta": "Un conflicto armado entre Chile y la alianza de Perú y Bolivia."}
            ],

            "Medio": [
                {"pregunta": "¿Qué consecuencias tuvo la guerra para el Perú?", "respuesta": "Pérdidas territoriales, daños económicos, destrucción y crisis política y social."},
                {"pregunta": "¿Qué recurso fue fundamental en las disputas económicas?", "respuesta": "El salitre."},
                {"pregunta": "¿Qué importancia tuvo la ocupación de Lima?", "respuesta": "Representó un duro golpe militar y político para el Perú."},
                {"pregunta": "¿Qué tratado terminó la guerra entre Perú y Chile?", "respuesta": "El Tratado de Ancón de 1883."},
                {"pregunta": "¿Cómo afectó la guerra a la infraestructura?", "respuesta": "Provocó destrucción y daños en diversas instalaciones productivas y de transporte."},
                {"pregunta": "¿Cómo afectó la guerra a la economía?", "respuesta": "Generó pérdidas productivas, destrucción y mayores dificultades financieras."},
                {"pregunta": "¿Qué ocurrió con Bolivia después de la guerra?", "respuesta": "Perdió su salida soberana al océano Pacífico."},
                {"pregunta": "¿Por qué el salitre era importante?", "respuesta": "Era un recurso de gran valor económico utilizado principalmente como fertilizante y para producir explosivos."},
                {"pregunta": "¿Qué etapa siguió al final de la guerra?", "respuesta": "Un periodo de reconstrucción y reorganización política y económica."},
                {"pregunta": "¿Qué impacto social tuvo la guerra?", "respuesta": "Provocó pérdidas humanas, desplazamientos y dificultades para la población."}
            ],

            "Difícil": [
                {"pregunta": "¿Cómo afectó la Guerra del Pacífico a la economía peruana?", "respuesta": "Provocó destrucción de infraestructura, pérdidas productivas, endeudamiento y dificultades para la recuperación."},
                {"pregunta": "¿Qué consecuencias políticas produjo la guerra?", "respuesta": "Generó inestabilidad política, conflictos internos y dificultades para reconstruir el Estado."},
                {"pregunta": "¿Cómo influyeron los recursos naturales en el conflicto?", "respuesta": "El control y los intereses económicos relacionados con recursos como el salitre fueron factores importantes en las tensiones."},
                {"pregunta": "¿Por qué la reconstrucción fue difícil después de la guerra?", "respuesta": "Porque el país quedó con graves daños económicos, sociales, territoriales y políticos."},
                {"pregunta": "¿Qué relación existió entre guerra y crisis económica?", "respuesta": "La guerra destruyó recursos e infraestructura y aumentó las dificultades financieras del Estado."},
                {"pregunta": "¿Cómo afectó la guerra al Estado peruano?", "respuesta": "Debilitó sus finanzas, instituciones e infraestructura y generó una etapa de reconstrucción."},
                {"pregunta": "¿Por qué la ocupación de Lima tuvo importancia política?", "respuesta": "Porque mostró la superioridad militar chilena y afectó el funcionamiento del gobierno peruano."},
                {"pregunta": "¿Qué importancia tuvo el Tratado de Ancón?", "respuesta": "Formalizó el fin de la guerra entre Perú y Chile y estableció condiciones territoriales."},
                {"pregunta": "¿Qué desafíos enfrentó el Perú después de 1883?", "respuesta": "Reconstruir la economía, infraestructura, instituciones y estabilidad política."},
                {"pregunta": "¿Cómo puede analizarse la guerra desde una perspectiva económica?", "respuesta": "Considerando los intereses sobre recursos, las finanzas estatales, la destrucción productiva y los costos de la guerra."}
            ]
        }
    },


    # ======================================================
    # COMUNICACIÓN
    # ======================================================

    "Comunicación": {

        "Comprensión lectora": {

            "Fácil": [
                {"pregunta": "¿Qué es la idea principal?", "respuesta": "Es la información central de un texto."},
                {"pregunta": "¿Qué es el tema?", "respuesta": "Es aquello de lo que trata principalmente un texto."},
                {"pregunta": "¿Qué es un texto?", "respuesta": "Es una unidad organizada de comunicación."},
                {"pregunta": "¿Qué es un párrafo?", "respuesta": "Es un conjunto de oraciones que desarrolla una idea relacionada."},
                {"pregunta": "¿Qué es un título?", "respuesta": "Es el nombre que identifica el contenido de un texto."},
                {"pregunta": "¿Qué es un resumen?", "respuesta": "Es una síntesis de las ideas principales de un texto."},
                {"pregunta": "¿Qué es un personaje?", "respuesta": "Es quien participa en los hechos de una narración."},
                {"pregunta": "¿Qué es el argumento?", "respuesta": "Es el conjunto de hechos principales de una obra o narración."},
                {"pregunta": "¿Qué es una fuente de información?", "respuesta": "Es un recurso del que se obtiene información."},
                {"pregunta": "¿Qué significa comprender un texto?", "respuesta": "Entender e interpretar la información que presenta."}
            ],

            "Medio": [
                {"pregunta": "¿Qué es una inferencia?", "respuesta": "Es una conclusión obtenida a partir de información y pistas del texto."},
                {"pregunta": "¿Qué diferencia existe entre información literal e inferencial?", "respuesta": "La literal aparece directamente; la inferencial se obtiene mediante interpretación."},
                {"pregunta": "¿Qué es la intención comunicativa?", "respuesta": "Es el propósito que tiene el emisor al producir un mensaje."},
                {"pregunta": "¿Qué es una idea secundaria?", "respuesta": "Es una idea que desarrolla, explica o complementa la idea principal."},
                {"pregunta": "¿Qué función cumplen los conectores?", "respuesta": "Relacionan ideas y ayudan a organizar el texto."},
                {"pregunta": "¿Qué es el contexto?", "respuesta": "Es el conjunto de circunstancias que rodean un mensaje."},
                {"pregunta": "¿Qué es una conclusión?", "respuesta": "Es una idea final que se obtiene a partir de la información analizada."},
                {"pregunta": "¿Qué es un argumento?", "respuesta": "Es una razón utilizada para defender una idea o postura."},
                {"pregunta": "¿Qué es una opinión?", "respuesta": "Es un punto de vista personal sobre un tema."},
                {"pregunta": "¿Qué es un hecho?", "respuesta": "Es un acontecimiento que puede comprobarse mediante evidencia."}
            ],

            "Difícil": [
                {"pregunta": "¿Por qué es importante identificar la intención del autor?", "respuesta": "Porque permite comprender qué busca comunicar y cómo organiza el contenido."},
                {"pregunta": "¿Cómo se reconoce la postura del autor?", "respuesta": "Analizando sus afirmaciones, argumentos, ejemplos y posición frente al tema."},
                {"pregunta": "¿Cómo se puede inferir información que no aparece directamente?", "respuesta": "Relacionando las pistas del texto con conocimientos y razonamientos."},
                {"pregunta": "¿Por qué es importante diferenciar hechos de opiniones?", "respuesta": "Porque permite evaluar mejor la información y reconocer qué afirmaciones pueden verificarse."},
                {"pregunta": "¿Cómo influye el contexto en la comprensión de un texto?", "respuesta": "Ayuda a interpretar el significado del mensaje considerando las circunstancias en que fue producido."},
                {"pregunta": "¿Por qué los conectores ayudan a la coherencia?", "respuesta": "Porque muestran relaciones entre las ideas y facilitan la comprensión del contenido."},
                {"pregunta": "¿Cómo se puede evaluar un argumento?", "respuesta": "Analizando si presenta razones pertinentes, evidencia suficiente y relación lógica con la conclusión."},
                {"pregunta": "¿Qué importancia tiene reconocer la estructura de un texto?", "respuesta": "Permite comprender cómo se organizan y relacionan sus ideas."},
                {"pregunta": "¿Cómo se puede determinar la idea principal?", "respuesta": "Identificando la idea que resume o explica el contenido central del texto."},
                {"pregunta": "¿Por qué un lector debe cuestionar la información?", "respuesta": "Para analizar su coherencia, evidencia, intención y confiabilidad."}
            ]
        },

        "Gramática": {

            "Fácil": [
                {"pregunta": "¿Qué es un sustantivo?", "respuesta": "Es una palabra que nombra personas, animales, lugares, objetos, ideas o sentimientos."},
                {"pregunta": "¿Qué es un verbo?", "respuesta": "Es una palabra que expresa acción, estado o proceso."},
                {"pregunta": "¿Qué es un adjetivo?", "respuesta": "Es una palabra que describe o caracteriza a un sustantivo."},
                {"pregunta": "¿Qué es un pronombre?", "respuesta": "Es una palabra que puede sustituir o representar a un sustantivo."},
                {"pregunta": "¿Qué es un adverbio?", "respuesta": "Es una palabra que modifica principalmente a un verbo, adjetivo u otro adverbio."},
                {"pregunta": "¿Qué es una oración?", "respuesta": "Es una unidad de sentido completo que presenta una estructura gramatical."},
                {"pregunta": "¿Qué es el sujeto?", "respuesta": "Es el elemento del que se dice algo o que realiza la acción."},
                {"pregunta": "¿Qué es el predicado?", "respuesta": "Es la parte que expresa algo acerca del sujeto."},
                {"pregunta": "¿Qué signo se utiliza al final de una oración enunciativa?", "respuesta": "El punto."},
                {"pregunta": "¿Qué signos se usan para formular una pregunta?", "respuesta": "Los signos de interrogación: ¿ ?"}
            ],

            "Medio": [
                {"pregunta": "¿Qué función cumple principalmente un adjetivo?", "respuesta": "Describir o caracterizar a un sustantivo."},
                {"pregunta": "¿Qué es el sujeto de una oración?", "respuesta": "Es el elemento que realiza la acción o del que se dice algo."},
                {"pregunta": "¿Qué es el predicado?", "respuesta": "Es la parte de la oración que expresa algo sobre el sujeto."},
                {"pregunta": "¿Qué es un verbo transitivo?", "respuesta": "Es un verbo que puede llevar un complemento directo."},
                {"pregunta": "¿Qué es el complemento directo?", "respuesta": "Es el elemento que recibe directamente la acción de un verbo transitivo."},
                {"pregunta": "¿Qué función cumple una conjunción?", "respuesta": "Une palabras, grupos de palabras u oraciones."},
                {"pregunta": "¿Qué es una preposición?", "respuesta": "Es una palabra que establece relaciones entre elementos de una oración."},
                {"pregunta": "¿Qué es el núcleo del sujeto?", "respuesta": "Es la palabra principal del sujeto, generalmente un sustantivo o pronombre."},
                {"pregunta": "¿Qué es el núcleo del predicado?", "respuesta": "Es el verbo principal de la oración."},
                {"pregunta": "¿Qué es una oración bimembre?", "respuesta": "Es una oración que puede dividirse en sujeto y predicado."}
            ],

            "Difícil": [
                {"pregunta": "¿Qué diferencia existe entre oración simple y compuesta?", "respuesta": "La simple tiene un solo verbo conjugado como núcleo; la compuesta contiene dos o más proposiciones."},
                {"pregunta": "¿Qué función cumplen los conectores?", "respuesta": "Relacionan ideas y ayudan a organizar el texto."},
                {"pregunta": "¿Qué diferencia existe entre coordinación y subordinación?", "respuesta": "En la coordinación las proposiciones tienen relación de igualdad sintáctica; en la subordinación una depende de otra."},
                {"pregunta": "¿Qué es una proposición subordinada?", "respuesta": "Es una estructura que depende sintácticamente de otra proposición."},
                {"pregunta": "¿Qué función cumple el complemento circunstancial?", "respuesta": "Aporta información sobre circunstancias como tiempo, lugar, modo o causa."},
                {"pregunta": "¿Qué es la concordancia?", "respuesta": "Es la correspondencia gramatical entre palabras, como género y número o persona y número."},
                {"pregunta": "¿Por qué es importante la puntuación?", "respuesta": "Porque ayuda a organizar las ideas y expresar correctamente las relaciones entre ellas."},
                {"pregunta": "¿Qué diferencia existe entre lenguaje formal e informal?", "respuesta": "El formal utiliza un registro más cuidado y adecuado a situaciones académicas o profesionales; el informal es más cotidiano."},
                {"pregunta": "¿Qué es la cohesión textual?", "respuesta": "Es la conexión lingüística entre las diferentes partes de un texto."},
                {"pregunta": "¿Qué es la coherencia textual?", "respuesta": "Es la organización lógica y significativa de las ideas de un texto."}
            ]
        }
    },


    # ======================================================
    # GEOGRAFÍA
    # ======================================================

    "Geografía": {

        "Clima": {

            "Fácil": [
                {"pregunta": "¿Qué es el clima?", "respuesta": "Es el conjunto de condiciones atmosféricas características de una región durante periodos prolongados."},
                {"pregunta": "¿Qué instrumento mide la temperatura?", "respuesta": "El termómetro."},
                {"pregunta": "¿Qué instrumento mide la presión atmosférica?", "respuesta": "El barómetro."},
                {"pregunta": "¿Qué instrumento mide la velocidad del viento?", "respuesta": "El anemómetro."},
                {"pregunta": "¿Qué instrumento mide la humedad?", "respuesta": "El higrómetro."},
                {"pregunta": "¿Qué es la precipitación?", "respuesta": "Es la caída de agua desde la atmósfera hacia la superficie terrestre."},
                {"pregunta": "¿Qué es el viento?", "respuesta": "Es el movimiento del aire."},
                {"pregunta": "¿Qué es la temperatura?", "respuesta": "Es una medida relacionada con el grado de calor o frío del aire."},
                {"pregunta": "¿Qué es la humedad?", "respuesta": "Es la cantidad de vapor de agua presente en el aire."},
                {"pregunta": "¿Qué es el tiempo atmosférico?", "respuesta": "Es el estado de la atmósfera en un lugar y momento determinados."}
            ],

            "Medio": [
                {"pregunta": "¿Cuál es la diferencia entre tiempo y clima?", "respuesta": "El tiempo describe condiciones atmosféricas momentáneas; el clima estudia patrones durante largos periodos."},
                {"pregunta": "¿Qué factores influyen en el clima?", "respuesta": "Latitud, altitud, relieve, distancia al mar y corrientes marinas, entre otros."},
                {"pregunta": "¿Cómo influye la altitud?", "respuesta": "Generalmente, al aumentar la altitud disminuye la temperatura."},
                {"pregunta": "¿Cómo influyen las corrientes marinas?", "respuesta": "Pueden modificar la temperatura y humedad de las regiones costeras."},
                {"pregunta": "¿Qué importancia tiene la latitud?", "respuesta": "Influye en la cantidad de radiación solar recibida."},
                {"pregunta": "¿Cómo influye el relieve?", "respuesta": "Puede modificar la circulación del aire y la distribución de las precipitaciones."},
                {"pregunta": "¿Qué es una región climática?", "respuesta": "Es un área que presenta características climáticas similares."},
                {"pregunta": "¿Qué relación existe entre temperatura y altitud?", "respuesta": "En general, la temperatura disminuye al aumentar la altitud."},
                {"pregunta": "¿Por qué las zonas cercanas al mar pueden tener temperaturas más moderadas?", "respuesta": "Porque el agua del mar cambia de temperatura más lentamente que la tierra."},
                {"pregunta": "¿Qué importancia tiene estudiar el clima?", "respuesta": "Ayuda a comprender condiciones ambientales y planificar actividades humanas."}
            ],

            "Difícil": [
                {"pregunta": "¿Cómo influye la altitud en el clima?", "respuesta": "Generalmente disminuye la temperatura y cambian las condiciones atmosféricas."},
                {"pregunta": "¿Cómo influyen las corrientes marinas?", "respuesta": "Pueden transportar calor o frío y modificar las condiciones climáticas de las costas."},
                {"pregunta": "¿Cómo influye el relieve en las precipitaciones?", "respuesta": "Las montañas pueden obligar al aire húmedo a ascender, favoreciendo precipitaciones en ciertas zonas."},
                {"pregunta": "¿Por qué la latitud modifica el clima?", "respuesta": "Porque determina el ángulo y cantidad de radiación solar que recibe una región."},
                {"pregunta": "¿Cómo afecta la distancia al mar?", "respuesta": "Las zonas costeras suelen tener menor amplitud térmica que las zonas interiores."},
                {"pregunta": "¿Qué relación existe entre clima y actividades humanas?", "respuesta": "El clima influye en agricultura, disponibilidad de agua, transporte, vivienda y otras actividades."},
                {"pregunta": "¿Por qué dos lugares de igual latitud pueden tener climas diferentes?", "respuesta": "Porque también intervienen altitud, relieve, corrientes marinas y distancia al mar."},
                {"pregunta": "¿Cómo influye la vegetación en el clima local?", "respuesta": "Puede modificar humedad, temperatura y circulación de agua y energía en la superficie."},
                {"pregunta": "¿Por qué el clima es importante para la agricultura?", "respuesta": "Porque determina condiciones como temperatura, precipitaciones y disponibilidad de agua."},
                {"pregunta": "¿Cómo puede afectar el cambio climático al clima regional?", "respuesta": "Puede modificar temperaturas, precipitaciones y frecuencia de determinados eventos extremos."}
            ]
        },

        "Cambio climático": {

            "Fácil": [
                {"pregunta": "¿Qué es el cambio climático?", "respuesta": "Es una modificación significativa y prolongada de los patrones climáticos."},
                {"pregunta": "¿Qué gas se emite en grandes cantidades al quemar combustibles fósiles?", "respuesta": "Dióxido de carbono."},
                {"pregunta": "¿Qué es la deforestación?", "respuesta": "Es la pérdida o eliminación de bosques."},
                {"pregunta": "¿Qué es el calentamiento global?", "respuesta": "Es el aumento a largo plazo de la temperatura media del sistema climático terrestre."},
                {"pregunta": "¿Qué son los gases de efecto invernadero?", "respuesta": "Son gases atmosféricos que retienen parte del calor terrestre."},
                {"pregunta": "¿Qué es una fuente de energía renovable?", "respuesta": "Es una fuente que se regenera naturalmente a escala humana."},
                {"pregunta": "¿Qué es la reforestación?", "respuesta": "Es la recuperación o establecimiento de árboles en áreas donde se han perdido bosques."},
                {"pregunta": "¿Qué es una sequía?", "respuesta": "Es un periodo prolongado con precipitaciones inferiores a las normales."},
                {"pregunta": "¿Qué es una inundación?", "respuesta": "Es la ocupación temporal de áreas por agua que normalmente no están cubiertas."},
                {"pregunta": "¿Qué fuente renovable utiliza la radiación del Sol?", "respuesta": "La energía solar."}
            ],

            "Medio": [
                {"pregunta": "¿Qué actividades humanas contribuyen al cambio climático?", "respuesta": "Quema de combustibles fósiles, deforestación y algunas actividades industriales y agropecuarias."},
                {"pregunta": "¿Qué es el efecto invernadero?", "respuesta": "Es un fenómeno natural en el que ciertos gases retienen parte del calor terrestre."},
                {"pregunta": "¿Qué acciones ayudan a reducir emisiones?", "respuesta": "Usar energías renovables, mejorar la eficiencia energética y proteger bosques."},
                {"pregunta": "¿Qué importancia tiene la reforestación?", "respuesta": "Ayuda a recuperar ecosistemas y aumentar la absorción de dióxido de carbono."},
                {"pregunta": "¿Qué es la adaptación al cambio climático?", "respuesta": "Es el proceso de ajustar sistemas y comunidades para reducir los impactos del cambio climático."},
                {"pregunta": "¿Qué es la mitigación?", "respuesta": "Son acciones destinadas a reducir las emisiones o aumentar la absorción de gases de efecto invernadero."},
                {"pregunta": "¿Cómo contribuye el transporte al cambio climático?", "respuesta": "Principalmente mediante emisiones generadas por el uso de combustibles fósiles."},
                {"pregunta": "¿Cómo puede ayudar la energía solar?", "respuesta": "Puede producir electricidad sin quemar combustibles fósiles durante su generación."},
                {"pregunta": "¿Por qué los bosques son importantes?", "respuesta": "Almacenan carbono, conservan biodiversidad y contribuyen al ciclo del agua."},
                {"pregunta": "¿Qué relación existe entre consumo de energía y emisiones?", "respuesta": "El uso de combustibles fósiles para producir energía genera emisiones de gases de efecto invernadero."}
            ],

            "Difícil": [
                {"pregunta": "¿Cómo contribuye la deforestación al cambio climático?", "respuesta": "Reduce la absorción de CO₂ y puede liberar carbono almacenado en vegetación y suelos."},
                {"pregunta": "¿Cuál es la diferencia entre mitigación y adaptación?", "respuesta": "La mitigación reduce las causas o emisiones; la adaptación reduce la vulnerabilidad frente a los impactos."},
                {"pregunta": "¿Cómo puede la conservación de bosques contribuir a reducir emisiones?", "respuesta": "Mantiene almacenado el carbono y conserva la capacidad de los ecosistemas para absorber CO₂."},
                {"pregunta": "¿Por qué las energías renovables pueden ayudar frente al cambio climático?", "respuesta": "Permiten producir energía con menores emisiones directas de gases de efecto invernadero que los combustibles fósiles."},
                {"pregunta": "¿Cómo pueden las ciudades adaptarse al cambio climático?", "respuesta": "Mediante planificación urbana, infraestructura resistente, áreas verdes y sistemas de prevención."},
                {"pregunta": "¿Por qué el cambio climático puede afectar la disponibilidad de agua?", "respuesta": "Porque puede modificar patrones de precipitación, evaporación, glaciares y sequías."},
                {"pregunta": "¿Cómo afecta el cambio climático a los ecosistemas?", "respuesta": "Puede modificar temperaturas y disponibilidad de agua y alterar la distribución de especies."},
                {"pregunta": "¿Qué relación existe entre cambio climático y biodiversidad?", "respuesta": "Los cambios ambientales pueden alterar hábitats y aumentar la presión sobre determinadas especies."},
                {"pregunta": "¿Por qué es importante combinar mitigación y adaptación?", "respuesta": "Porque es necesario reducir las causas del cambio climático y al mismo tiempo prepararse para sus impactos."},
                {"pregunta": "¿Cómo puede una comunidad reducir su huella de carbono?", "respuesta": "Mejorando el uso de energía, utilizando transporte sostenible, reduciendo residuos y protegiendo áreas naturales."}
            ]
        }
    },


    # ======================================================
    # INGLÉS
    # ======================================================

    "Inglés": {

        "Present Simple": {

            "Fácil": [
                {"pregunta": "Completa: She ___ to school every day.", "respuesta": "goes"},
                {"pregunta": "Completa: I ___ basketball on weekends.", "respuesta": "play"},
                {"pregunta": "Completa: He ___ English every day.", "respuesta": "studies"},
                {"pregunta": "Completa: They ___ football after school.", "respuesta": "play"},
                {"pregunta": "Completa: My mother ___ coffee every morning.", "respuesta": "drinks"},
                {"pregunta": "Completa: We ___ in Peru.", "respuesta": "live"},
                {"pregunta": "Completa: Carlos ___ videogames.", "respuesta": "plays"},
                {"pregunta": "Completa: The dog ___ a lot.", "respuesta": "runs"},
                {"pregunta": "Completa: I ___ music.", "respuesta": "like"},
                {"pregunta": "Completa: She ___ English very well.", "respuesta": "speaks"}
            ],

            "Medio": [
                {"pregunta": "Transforma a pregunta: You like music.", "respuesta": "Do you like music?"},
                {"pregunta": "Completa: He ___ (study) English every afternoon.", "respuesta": "studies"},
                {"pregunta": "Transforma a negativo: I like pizza.", "respuesta": "I don't like pizza."},
                {"pregunta": "Completa: She ___ (watch) TV every night.", "respuesta": "watches"},
                {"pregunta": "Transforma a pregunta: She plays tennis.", "respuesta": "Does she play tennis?"},
                {"pregunta": "Completa: They ___ (go) to school by bus.", "respuesta": "go"},
                {"pregunta": "Transforma a negativo: He plays basketball.", "respuesta": "He doesn't play basketball."},
                {"pregunta": "Completa: My father ___ (work) every day.", "respuesta": "works"},
                {"pregunta": "Transforma a pregunta: They study English.", "respuesta": "Do they study English?"},
                {"pregunta": "Completa: Ana ___ (wash) her hands before eating.", "respuesta": "washes"}
            ],

            "Difícil": [
                {"pregunta": "Escribe la forma negativa: She plays tennis every Saturday.", "respuesta": "She doesn't play tennis every Saturday."},
                {"pregunta": "Transforma a pregunta: They study English.", "respuesta": "Do they study English?"},
                {"pregunta": "Completa: My brother ___ (go) to school by bus.", "respuesta": "goes"},
                {"pregunta": "Completa: The teacher ___ (teach) English.", "respuesta": "teaches"},
                {"pregunta": "Transforma a negativo: Maria studies every night.", "respuesta": "Maria doesn't study every night."},
                {"pregunta": "Transforma a pregunta: Your father works here.", "respuesta": "Does your father work here?"},
                {"pregunta": "Completa: My friends ___ (watch) movies on Fridays.", "respuesta": "watch"},
                {"pregunta": "Completa: He ___ (fix) computers.", "respuesta": "fixes"},
                {"pregunta": "Transforma a pregunta: She likes science.", "respuesta": "Does she like science?"},
                {"pregunta": "Completa: The sun ___ (rise) in the east.", "respuesta": "rises"}
            ]
        },

        "Vocabulary": {

            "Fácil": [
                {"pregunta": "¿Qué significa 'book'?", "respuesta": "Libro."},
                {"pregunta": "¿Qué significa 'school'?", "respuesta": "Escuela o colegio."},
                {"pregunta": "¿Qué significa 'house'?", "respuesta": "Casa."},
                {"pregunta": "¿Qué significa 'friend'?", "respuesta": "Amigo o amiga."},
                {"pregunta": "¿Qué significa 'water'?", "respuesta": "Agua."},
                {"pregunta": "¿Qué significa 'food'?", "respuesta": "Comida."},
                {"pregunta": "¿Qué significa 'teacher'?", "respuesta": "Profesor o profesora."},
                {"pregunta": "¿Qué significa 'student'?", "respuesta": "Estudiante."},
                {"pregunta": "¿Qué significa 'computer'?", "respuesta": "Computadora."},
                {"pregunta": "¿Qué significa 'family'?", "respuesta": "Familia."}
            ],

            "Medio": [
                {"pregunta": "¿Qué significa 'environment'?", "respuesta": "Medio ambiente."},
                {"pregunta": "¿Qué significa 'improve'?", "respuesta": "Mejorar."},
                {"pregunta": "¿Qué significa 'knowledge'?", "respuesta": "Conocimiento."},
                {"pregunta": "¿Qué significa 'challenge'?", "respuesta": "Desafío o reto."},
                {"pregunta": "¿Qué significa 'careful'?", "respuesta": "Cuidadoso."},
                {"pregunta": "¿Qué significa 'healthy'?", "respuesta": "Saludable."},
                {"pregunta": "¿Qué significa 'future'?", "respuesta": "Futuro."},
                {"pregunta": "¿Qué significa 'environmental'?", "respuesta": "Ambiental."},
                {"pregunta": "¿Qué significa 'important'?", "respuesta": "Importante."},
                {"pregunta": "¿Qué significa 'develop'?", "respuesta": "Desarrollar."}
            ],

            "Difícil": [
                {"pregunta": "¿Cuál es la diferencia entre 'say' y 'tell'?", "respuesta": "'Tell' suele indicar a quién se comunica algo, mientras 'say' se centra en lo dicho."},
                {"pregunta": "¿Cuál es la diferencia entre 'borrow' y 'lend'?", "respuesta": "'Borrow' es pedir prestado y 'lend' es prestar."},
                {"pregunta": "¿Qué significa 'although'?", "respuesta": "Aunque."},
                {"pregunta": "¿Qué significa 'however'?", "respuesta": "Sin embargo."},
                {"pregunta": "¿Qué significa 'therefore'?", "respuesta": "Por lo tanto."},
                {"pregunta": "¿Qué significa 'achievement'?", "respuesta": "Logro."},
                {"pregunta": "¿Qué significa 'opportunity'?", "respuesta": "Oportunidad."},
                {"pregunta": "¿Qué significa 'responsibility'?", "respuesta": "Responsabilidad."},
                {"pregunta": "¿Qué significa 'awareness'?", "respuesta": "Conciencia o conocimiento sobre algo."},
                {"pregunta": "¿Qué significa 'solution'?", "respuesta": "Solución."}
            ]
        }
    },


    # ======================================================
    # BIOLOGÍA
    # ======================================================

    "Biología": {

        "Célula": {

            "Fácil": [
                {"pregunta": "¿Cuál es la unidad básica de los seres vivos?", "respuesta": "La célula."},
                {"pregunta": "¿Qué organelo controla gran parte de las actividades celulares?", "respuesta": "El núcleo."},
                {"pregunta": "¿Qué organelo participa en la producción de energía?", "respuesta": "La mitocondria."},
                {"pregunta": "¿Qué estructura delimita la célula?", "respuesta": "La membrana celular."},
                {"pregunta": "¿Qué organelo realiza la fotosíntesis?", "respuesta": "El cloroplasto."},
                {"pregunta": "¿Qué estructura está presente en células vegetales y les da soporte?", "respuesta": "La pared celular."},
                {"pregunta": "¿Qué contiene el núcleo?", "respuesta": "La mayor parte del material genético."},
                {"pregunta": "¿Qué estructura controla el paso de sustancias?", "respuesta": "La membrana celular."},
                {"pregunta": "¿Qué organelo produce proteínas?", "respuesta": "Los ribosomas."},
                {"pregunta": "¿Qué organelo almacena sustancias y agua en las células vegetales?", "respuesta": "La vacuola."}
            ],

            "Medio": [
                {"pregunta": "¿Cuál es la función de la mitocondria?", "respuesta": "Participa en la producción de energía para la célula."},
                {"pregunta": "¿Qué diferencia principal existe entre célula animal y vegetal?", "respuesta": "La vegetal posee pared celular y cloroplastos, entre otras características."},
                {"pregunta": "¿Cuál es la función del núcleo?", "respuesta": "Contiene material genético y participa en el control de actividades celulares."},
                {"pregunta": "¿Qué función cumple la membrana celular?", "respuesta": "Regula el intercambio de sustancias entre la célula y el medio."},
                {"pregunta": "¿Qué función tienen los ribosomas?", "respuesta": "Participan en la síntesis de proteínas."},
                {"pregunta": "¿Qué función cumple el cloroplasto?", "respuesta": "Permite realizar principalmente la fotosíntesis."},
                {"pregunta": "¿Qué es el citoplasma?", "respuesta": "Es la región celular donde se encuentran los organelos y ocurren diversas reacciones."},
                {"pregunta": "¿Qué diferencia existe entre células procariotas y eucariotas?", "respuesta": "Las eucariotas poseen núcleo definido; las procariotas no."},
                {"pregunta": "¿Por qué las células necesitan energía?", "respuesta": "Para realizar funciones como crecimiento, transporte y síntesis de sustancias."},
                {"pregunta": "¿Qué función cumple la pared celular vegetal?", "respuesta": "Brinda soporte y protección a la célula."}
            ],

            "Difícil": [
                {"pregunta": "¿Por qué la membrana celular es importante?", "respuesta": "Porque delimita la célula y regula el intercambio de sustancias."},
                {"pregunta": "¿Por qué las células necesitan energía?", "respuesta": "Para realizar procesos esenciales como transporte, síntesis y mantenimiento."},
                {"pregunta": "¿Qué diferencia existe entre transporte pasivo y activo?", "respuesta": "El pasivo no requiere energía celular directamente; el activo requiere energía."},
                {"pregunta": "¿Qué es la difusión?", "respuesta": "Es el movimiento de partículas desde una zona de mayor concentración hacia otra de menor concentración."},
                {"pregunta": "¿Qué es la ósmosis?", "respuesta": "Es el movimiento de agua a través de una membrana semipermeable."},
                {"pregunta": "¿Por qué las células tienen organelos especializados?", "respuesta": "Porque permiten realizar funciones específicas de manera organizada."},
                {"pregunta": "¿Qué relación existe entre ADN y núcleo?", "respuesta": "En las células eucariotas, el núcleo contiene la mayor parte del ADN."},
                {"pregunta": "¿Cómo se relacionan ribosomas y proteínas?", "respuesta": "Los ribosomas participan en la síntesis de proteínas a partir de información genética."},
                {"pregunta": "¿Por qué las células vegetales realizan fotosíntesis?", "respuesta": "Porque poseen cloroplastos con clorofila que captan energía luminosa."},
                {"pregunta": "¿Por qué una célula no puede crecer indefinidamente?", "respuesta": "Porque al aumentar su tamaño se dificulta mantener un intercambio eficiente de sustancias con el medio."}
            ]
        },

        "Reproducción": {

            "Fácil": [
                {"pregunta": "¿Qué es la reproducción?", "respuesta": "Es el proceso mediante el cual los seres vivos originan nuevos individuos."},
                {"pregunta": "¿Cuáles son los dos tipos principales?", "respuesta": "Asexual y sexual."},
                {"pregunta": "¿Qué son los gametos?", "respuesta": "Son células sexuales especializadas."},
                {"pregunta": "¿Qué gameto masculino participa en la reproducción humana?", "respuesta": "El espermatozoide."},
                {"pregunta": "¿Qué gameto femenino participa en la reproducción humana?", "respuesta": "El óvulo."},
                {"pregunta": "¿Qué es la fecundación?", "respuesta": "Es la unión de gametos que da origen a una nueva célula."},
                {"pregunta": "¿Qué tipo de reproducción requiere generalmente gametos?", "respuesta": "La reproducción sexual."},
                {"pregunta": "¿Qué tipo de reproducción puede ocurrir con un solo organismo?", "respuesta": "La reproducción asexual."},
                {"pregunta": "¿Qué es un cigoto?", "respuesta": "Es la célula formada después de la fecundación."},
                {"pregunta": "¿Qué proceso produce gametos?", "respuesta": "La meiosis."}
            ],

            "Medio": [
                {"pregunta": "¿Cuál es una característica de la reproducción sexual?", "respuesta": "Generalmente implica gametos y combinación de material genético."},
                {"pregunta": "¿Qué diferencia existe entre reproducción sexual y asexual?", "respuesta": "La sexual implica combinación de material genético; la asexual puede ocurrir a partir de un solo organismo."},
                {"pregunta": "¿Qué son los gametos?", "respuesta": "Células sexuales especializadas que participan en la reproducción."},
                {"pregunta": "¿Qué ocurre durante la fecundación?", "respuesta": "Se unen los gametos y se forma un cigoto."},
                {"pregunta": "¿Qué función tiene la meiosis?", "respuesta": "Produce células con la mitad del número de cromosomas, como los gametos."},
                {"pregunta": "¿Qué función tiene la mitosis?", "respuesta": "Permite crecimiento, reparación y reproducción celular en determinados organismos."},
                {"pregunta": "¿Qué ventaja puede tener la reproducción asexual?", "respuesta": "Permite producir descendencia rápidamente sin necesidad de encontrar pareja."},
                {"pregunta": "¿Qué ventaja evolutiva puede tener la reproducción sexual?", "respuesta": "Genera variabilidad genética."},
                {"pregunta": "¿Qué es la fecundación interna?", "respuesta": "Es la unión de gametos dentro del organismo."},
                {"pregunta": "¿Qué es la fecundación externa?", "respuesta": "Es la unión de gametos fuera del organismo, común en ciertos animales acuáticos."}
            ],

            "Difícil": [
                {"pregunta": "¿Por qué la reproducción sexual genera variabilidad genética?", "respuesta": "Porque combina material genético de los progenitores mediante procesos como meiosis y fecundación."},
                {"pregunta": "¿Qué importancia tiene la variabilidad genética?", "respuesta": "Favorece la capacidad de las poblaciones para responder a cambios ambientales."},
                {"pregunta": "¿Por qué la meiosis es importante para la reproducción sexual?", "respuesta": "Porque reduce a la mitad el número de cromosomas de los gametos y favorece la variabilidad genética."},
                {"pregunta": "¿Qué ocurriría si los gametos no redujeran su número de cromosomas?", "respuesta": "El número de cromosomas aumentaría en cada generación tras la fecundación."},
                {"pregunta": "¿Qué diferencia genética existe entre descendencia sexual y asexual?", "respuesta": "La sexual suele generar mayor variabilidad genética; la asexual produce descendencia genéticamente muy similar al progenitor."},
                {"pregunta": "¿Qué relación existe entre reproducción y evolución?", "respuesta": "La reproducción permite transmitir características y la variabilidad puede favorecer procesos evolutivos."},
                {"pregunta": "¿Por qué la variabilidad puede favorecer a una población?", "respuesta": "Porque algunos individuos pueden presentar características útiles ante cambios ambientales."},
                {"pregunta": "¿Qué función cumple la fecundación?", "respuesta": "Une material genético de los gametos y restablece el número diploide de cromosomas."},
                {"pregunta": "¿Qué diferencia existe entre células haploides y diploides?", "respuesta": "Las haploides tienen un solo juego de cromosomas; las diploides tienen dos."},
                {"pregunta": "¿Cómo se relacionan meiosis y fecundación?", "respuesta": "La meiosis produce gametos haploides y la fecundación los une para formar un cigoto diploide."}
            ]
        }
    },


    # ======================================================
    # COMPUTACIÓN
    # ======================================================

    "Computación": {

        "Programación": {

            "Fácil": [
                {"pregunta": "¿Qué es un algoritmo?", "respuesta": "Un conjunto ordenado de instrucciones para resolver un problema."},
                {"pregunta": "¿Qué es una variable?", "respuesta": "Un espacio o referencia utilizado para almacenar datos."},
                {"pregunta": "¿Qué es un programa?", "respuesta": "Un conjunto de instrucciones que una computadora puede ejecutar."},
                {"pregunta": "¿Qué es un lenguaje de programación?", "respuesta": "Un lenguaje utilizado para escribir instrucciones para una computadora."},
                {"pregunta": "¿Qué es un dato?", "respuesta": "Una representación de información que puede ser procesada."},
                {"pregunta": "¿Qué es una condición?", "respuesta": "Una expresión que permite tomar decisiones según se cumpla o no."},
                {"pregunta": "¿Qué es un ciclo?", "respuesta": "Una estructura que permite repetir instrucciones."},
                {"pregunta": "¿Qué es una función?", "respuesta": "Un bloque de instrucciones que realiza una tarea específica."},
                {"pregunta": "¿Qué es un error de programación?", "respuesta": "Un problema en el código que puede provocar un resultado incorrecto o impedir su ejecución."},
                {"pregunta": "¿Qué es depurar un programa?", "respuesta": "Buscar y corregir errores en el código."}
            ],

            "Medio": [
                {"pregunta": "¿Para qué sirve una condición if?", "respuesta": "Para ejecutar instrucciones cuando se cumple una condición."},
                {"pregunta": "¿Para qué sirve un ciclo for?", "respuesta": "Para repetir instrucciones recorriendo una secuencia."},
                {"pregunta": "¿Para qué sirve una función?", "respuesta": "Para agrupar instrucciones reutilizables que realizan una tarea."},
                {"pregunta": "¿Qué es un bucle while?", "respuesta": "Una estructura que repite instrucciones mientras se cumpla una condición."},
                {"pregunta": "¿Qué es una lista?", "respuesta": "Una estructura que almacena varios elementos ordenados."},
                {"pregunta": "¿Qué es una cadena de texto?", "respuesta": "Una secuencia de caracteres."},
                {"pregunta": "¿Qué es un operador?", "respuesta": "Un símbolo o palabra que permite realizar operaciones sobre datos."},
                {"pregunta": "¿Qué es una expresión lógica?", "respuesta": "Una expresión cuyo resultado puede ser verdadero o falso."},
                {"pregunta": "¿Qué es una entrada de datos?", "respuesta": "Información que recibe el programa desde el usuario u otra fuente."},
                {"pregunta": "¿Qué es una salida de datos?", "respuesta": "Información que produce o muestra el programa."}
            ],

            "Difícil": [
                {"pregunta": "¿Cuál es la diferencia entre función y variable?", "respuesta": "Una variable almacena datos; una función agrupa instrucciones para realizar una tarea."},
                {"pregunta": "¿Por qué es importante dividir un programa en funciones?", "respuesta": "Facilita la organización, reutilización, comprensión y mantenimiento del código."},
                {"pregunta": "¿Qué es la complejidad de un algoritmo?", "respuesta": "Es una forma de analizar los recursos que necesita un algoritmo según el tamaño de la entrada."},
                {"pregunta": "¿Qué significa reutilizar código?", "respuesta": "Usar nuevamente una parte del código para evitar repetir instrucciones."},
                {"pregunta": "¿Qué diferencia existe entre error de sintaxis y error lógico?", "respuesta": "El de sintaxis impide interpretar correctamente el código; el lógico produce resultados incorrectos aunque el programa pueda ejecutarse."},
                {"pregunta": "¿Por qué es importante validar los datos de entrada?", "respuesta": "Para evitar errores y asegurar que el programa reciba información válida."},
                {"pregunta": "¿Qué es una estructura de datos?", "respuesta": "Una forma de organizar y almacenar información para facilitar su procesamiento."},
                {"pregunta": "¿Qué es la abstracción en programación?", "respuesta": "Es representar los aspectos esenciales de un problema ocultando detalles innecesarios."},
                {"pregunta": "¿Qué significa modularizar un programa?", "respuesta": "Dividirlo en partes independientes y organizadas que realizan funciones específicas."},
                {"pregunta": "¿Por qué es importante documentar un programa?", "respuesta": "Ayuda a comprender, mantener y modificar el código posteriormente."}
            ]
        },

        "Python": {

            "Fácil": [
                {"pregunta": "¿Qué función muestra información en Python?", "respuesta": "print()."},
                {"pregunta": "¿Qué símbolo se utiliza para comentarios de una línea?", "respuesta": "#."},
                {"pregunta": "¿Qué función recibe información del usuario?", "respuesta": "input()."},
                {"pregunta": "¿Qué palabra crea una condición?", "respuesta": "if."},
                {"pregunta": "¿Qué palabra crea un ciclo?", "respuesta": "for o while."},
                {"pregunta": "¿Qué palabra se utiliza para definir una función?", "respuesta": "def."},
                {"pregunta": "¿Qué tipo representa True y False?", "respuesta": "bool."},
                {"pregunta": "¿Qué símbolo se usa para asignar un valor?", "respuesta": "=."},
                {"pregunta": "¿Qué tipo de dato representa texto?", "respuesta": "str."},
                {"pregunta": "¿Qué tipo de dato representa números enteros?", "respuesta": "int."}
            ],

            "Medio": [
                {"pregunta": "¿Qué hace input()?", "respuesta": "Recibe información introducida por el usuario."},
                {"pregunta": "¿Qué tipo representa True o False?", "respuesta": "Booleano (bool)."},
                {"pregunta": "¿Para qué sirve elif?", "respuesta": "Permite comprobar otra condición cuando la anterior no se cumple."},
                {"pregunta": "¿Para qué sirve else?", "respuesta": "Define las instrucciones que se ejecutan cuando ninguna condición anterior se cumple."},
                {"pregunta": "¿Para qué sirve range()?", "respuesta": "Genera una secuencia de números."},
                {"pregunta": "¿Para qué sirve len()?", "respuesta": "Devuelve la cantidad de elementos o caracteres de un objeto compatible."},
                {"pregunta": "¿Qué es una lista en Python?", "respuesta": "Una colección ordenada y modificable de elementos."},
                {"pregunta": "¿Qué es una cadena en Python?", "respuesta": "Una secuencia de caracteres de texto."},
                {"pregunta": "¿Qué hace int()?", "respuesta": "Convierte un valor compatible a un número entero."},
                {"pregunta": "¿Qué hace str()?", "respuesta": "Convierte un valor compatible a texto."}
            ],

            "Difícil": [
                {"pregunta": "¿Qué es una lista en Python?", "respuesta": "Una estructura de datos ordenada y modificable."},
                {"pregunta": "¿Qué diferencia existe entre lista y tupla?", "respuesta": "La lista puede modificarse; la tupla es inmutable."},
                {"pregunta": "¿Qué es un diccionario en Python?", "respuesta": "Una estructura que almacena pares clave-valor."},
                {"pregunta": "¿Qué es una función lambda?", "respuesta": "Una función anónima que puede escribirse de forma compacta."},
                {"pregunta": "¿Qué significa que un objeto sea mutable?", "respuesta": "Que puede modificarse después de ser creado."},
                {"pregunta": "¿Qué significa que un objeto sea inmutable?", "respuesta": "Que no puede modificarse después de ser creado."},
                {"pregunta": "¿Qué es una excepción?", "respuesta": "Un evento que ocurre durante la ejecución y puede alterar el flujo normal del programa."},
                {"pregunta": "¿Para qué sirve try-except?", "respuesta": "Para manejar excepciones y evitar que ciertos errores detengan el programa de forma inesperada."},
                {"pregunta": "¿Qué es una librería?", "respuesta": "Un conjunto de código reutilizable que proporciona funciones o herramientas."},
                {"pregunta": "¿Qué ventaja tiene utilizar funciones?", "respuesta": "Permiten organizar y reutilizar código, reduciendo repeticiones."}
            ]
        }
    },


    # ======================================================
    # EDUCACIÓN CÍVICA
    # ======================================================

    "Educación Cívica": {

        "Democracia": {

            "Fácil": [
                {"pregunta": "¿Qué es la democracia?", "respuesta": "Es un sistema político en el que la ciudadanía participa en las decisiones públicas."},
                {"pregunta": "¿Qué es el voto?", "respuesta": "Es el mecanismo mediante el cual una persona expresa su elección en un proceso electoral."},
                {"pregunta": "¿Qué son los derechos humanos?", "respuesta": "Son derechos inherentes a todas las personas que protegen su dignidad y libertad."},
                {"pregunta": "¿Qué es la ciudadanía?", "respuesta": "Es la condición que permite ejercer derechos y cumplir deberes dentro de una comunidad política."},
                {"pregunta": "¿Qué es una Constitución?", "respuesta": "Es la norma fundamental que organiza el Estado y reconoce derechos y deberes."},
                {"pregunta": "¿Qué es la participación ciudadana?", "respuesta": "Es la intervención de las personas en asuntos de interés público."},
                {"pregunta": "¿Qué es una elección?", "respuesta": "Es un proceso mediante el cual se seleccionan representantes o se toman determinadas decisiones."},
                {"pregunta": "¿Qué es una ley?", "respuesta": "Es una norma jurídica que establece reglas obligatorias."},
                {"pregunta": "¿Qué significa igualdad?", "respuesta": "Significa reconocer la misma dignidad y derechos fundamentales a las personas."},
                {"pregunta": "¿Qué es el Estado?", "respuesta": "Es la organización política y jurídica de una sociedad en un territorio determinado."}
            ],

            "Medio": [
                {"pregunta": "¿Por qué es importante la participación ciudadana?", "respuesta": "Permite intervenir en asuntos públicos y contribuir a la vida democrática."},
                {"pregunta": "¿Qué significa igualdad ante la ley?", "respuesta": "Que las personas deben recibir el mismo reconocimiento y protección jurídica sin discriminación arbitraria."},
                {"pregunta": "¿Qué función cumple una Constitución?", "respuesta": "Organiza el Estado y establece derechos, deberes y reglas fundamentales."},
                {"pregunta": "¿Qué son los deberes ciudadanos?", "respuesta": "Son responsabilidades que las personas deben cumplir como miembros de una sociedad."},
                {"pregunta": "¿Por qué son importantes las elecciones?", "respuesta": "Permiten seleccionar representantes y expresar preferencias políticas mediante procedimientos establecidos."},
                {"pregunta": "¿Qué es la libertad de expresión?", "respuesta": "Es el derecho a expresar ideas y opiniones dentro de los límites establecidos por la ley."},
                {"pregunta": "¿Qué significa respetar los derechos humanos?", "respuesta": "Reconocer y proteger la dignidad y los derechos de todas las personas."},
                {"pregunta": "¿Qué es la convivencia democrática?", "respuesta": "Es vivir respetando derechos, normas, diferencias y mecanismos pacíficos de participación."},
                {"pregunta": "¿Qué es la responsabilidad ciudadana?", "respuesta": "Es actuar cumpliendo deberes y considerando el impacto de nuestras acciones en la sociedad."},
                {"pregunta": "¿Por qué son importantes las normas?", "respuesta": "Porque establecen reglas que ayudan a organizar la convivencia social."}
            ],

            "Difícil": [
                {"pregunta": "¿Por qué la división de poderes es importante en una democracia?", "respuesta": "Distribuye funciones y establece controles entre instituciones para evitar la concentración excesiva del poder."},
                {"pregunta": "¿Por qué son importantes las instituciones democráticas?", "respuesta": "Organizan el funcionamiento del Estado, establecen reglas y permiten ejercer y controlar el poder público."},
                {"pregunta": "¿Qué relación existe entre derechos y deberes?", "respuesta": "El ejercicio de derechos debe convivir con el respeto a los derechos de los demás y el cumplimiento de responsabilidades."},
                {"pregunta": "¿Por qué la participación ciudadana fortalece la democracia?", "respuesta": "Porque permite que la población intervenga en asuntos públicos y supervise el funcionamiento de las instituciones."},
                {"pregunta": "¿Por qué el Estado de derecho es importante?", "respuesta": "Porque establece que autoridades y ciudadanos deben actuar conforme a normas jurídicas."},
                {"pregunta": "¿Qué importancia tiene la libertad de expresión en una democracia?", "respuesta": "Permite expresar ideas, debatir asuntos públicos y participar en la formación de opiniones."},
                {"pregunta": "¿Por qué debe existir separación de poderes?", "respuesta": "Para distribuir el poder y establecer mecanismos de control institucional."},
                {"pregunta": "¿Qué relación existe entre democracia y respeto a las minorías?", "respuesta": "Una democracia debe reconocer derechos y libertades de todas las personas, incluyendo grupos minoritarios."},
                {"pregunta": "¿Cómo puede un ciudadano participar además de votar?", "respuesta": "Puede participar en organizaciones, consultas, espacios comunitarios y otras formas legales de intervención pública."},
                {"pregunta": "¿Por qué es importante informarse antes de participar en asuntos públicos?", "respuesta": "Porque permite comprender mejor los problemas, evaluar información y participar de manera responsable."}
            ]
        }
    }
}


# ==========================================================
# FUNCIONES
# ==========================================================

def obtener_temas(materia):
    return list(banco_preguntas[materia].keys())


def obtener_preguntas(materia, tema, dificultad):
    return banco_preguntas[materia][tema][dificultad]


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("Configuración")

materia = st.sidebar.selectbox(
    "Selecciona una materia:",
    list(banco_preguntas.keys())
)

tema = st.sidebar.selectbox(
    "Selecciona un tema:",
    obtener_temas(materia)
)

dificultad = st.sidebar.selectbox(
    "Selecciona la dificultad:",
    [
        "Fácil",
        "Medio",
        "Difícil"
    ]
)

cantidad = st.sidebar.slider(
    "Cantidad de preguntas:",
    min_value=1,
    max_value=10,
    value=5
)

st.sidebar.divider()

st.sidebar.write("Materias disponibles:")

st.sidebar.write(
    f"{len(banco_preguntas)} materias"
)


# ==========================================================
# TEMA ESPECÍFICO
# ==========================================================

st.subheader("Tema específico")

tema_libre = st.text_input(
    "También puedes escribir un tema que quieras estudiar:",
    placeholder="Ejemplo: fotosíntesis"
)

if tema_libre.strip():

    encontrado = False

    for materia_nombre in banco_preguntas:

        for tema_nombre in banco_preguntas[materia_nombre]:

            if tema_libre.lower() in tema_nombre.lower():

                encontrado = True

    if encontrado:

        st.success(
            "El tema está disponible en el banco de preguntas."
        )

    else:

        st.info(
            "Ese tema todavía no está en el banco de preguntas. "
            "Selecciona uno de los temas disponibles."
        )


# ==========================================================
# GENERAR PREGUNTAS
# ==========================================================

if st.button(
    "Generar preguntas",
    type="primary"
):

    banco = obtener_preguntas(
        materia,
        tema,
        dificultad
    )

    # Selecciona preguntas SIN REPETIR

    seleccionadas = random.sample(
        banco,
        cantidad
    )

    st.session_state.preguntas = seleccionadas

    st.session_state.materia_actual = materia

    st.session_state.tema_actual = tema

    st.session_state.dificultad_actual = dificultad

    st.session_state.mostrar_respuestas = False


# ==========================================================
# MOSTRAR PREGUNTAS
# ==========================================================

if "preguntas" in st.session_state:

    st.divider()

    st.header(
        st.session_state.materia_actual
    )

    st.write(
        f"Tema: **{st.session_state.tema_actual}**"
    )

    st.write(
        f"Dificultad: **{st.session_state.dificultad_actual}**"
    )

    st.divider()

    for numero, item in enumerate(
        st.session_state.preguntas,
        start=1
    ):

        st.subheader(
            f"Pregunta {numero}"
        )

        st.write(
            item["pregunta"]
        )

        st.text_input(
            "Tu respuesta:",
            key=f"respuesta_{numero}"
        )

        st.divider()


# ==========================================================
# MOSTRAR RESPUESTAS
# ==========================================================

if "preguntas" in st.session_state:

    if st.button(
        "Mostrar respuestas"
    ):

        st.session_state.mostrar_respuestas = True


if (
    "mostrar_respuestas" in st.session_state
    and st.session_state.mostrar_respuestas
):

    st.header(
        "Respuestas correctas"
    )

    for numero, item in enumerate(
        st.session_state.preguntas,
        start=1
    ):

        st.write(
            f"**Pregunta {numero}:** "
            f"{item['respuesta']}"
        )


# ==========================================================
# INFORMACIÓN FINAL
# ==========================================================

st.divider()

st.info(
    "Selecciona una materia, un tema y una dificultad. "
    "Después genera preguntas para comenzar a estudiar."
)

st.caption(
    "StudyGen - Proyecto de programación de 4.º de secundaria"
)
