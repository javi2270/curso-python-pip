# Importamos la librería random para generar números aleatorios
import random

# Definimos las opciones del juego
opciones = ["piedra", "papel", "tijera"]

# Definimos la función `jugar_piedra_papel_tijera()`
def jugar_piedra_papel_tijera():

    # Generamos la jugada de la computadora
    jugada_computadora = random.choice(opciones)

    # Solicitamos la jugada del jugador
    jugada_jugador = input("¿Piedra, papel o tijera?: ")

    # Comparamos las jugadas y determinamos el resultado
    if jugada_jugador == jugada_computadora:
        resultado = "Empate"
    elif (jugada_jugador == "piedra" and jugada_computadora == "tijera") or (jugada_jugador == "papel" and jugada_computadora == "piedra") or (jugada_jugador == "tijera" and jugada_computadora == "papel"):
        resultado = "Jugador gana"
    else:
        resultado = "Computadora gana"

    # Imprimimos el resultado del juego
    print(f"La jugada de la computadora fue {jugada_computadora}. La jugada del jugador fue {jugada_jugador}. El resultado es {resultado}.")

# Ejecutamos la función `jugar_piedra_papel_tijera()`
jugar_piedra_papel_tijera()
