import streamlit as st
import sympy as sp

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="MatePaso a Paso",
    page_icon="➗",
    layout="centered"
)

# =====================================================
# TÍTULO
# =====================================================

st.title("MatePaso a Paso")

st.write(
    "Resuelve ecuaciones de primer grado "
    "de forma sencilla y paso a paso."
)

st.divider()

# Variable matemática
x = sp.Symbol("x")


# =====================================================
# PREPARAR LA ECUACIÓN
# =====================================================

def preparar_ecuacion(texto):

    # Eliminar espacios
    texto = texto.replace(" ", "")

    # Convertir X mayúscula en x
    texto = texto.replace("X", "x")

    # Convertir ^ en **
    texto = texto.replace("^", "**")

    # Convertir algunas formas comunes
    texto = texto.replace("÷", "/")
    texto = texto.replace("−", "-")

    return texto


# =====================================================
# RESOLVER ECUACIÓN
# =====================================================

def resolver_ecuacion(texto):

    texto = preparar_ecuacion(texto)

    # Comprobar que tenga =
    if "=" not in texto:
        raise ValueError(
            "La ecuación debe contener el signo ="
        )

    # Separar los dos lados
    izquierda, derecha = texto.split("=", 1)

    # sympify entiende expresiones como:
    # 2*x + 5
    # 4*(x + 2)
    # x/2 + 3

    lado_izquierdo = sp.sympify(
        izquierda,
        locals={"x": x}
    )

    lado_derecho = sp.sympify(
        derecha,
        locals={"x": x}
    )

    # Crear ecuación
    ecuacion = sp.Eq(
        lado_izquierdo,
        lado_derecho
    )

    # Resolver
    soluciones = sp.solve(
        ecuacion,
        x
    )

    return ecuacion, soluciones


# =====================================================
# MOSTRAR PROCEDIMIENTO
# =====================================================

def mostrar_procedimiento(ecuacion, solucion):

    izquierda = ecuacion.lhs
    derecha = ecuacion.rhs

    st.subheader("Procedimiento paso a paso")

    # -------------------------------------------------
    # PASO 1
    # -------------------------------------------------

    st.write(
        "Paso 1: Llevamos todos los términos con x "
        "a un lado y los números al otro."
    )

    expresion = sp.expand(
        izquierda - derecha
    )

    st.latex(
        sp.Eq(
            expresion,
            0
        )
    )

    # -------------------------------------------------
    # PASO 2
    # -------------------------------------------------

    coeficiente = expresion.coeff(x)

    termino = expresion.subs(x, 0)

    st.write(
        "Paso 2: Identificamos el coeficiente de x "
        "y el término independiente."
    )

    st.latex(
        sp.Eq(
            coeficiente * x,
            -termino
        )
    )

    # -------------------------------------------------
    # PASO 3
    # -------------------------------------------------

    st.write(
        "Paso 3: Despejamos x."
    )

    st.latex(
        sp.Eq(
            x,
            solucion
        )
    )

    # -------------------------------------------------
    # RESULTADO
    # -------------------------------------------------

    st.divider()

    st.success(
        f"Resultado final: x = {solucion}"
    )

    st.latex(
        f"x = {sp.latex(solucion)}"
    )


# =====================================================
# CAJA DE TEXTO
# =====================================================

st.subheader("Escribe tu ecuación")

ejercicio = st.text_input(
    "Ecuación",
    placeholder="Ejemplo: 2x + 5 = 15"
)


# =====================================================
# BOTÓN
# =====================================================

if st.button(
    "Resolver ecuación",
    type="primary"
):

    if ejercicio.strip() == "":

        st.warning(
            "Primero escribe una ecuación."
        )

    else:

        try:

            ecuacion, soluciones = resolver_ecuacion(
                ejercicio
            )

            # -------------------------------------------------
            # COMPROBAR SOLUCIÓN
            # -------------------------------------------------

            if len(soluciones) == 0:

                st.error(
                    "Esta ecuación no tiene una solución."
                )

            elif len(soluciones) > 1:

                st.warning(
                    "Esta ecuación tiene más de una solución."
                )

                for solucion in soluciones:
                    st.write(
                        f"x = {solucion}"
                    )

            else:

                solucion = soluciones[0]

                st.success(
                    "Ecuación reconocida correctamente."
                )

                # -------------------------------------------------
                # ECUACIÓN ORIGINAL
                # -------------------------------------------------

                st.subheader(
                    "Ecuación"
                )

                st.latex(
                    sp.latex(ecuacion)
                )

                # -------------------------------------------------
                # PROCEDIMIENTO
                # -------------------------------------------------

                mostrar_procedimiento(
                    ecuacion,
                    solucion
                )

        except Exception as error:

            st.error(
                "No pude entender la ecuación."
            )

            st.write(
                "Ejemplos que puedes utilizar:"
            )

            st.code("2x + 5 = 15")
            st.code("3x - 7 = 14")
            st.code("5x = 35")
            st.code("2x + 8 = 4x - 6")
            st.code("4(x + 2) = 20")
            st.code("x/2 + 3 = 7")


# =====================================================
# EJEMPLOS
# =====================================================

st.divider()

st.subheader("Ejemplos")

st.write(
    "Prueba cualquiera de estas ecuaciones:"
)

ejemplos = [
    "2x + 5 = 15",
    "3x - 7 = 14",
    "5x = 35",
    "2x + 8 = 4x - 6",
    "4(x + 2) = 20",
    "x/2 + 3 = 7",
    "7 - 2x = 15",
    "3(x - 2) + 4 = 19"
]

for ejemplo in ejemplos:

    st.code(ejemplo)


# =====================================================
# BARRA LATERAL
# =====================================================

st.sidebar.title("Configuración")

st.sidebar.write(
    "Nivel: 4.º de secundaria"
)

st.sidebar.write(
    "Tema: Ecuaciones de primer grado"
)

st.sidebar.divider()

st.sidebar.write(
    "Funciones:"
)

st.sidebar.write(
    "Resolver ecuaciones"
)

st.sidebar.write(
    "Mostrar procedimiento"
)

st.sidebar.write(
    "Trabajar con paréntesis"
)

st.sidebar.write(
    "Trabajar con fracciones"
)

st.sidebar.write(
    "Resolver ecuaciones con x en ambos lados"
)

st.sidebar.divider()

st.sidebar.caption(
    "Proyecto de programación"
)