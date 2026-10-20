# =======================================================
# Archivo: app_web.py
# Aplicación Web: Python desde Cero (Streamlit)
# =======================================================

import streamlit as st
import os
from lecciones import banco_lecciones

# Configuración de la página web
st.set_page_config(page_title="Python desde Cero", page_icon="🐍", layout="centered")

# Inicializamos las variables de sesión
if "iniciado" not in st.session_state:
    st.session_state.iniciado = False
    st.session_state.indice = 0
    st.session_state.puntos = 0
    st.session_state.intentos = 3
    st.session_state.nombre = ""
    st.session_state.terminado = False
    st.session_state.respondido_bien = False
    st.session_state.sin_intentos = False

# Título de la Web
st.title("🐍 Python desde Cero")
st.caption("Aprende a programar paso a paso con retos interactivos.")

# -------------------------------------------------------
# PANTALLA 1: INICIO Y NOMBRE
# -------------------------------------------------------
if not st.session_state.iniciado and not st.session_state.terminado:
    st.write("### ¡Bienvenido a tu primer curso de programación!")
    st.write("Aprenderás conceptos clave y pondrás a prueba tu lógica.")

    nombre_input = st.text_input("¿Cuál es tu nombre para el certificado?:", placeholder="Ej: Selene")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🚀 Comenzar Curso", type="primary", use_container_width=True):
            if nombre_input.strip():
                st.session_state.nombre = nombre_input.strip()
                st.session_state.iniciado = True
                st.session_state.indice = 0
                st.session_state.puntos = 0
                st.session_state.intentos = 3
                st.rerun()
            else:
                st.warning("Por favor, escribe tu nombre para comenzar.")

    with col2:
        if st.button("🏆 Ver Salón de la Fama", use_container_width=True):
            if os.path.exists("ranking.txt"):
                with open("ranking.txt", "r", encoding="utf-8") as f:
                    st.text_area("Historial de Estudiantes", f.read(), height=200)
            else:
                st.info("Aún no hay puntuaciones registradas.")

# -------------------------------------------------------
# PANTALLA 2: JUEGO Y LECCIONES
# -------------------------------------------------------
elif st.session_state.iniciado and not st.session_state.terminado:
    total_lecciones = len(banco_lecciones)
    leccion_actual = banco_lecciones[st.session_state.indice]

    # Barra de progreso
    progreso = (st.session_state.indice) / total_lecciones
    st.progress(progreso)

    # Cabecera con datos del alumno
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write(f"👤 Estudiante: **{st.session_state.nombre}**")
    with c2:
        st.write(f"⭐ Puntos: **{st.session_state.puntos}**")

    # Contenido de la Lección
    st.subheader(leccion_actual["titulo"])
    
    with st.container():
        st.info(f"📘 **Teoría:**\n\n{leccion_actual['teoria']}")

    st.write(f"🎯 **Reto:** {leccion_actual['pregunta']}")

    # Vidas
    vidas_texto = " ❤️ " * st.session_state.intentos
    st.write(f"**Intentos restantes:** {vidas_texto}")

    # Formulario de respuesta
    with st.form(key=f"form_{st.session_state.indice}"):
        resp_usuario = st.text_input("Tu respuesta de código:", key=f"input_{st.session_state.indice}")
        boton_enviar = st.form_submit_button("Comprobar Respuesta")

    if boton_enviar:
        limpia = resp_usuario.lower().replace(" ", "").strip()
        esperada = leccion_actual["respuesta"].lower().replace(" ", "").strip()

        if limpia == esperada or limpia == esperada + "()":
            st.session_state.puntos += 10
            st.session_state.respondido_bien = True
            st.success("✅ ¡EXCELENTE! Respuesta correcta (+10 puntos).")
        else:
            st.session_state.intentos -= 1
            if st.session_state.intentos > 0:
                st.warning(f"❌ Casi... 💡 **Pista:** {leccion_actual['pista']}")
            else:
                st.session_state.sin_intentos = True
                st.error(f"❌ Intentos agotados. La respuesta correcta era: `{leccion_actual['respuesta']}`")

    # Botón para avanzar si acertó o se quedó sin intentos
    if st.session_state.respondido_bien or st.session_state.sin_intentos:
        if st.button("Siguiente Lección ➡️", type="primary"):
            st.session_state.indice += 1
            st.session_state.intentos = 3
            st.session_state.respondido_bien = False
            st.session_state.sin_intentos = False
            
            if st.session_state.indice >= total_lecciones:
                st.session_state.terminado = True
                st.session_state.iniciado = False
            st.rerun()

# -------------------------------------------------------
# PANTALLA 3: RESULTADOS FINALES
# -------------------------------------------------------
elif st.session_state.terminado:
    total_posible = len(banco_lecciones) * 10
    
    if st.session_state.puntos == total_posible:
        st.balloons()  # ¡Lluvia de globos! 🎈
        st.success(f"🏆 ¡PUNTAJE PERFECTO! {st.session_state.puntos} de {total_posible} puntos.")
        st.write("¡Eres un auténtico maestro de Python!")
    elif st.session_state.puntos >= (total_posible * 0.7):
        st.success(f"⭐ ¡EXCELENTE TRABAJO! {st.session_state.puntos} de {total_posible} puntos.")
        st.write("Tienes un gran dominio de los fundamentos.")
    else:
        st.info(f"💪 ¡Buen esfuerzo! {st.session_state.puntos} de {total_posible} puntos.")
        st.write("Sigue practicando para dominar todos los conceptos.")

    # Guardar en ranking.txt
    with open("ranking.txt", "a", encoding="utf-8") as f:
        f.write(f"- {st.session_state.nombre} (Web): {st.session_state.puntos}/{total_posible} puntos\n")

    if st.button("🔄 Reiniciar Curso", type="primary"):
        st.session_state.iniciado = False
        st.session_state.terminado = False
        st.session_state.indice = 0
        st.session_state.puntos = 0
        st.rerun()