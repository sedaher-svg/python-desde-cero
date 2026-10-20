# 🐍 Python desde Cero

¡Bienvenido a **Python desde Cero**! Una aplicación educativa de consola diseñada especialmente para principiantes que quieren aprender a programar paso a paso, practicar con retos interactivos y comprobar sus conocimientos.

---

## 🚀 Características del Proyecto

* **Interfaz de Consola Interactiva:** Navegación fluida mediante un menú principal continuo.
* **Sistema de Vidas y Pistas:** Los estudiantes tienen hasta 3 intentos por reto; si fallan, la aplicación les ofrece una pista didáctica.
* **Salón de la Fama Persistente:** Las puntuaciones se guardan automáticamente en `ranking.txt` en el disco.
* **Modo Profesor:** Permite a los instructores crear y añadir nuevas lecciones en tiempo real sin tocar el código.
* **Arquitectura Modular (DRY):** Código limpio dividido en lógica (`main.py`) y contenidos (`lecciones.py`).

---

## 📂 Estructura del Proyecto

```text
python_desde_cero/
│
├── main.py          # Motor principal y lógica del juego
├── lecciones.py     # Banco de lecciones y preguntas (Diccionarios)
├── ranking.txt      # Archivo persistente con el historial de alumnos
└── README.md        # Documentación oficial del proyecto