#Este es el bueno ahora si 3.0 :)

import random

# Datos del juego
personajes = [
    {"nombre": "Sra. Blanca", "profesion": "Ama de llaves"},
    {"nombre": "Coronel Sanders", "profesion": "Militar"},
    {"nombre": "Sr. Griphook", "profesion": "Banquero"},
    {"nombre": "Sra. Azul", "profesion": "Artista"},
    {"nombre": "Dr. Alastor", "profesion": "Profesor"}
]

locaciones = {
    "Salón": "El crimen tuvo lugar en el lujoso salón. Luces tenues y aroma de incienso.",
    "Biblioteca": "La biblioteca estaba en silencio cuando ocurrió el crimen. Solo las sombras conocían el secreto.",
    "Cocina": "En medio de ollas y cuchillos, alguien cometió un asesinato en la cocina.",
    "Jardín": "El jardín se veía tranquilo, hasta que alguien descubrió un cuerpo junto a los rosales.",
    "Estudio": "El crimen sucedió en el estudio, rodeado de libros antiguos y secretos."
}

armas = ["Lápiz", "Daga", "Pistola", "Cuerda", "Llave inglesa"]

# Selección aleatoria de culpable, arma y locación
culpable = random.choice(personajes)
arma_seleccionada = random.choice(armas)
locacion_seleccionada = random.choice(list(locaciones.keys()))

# Resultados de la investigación
resultados_investigacion = [
    "Encuentras huellas en el suelo que llevan hacia la salida.",
    "Hay una nota arrugada en el suelo con pistas sobre el arma usada.",
    "Encuentras un guante ensangrentado bajo un mueble cercano.",
    "La victima contiene restos de sagre entre las uñas, al parecer son del culpable.",
    "Las ventanas están rotas desde dentro, indicando una posible lucha.",
    "La posición del cuerpo sugiere que intentaba huir del atacante.",
    "Una grabación de seguridad muestra una figura misteriosa rondando el área."

]

# Respuestas de los personajes
respuestas_inocente = [
    "Responde con seguridad, afirmando su inocencia.",
    "Te mira a los ojos y te explica con calma por qué no podría haberlo hecho.",
    "Responde tranquilamente y proporciona información convincente.",
    "Mantiene una postura relajada mientras habla y su tono es consistente.",
    "Da detalles específicos de su coartada y responde a todas las preguntas sin vacilar."
]

respuestas_culpable = [
    "Parece nervioso y evita tu mirada.",
    "Se muestra impaciente y cambia de tema abruptamente.",
    "Se pone a la defensiva y comienza a sudar visiblemente.",
    "Tartamudea ligeramente y su voz tiembla cuando intenta justificarse.",
    "Se toca el rostro o el cuello con frecuencia, mostrando signos de incomodidad."
]

# Presentar información inicial
print("Bienvenido al juego de Clue - Edición Chafa-Mejorada")
print(f"El crimen ocurrió en: {locacion_seleccionada}")
print(locaciones[locacion_seleccionada])

# Función de investigar la locación
def investigar():
    print("\nInvestigas la locación detenidamente...")
    pista = random.choice(resultados_investigacion)
    print(f"Pista encontrada: {pista}")

# Función de interrogar a un personaje
def interrogar():
    print("\nPersonajes disponibles para interrogar:")
    for i, personaje in enumerate(personajes, 1):
        print(f"{i}. {personaje['nombre']} ({personaje['profesion']})")
    
    try:
        eleccion = int(input("Selecciona el número del personaje que quieres interrogar: "))
        if 1 <= eleccion <= len(personajes):
            personaje = personajes[eleccion - 1]
            if personaje == culpable:
                respuesta = random.choice(respuestas_culpable)
            else:
                respuesta = random.choice(respuestas_inocente)
            print(f"{personaje['nombre']} responde: {respuesta}")
        else:
            print("Número fuera de rango. Inténtalo de nuevo.")
            interrogar()
    except ValueError:
        print("Entrada no válida. Introduce un número.")
        interrogar()

# Función de acusar al culpable
def acusar():
    print("\n¡Es hora de acusar al culpable!")
    for i, personaje in enumerate(personajes, 1):
        print(f"{i}. {personaje['nombre']} ({personaje['profesion']})")
    
    try:
        eleccion = int(input("¿A quién acusas?: "))
        if 1 <= eleccion <= len(personajes):
            acusado = personajes[eleccion - 1]
            if acusado == culpable:
                print(f"¡Felicidades! Has resuelto el caso. El culpable era {acusado['nombre']} con un(a) {arma_seleccionada} en {locacion_seleccionada}.")
            else:
                print(f"Lo siento, {acusado['nombre']} no es el culpable.")
        else:
            print("Número fuera de rango. Inténtalo de nuevo.")
            acusar()
    except ValueError:
        print("Entrada no válida. Introduce un número.")
        acusar()

# Menú principal
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Investigar la locación")
        print("2. Interrogar a un personaje")
        print("3. Acusar al culpable")
        print("4. Salir")
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == '1':
            investigar()
        elif opcion == '2':
            interrogar()
        elif opcion == '3':
            acusar()
            break
        elif opcion == '4':
            print("¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el juego
menu()
