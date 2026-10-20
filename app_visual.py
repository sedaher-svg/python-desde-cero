# =======================================================
# Archivo: app_visual.py
# Aplicación: Python desde Cero (Interfaz Gráfica de Escritorio)
# =======================================================

import tkinter as tk
from tkinter import messagebox
import os
from lecciones import banco_lecciones

class PythonDesdeCeroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Python desde Cero - App Educativa")
        self.root.geometry("620x680")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f6f9")

        # Variables del juego
        self.indice = 0
        self.puntos = 0
        self.intentos = 3
        self.nombre = ""

        # Construir pantalla de inicio
        self.crear_pantalla_inicio()

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ---------------------------------------------------
    # PANTALLA 1: BIENVENIDA Y NOMBRE
    # ---------------------------------------------------
    def crear_pantalla_inicio(self):
        self.limpiar_pantalla()

        # Marco decorativo
        frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="groove", padx=30, pady=30)
        frame.pack(expand=True, padx=40, pady=40)

        titulo = tk.Label(frame, text="🐍 Python desde Cero", font=("Segoe UI", 20, "bold"), fg="#1e293b", bg="#ffffff")
        titulo.pack(pady=10)

        subtitulo = tk.Label(frame, text="Aprende los fundamentos de Python paso a paso\ncon retos interactivos.", font=("Segoe UI", 11), fg="#64748b", bg="#ffffff", justify="center")
        subtitulo.pack(pady=10)

        lbl_nombre = tk.Label(frame, text="¿Cuál es tu nombre?", font=("Segoe UI", 12, "bold"), fg="#334155", bg="#ffffff")
        lbl_nombre.pack(pady=(20, 5))

        self.entry_nombre = tk.Entry(frame, font=("Segoe UI", 12), width=24, justify="center", relief="solid", bd=1)
        self.entry_nombre.pack(pady=10, ipady=4)
        self.entry_nombre.focus()

        btn_iniciar = tk.Button(frame, text="🚀 ¡Comenzar Curso!", font=("Segoe UI", 12, "bold"), bg="#10b981", fg="#ffffff", activebackground="#059669", relief="flat", padx=20, pady=8, cursor="hand2", command=self.iniciar_curso)
        btn_iniciar.pack(pady=15)

        btn_ranking = tk.Button(frame, text="🏆 Ver Salón de la Fama", font=("Segoe UI", 10), bg="#e2e8f0", fg="#334155", relief="flat", padx=15, pady=5, cursor="hand2", command=self.mostrar_ranking)
        btn_ranking.pack(pady=5)

    def iniciar_curso(self):
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Atención", "Por favor, escribe tu nombre para comenzar.")
            return
        self.nombre = nombre
        self.indice = 0
        self.puntos = 0
        self.mostrar_leccion()

    # ---------------------------------------------------
    # PANTALLA 2: MOSTRAR LECCIÓN Y RETO
    # ---------------------------------------------------
    def mostrar_leccion(self):
        self.limpiar_pantalla()
        self.intentos = 3

        leccion = banco_lecciones[self.indice]

        # Barra superior con puntuación y vidas
        barra = tk.Frame(self.root, bg="#1e293b", padx=20, pady=10)
        barra.pack(fill="x")

        lbl_estudiante = tk.Label(barra, text=f"👤 {self.nombre}", font=("Segoe UI", 11, "bold"), fg="#f8fafc", bg="#1e293b")
        lbl_estudiante.pack(side="left")

        self.lbl_puntos = tk.Label(barra, text=f"⭐ Puntos: {self.puntos}", font=("Segoe UI", 11, "bold"), fg="#fbbf24", bg="#1e293b")
        self.lbl_puntos.pack(side="right")

        # Contenedor principal de la lección
        cuerpo = tk.Frame(self.root, bg="#f4f6f9", padx=30, pady=15)
        cuerpo.pack(fill="both", expand=True)

        # Título de la lección
        lbl_titulo = tk.Label(cuerpo, text=leccion["titulo"], font=("Segoe UI", 14, "bold"), fg="#0f172a", bg="#f4f6f9")
        lbl_titulo.pack(pady=(5, 10))

        # Tarjeta de teoría
        card_teoria = tk.Frame(cuerpo, bg="#ffffff", bd=1, relief="solid", padx=15, pady=12)
        card_teoria.pack(fill="x", pady=5)
        
        lbl_teoria_header = tk.Label(card_teoria, text="📘 Teoría:", font=("Segoe UI", 10, "bold"), fg="#2563eb", bg="#ffffff")
        lbl_teoria_header.pack(anchor="w")
        
        lbl_teoria = tk.Label(card_teoria, text=leccion["teoria"], font=("Segoe UI", 11), fg="#334155", bg="#ffffff", justify="left")
        lbl_teoria.pack(anchor="w", pady=5)

        # Pregunta / Reto
        lbl_reto = tk.Label(cuerpo, text="🎯 Reto:", font=("Segoe UI", 12, "bold"), fg="#0f172a", bg="#f4f6f9")
        lbl_reto.pack(anchor="w", pady=(15, 2))

        lbl_pregunta = tk.Label(cuerpo, text=leccion["pregunta"], font=("Segoe UI", 11), fg="#1e293b", bg="#f4f6f9", justify="left", wraplength=540)
        lbl_pregunta.pack(anchor="w", pady=(0, 10))

        # Entrada de respuesta
        self.entry_resp = tk.Entry(cuerpo, font=("Segoe UI", 12), width=35, relief="solid", bd=1)
        self.entry_resp.pack(pady=5, ipady=4)
        self.entry_resp.focus()
        self.entry_resp.bind("<Return>", lambda event: self.comprobar_respuesta())

        # Vidas restantes
        self.lbl_vidas = tk.Label(cuerpo, text="Intentos restantes: ❤️ ❤️ ❤️", font=("Segoe UI", 10, "bold"), fg="#ef4444", bg="#f4f6f9")
        self.lbl_vidas.pack(pady=5)

        # Mensaje de retroalimentación (pistas, aciertos)
        self.lbl_feedback = tk.Label(cuerpo, text="", font=("Segoe UI", 10), bg="#f4f6f9", wraplength=540)
        self.lbl_feedback.pack(pady=5)

        # Botón para comprobar
        self.btn_comprobar = tk.Button(cuerpo, text="Comprobar Respuesta", font=("Segoe UI", 11, "bold"), bg="#2563eb", fg="#ffffff", activebackground="#1d4ed8", relief="flat", padx=15, pady=6, cursor="hand2", command=self.comprobar_respuesta)
        self.btn_comprobar.pack(pady=8)

        # Botón siguiente (inicialmente oculto)
        self.btn_siguiente = tk.Button(cuerpo, text="Siguiente Lección ➡️", font=("Segoe UI", 11, "bold"), bg="#10b981", fg="#ffffff", activebackground="#059669", relief="flat", padx=15, pady=6, cursor="hand2", command=self.avanzar_leccion)

    def comprobar_respuesta(self):
        leccion = banco_lecciones[self.indice]
        usuario_resp = self.entry_resp.get().lower().replace(" ", "").strip()
        resp_esperada = leccion["respuesta"].lower().replace(" ", "").strip()

        if usuario_resp == resp_esperada or usuario_resp == resp_esperada + "()":
            self.puntos += 10
            self.lbl_feedback.configure(text="✅ ¡EXCELENTE! Respuesta correcta (+10 puntos).", fg="#16a34a")
            self.desactivar_entrada()
        else:
            self.intentos -= 1
            if self.intentos > 0:
                vidas_iconos = " ".join(["❤️"] * self.intentos)
                self.lbl_vidas.configure(text=f"Intentos restantes: {vidas_iconos}")
                self.lbl_feedback.configure(text=f"❌ Casi... 💡 Pista: {leccion['pista']}", fg="#d97706")
            else:
                self.lbl_vidas.configure(text="Intentos agotados 💔")
                self.lbl_feedback.configure(text=f"❌ Se acabaron los intentos. La respuesta era: {leccion['respuesta']}", fg="#dc2626")
                self.desactivar_entrada()

    def desactivar_entrada(self):
        self.entry_resp.configure(state="disabled")
        self.btn_comprobar.pack_forget()
        self.btn_siguiente.pack(pady=8)
        self.lbl_puntos.configure(text=f"⭐ Puntos: {self.puntos}")

    def avanzar_leccion(self):
        self.indice += 1
        if self.indice < len(banco_lecciones):
            self.mostrar_leccion()
        else:
            self.mostrar_pantalla_final()

    # ---------------------------------------------------
    # PANTALLA 3: RESUMEN FINAL Y GUARDADO
    # ---------------------------------------------------
    def mostrar_pantalla_final(self):
        self.limpiar_pantalla()
        total_posible = len(banco_lecciones) * 10

        # Guardar en ranking.txt
        with open("ranking.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"- {self.nombre} (App Visual): {self.puntos}/{total_posible} puntos\n")

        frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="groove", padx=30, pady=30)
        frame.pack(expand=True, padx=40, pady=40)

        if self.puntos == total_posible:
            icono, mensaje = "🏆", "¡PUNTAJE PERFECTO!\nEres un maestro de Python."
        elif self.puntos >= (total_posible * 0.7):
            icono, mensaje = "⭐", "¡EXCELENTE TRABAJO!\nTienes muy claros los fundamentos."
        else:
            icono, mensaje = "💪", "¡BUEN ESFUERZO!\nLa práctica hace al maestro."

        lbl_icono = tk.Label(frame, text=icono, font=("Segoe UI", 48), bg="#ffffff")
        lbl_icono.pack()

        lbl_fin = tk.Label(frame, text="¡Curso Completado!", font=("Segoe UI", 18, "bold"), fg="#0f172a", bg="#ffffff")
        lbl_fin.pack(pady=5)

        lbl_resultado = tk.Label(frame, text=f"Estudiante: {self.nombre}\nPuntuación: {self.puntos} de {total_posible} puntos", font=("Segoe UI", 12), fg="#334155", bg="#ffffff")
        lbl_resultado.pack(pady=10)

        lbl_mensaje = tk.Label(frame, text=mensaje, font=("Segoe UI", 11, "italic"), fg="#2563eb", bg="#ffffff", justify="center")
        lbl_mensaje.pack(pady=10)

        btn_ranking = tk.Button(frame, text="🏆 Ver Salón de la Fama", font=("Segoe UI", 11), bg="#3b82f6", fg="#ffffff", relief="flat", padx=15, pady=6, cursor="hand2", command=self.mostrar_ranking)
        btn_ranking.pack(pady=5)

        btn_reintentar = tk.Button(frame, text="🔄 Volver al Inicio", font=("Segoe UI", 11), bg="#e2e8f0", fg="#334155", relief="flat", padx=15, pady=6, cursor="hand2", command=self.crear_pantalla_inicio)
        btn_reintentar.pack(pady=5)

    def mostrar_ranking(self):
        contenido = "Aún no hay puntuaciones."
        if os.path.exists("ranking.txt"):
            with open("ranking.txt", "r", encoding="utf-8") as archivo:
                texto = archivo.read().strip()
                if texto:
                    contenido = texto
        messagebox.showinfo("🏆 Salón de la Fama", contenido)


# =======================================================
# EJECUCIÓN DE LA APLICACIÓN
# =======================================================
if __name__ == "__main__":
    ventana = tk.Tk()
    app = PythonDesdeCeroApp(ventana)
    ventana.mainloop()