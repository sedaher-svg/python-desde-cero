
# =======================================================
# Archivo: main.py
# Aplicación: Python desde Cero (Motor Principal)
# =======================================================

import os
# ¡Aquí importamos el contenido desde tu otro archivo!
from lecciones import banco_lecciones

# -------------------------------------------------------
# FUNCIONES DEL JUEGO
# -------------------------------------------------------

def hacer_pregunta(texto_pregunta, respuesta_correcta, pista):
    """Hace una pregunta, da 3 intentos, muestra pistas y devuelve puntos."""
    intentos = 3
    acerto = False

    while intentos > 0 and not acerto:
        respuesta = input(f"{texto_pregunta} (Intentos: {intentos}): ")
        
        resp_limpia = respuesta.lower().replace(" ", "").strip()
        resp_esperada = respuesta_correcta.lower().replace(" ", "").strip()

        if resp_limpia == resp_esperada or resp_limpia == resp_esperada + "()":
            print("✅ ¡Respuesta correcta! (+10 puntos)\n")
            acerto = True
            return 10
        else:
            intentos = intentos - 1
            if intentos > 0:
                print(f"❌ Casi... 💡 Pista: {pista}. ¡Prueba otra vez!\n")
            else:
                print(f"\n❌ Se agotaron los intentos. La respuesta era: {respuesta_correcta}\n")
                return 0


def ver_ranking():
    """Muestra el historial guardado en ranking.txt."""
    print("\n" + "=" * 52)
    print("           🏆 SALÓN DE LA FAMA (HISTORIAL)        ")
    print("=" * 52)

    if os.path.exists("ranking.txt"):
        with open("ranking.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido.strip():
                print(contenido)
            else:
                print("Aún no hay puntuaciones registradas.")
    else:
        print("Aún no hay puntuaciones registradas. ¡Sé el primero en jugar!")
    
    print("=" * 52 + "\n")


def agregar_nueva_leccion():
    """Permite al profesor crear una nueva lección desde la consola."""
    print("\n" + "=" * 52)
    print("         🎓 MODO PROFESOR: CREAR NUEVA LECCIÓN       ")
    print("=" * 52)

    titulo = input("1. Título de la lección: ").strip()
    teoria = input("2. Explicación teórica corta: ").strip()
    pregunta = input("3. Pregunta o reto para el estudiante: ").strip()
    respuesta = input("4. Respuesta correcta esperada: ").strip()
    pista = input("5. Pista por si el alumno falla: ").strip()

    nueva_ficha = {
        "titulo": titulo,
        "teoria": teoria,
        "pregunta": pregunta,
        "respuesta": respuesta,
        "pista": pista
    }

    banco_lecciones.append(nueva_ficha)
    print(f"\n✅ ¡Éxito! Ahora el curso tiene {len(banco_lecciones)} lecciones.\n")


def iniciar_entrenamiento():
    """Ejecuta automáticamente todas las lecciones importadas."""
    print("\n" + "=" * 52)
    print("             NUEVA SESIÓN DE APRENDIZAJE          ")
    print("=" * 52)

    nombre = input("¿Cuál es el nombre del estudiante?: ")
    print(f"\n¡Mucho gusto, {nombre}! Comencemos tu curso.\n")
    
    puntos = 0
    total_posible = len(banco_lecciones) * 10

    for leccion in banco_lecciones:
        print("-" * 52)
        print(leccion["titulo"])
        print("-" * 52)
        print(leccion["teoria"])
        print("-" * 52)
        
        puntos = puntos + hacer_pregunta(
            texto_pregunta=leccion["pregunta"],
            respuesta_correcta=leccion["respuesta"],
            pista=leccion["pista"]
        )

    print("=" * 52)
    print("              RESUMEN DE TU SESIÓN                ")
    print("=" * 52)
    print(f"Estudiante: {nombre}")
    print(f"Puntuación final: {puntos} de {total_posible} puntos.")

    if puntos == total_posible:
        print("🏆 ¡PUNTAJE PERFECTO! Eres un auténtico maestro de Python.")
    elif puntos >= (total_posible * 0.7):
        print("⭐ ¡Excelente trabajo! Tienes un gran dominio de los fundamentos.")
    else:
        print("💪 ¡A seguir practicando! La constancia hace al maestro.")

    with open("ranking.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"- {nombre}: {puntos}/{total_posible} puntos\n")

    print("\n💾 ¡Progreso guardado con éxito en 'ranking.txt'!\n")


# =======================================================
# BUCLE DEL MENÚ PRINCIPAL
# =======================================================

while True:
    print("=" * 52)
    print("     🐍 PYTHON DESDE CERO - MENÚ PRINCIPAL 🐍    ")
    print("=" * 52)
    print(f"1. Empezar entrenamiento ({len(banco_lecciones)} Lecciones)")
    print("2. Ver Salón de la Fama (Ranking)")
    print("3. Agregar nueva lección (Modo Profesor) 🎓")
    print("4. Salir del programa")
    print("=" * 52)

    opcion = input("Elige una opción (1, 2, 3 o 4): ").strip()

    if opcion == "1":
        iniciar_entrenamiento()
    elif opcion == "2":
        ver_ranking()
    elif opcion == "3":
        agregar_nueva_leccion()
    elif opcion == "4":
        print("\n👋 ¡Gracias por usar Python desde Cero! ¡Hasta pronto!\n")
        break
    else:
        print("\n⚠️ Opción no válida. Por favor, escribe 1, 2, 3 o 4.\n")