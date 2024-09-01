# Importación de librerías
import random

# Lista de palabras a adivinar
palabras = ["coding", "ganar"]

# Función para seleccionar una palabra aleatoria de la lista
def seleccionar_palabra():
    word = random.choice(palabras)
    return word
    
# Función para mostrar la palabra oculta con letras adivinadas
def mostrar_palabra_oculta(palabra, letras_adivinadas):
    palabra_mostrada = ""

    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += "_"  

    return palabra_mostrada

# Función para dibujar el ahorcado según los intentos incorrectos
def dibujar_ahorcado(intentos_incorrectos):

    ahorcado = [
        "  ____ ",
        " |    |",
        " |    O",
        " |   /|\\",
        " |   / \\",
        "_|_"
    ]

    for i in range(intentos_incorrectos):
        print(ahorcado[i])
    
"""-------------------------------------
INICIO DE JUEGO
-------------------------------------"""
# Declaración de variables
palabra = seleccionar_palabra()
letras_adivinadas = []
intentos_incorrectos = 0
max_intentos = 6

# Mensaje de bienvenida
print("¡Bienvenido al Juego del Ahorcado!")

while True:
    palabra_mostrada = mostrar_palabra_oculta(palabra, letras_adivinadas)
    print("\nPalabra: " + palabra_mostrada)
    
    letra = input("Ingresa una letra: ")

    if letra in letras_adivinadas:
        print("ALERTA! Ya has ingresado esa letra.")
        
    elif letra in palabra:
        letras_adivinadas.append(letra)
        
        if palabra_mostrada == palabra:
            print("\nFelicidades! Has adivinado la palabra "+palabra)
            break

    else: 
        intentos_incorrectos += 1
        dibujar_ahorcado(intentos_incorrectos)
        if intentos_incorrectos == max_intentos:
            print("\GAME OVER! La palabra era:"+palabra)
            break
    