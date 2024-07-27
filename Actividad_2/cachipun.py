# Juego "Cachipún" contra la computadora 

# Instrucciones:
# Ejecuta el programa con el siguiente comando, 

# Ejemplo de comando: python cachipun.py piedra

# El programa pedirá al usuario que ingrese una opción (piedra, papel o tijera)
# Usa el comando de ejemplo y reemplaza piedra con 
# la opción que desees (piedra, papel, o tijera):


# ------------------------------------------------------------- #

import random
import sys

# Definir opciones 
opciones = ["piedra", "papel", "tijera"]

# Verificar que se haya pasado un argumento
if len(sys.argv) != 2:
    print("Uso: python cachipun.py [piedra|papel|tijera]")
    sys.exit(1)

# Obtener el argumento del usuario
jugador = sys.argv[1].lower()

# Verificar que el argumento sea válido
if jugador not in opciones:
    print("Argumento inválido: Debe ser piedra, papel o tijera")
    sys.exit(1)

# Elección random o al azar del computador
computador = random.choice(opciones)

# Imprimir las elecciones
print(f"Tu jugaste {jugador.capitalize()}")
print(f"Computador jugó {computador.capitalize()}")

# Determinar el resultado del juego
if jugador == computador:
    resultado = "Empate"
elif (jugador == "piedra" and computador == "tijera") or \
     (jugador == "papel" and computador == "piedra") or \
     (jugador == "tijera" and computador == "papel"):
    resultado = "¡Ganaste!"
else:
    resultado = "¡Perdiste!"

# Mostrar resultado
print(resultado)
