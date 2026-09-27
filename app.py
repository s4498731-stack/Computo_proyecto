import streamlit as st
import time

# 1. Configuración de la página
st.set_page_config(page_title="Prueba de IA en Equipo", page_icon="🚀", layout="centered")

st.title("🚀 Aplicación de Prueba en Equipo")
st.write("¡Si estás viendo esto, tu entorno de Streamlit en Codespaces funciona perfectamente!")

# 2. Caja de entrada interactiva para simular IA
st.subheader("🤖 Prueba el modelo de IA simulado")
usuario_input = st.text_input("Escribe una pregunta para la IA:", placeholder="Ej: ¿Cómo funciona Streamlit?")

if st.button("Enviar a la IA", type="primary"):
    if usuario_input:
        with st.spinner("La IA está procesando tu respuesta..."):
            time.sleep(1.5)  # Simula el tiempo de espera de una API de IA
        st.success(f"🤖 **Respuesta de la IA:** He recibido tu mensaje: '{usuario_input}'. ¡El sistema interactivo está respondiendo en vivo!")
    else:
        st.warning("Por favor, escribe algo primero antes de presionar el botón.")

# 3. Panel de control interactivo (Sidebar)
st.sidebar.header("⚙️ Ajustes del Modelo")
temperatura = st.sidebar.slider("Temperatura (Creatividad)", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
st.sidebar.info(f"Configuración actual del equipo: {temperatura}")
