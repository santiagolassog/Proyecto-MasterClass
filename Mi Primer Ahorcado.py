import random

# Lista de palabras a adivinar
palabras = ["tony", "programacion", "desarrollo", "aprendizaje", "proyecto"]

def seleccionar_palabra():
    # Función para seleccionar una palabra aleatoria de la lista
    return random.choice(palabras)

def mostrar_palabra_oculta(palabra, letras_adivinadas):
    # Función para mostrar la palabra oculta con letras adivinadas
    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += "_"
    return palabra_mostrada

def dibujar_ahorcado(intentos_incorrectos):
    # Función para dibujar el ahorcado según los intentos incorrectos
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
palabra = seleccionar_palabra()
letras_adivinadas = []
intentos_incorrectos = 0
max_intentos = 6

print("¡Bienvenido al Juego del Ahorcado!")

while True:
    palabra_mostrada = mostrar_palabra_oculta(palabra, letras_adivinadas)
    print("\nPalabra: " + palabra_mostrada)
    letra = input("Ingresa una letra: ").lower()

    if letra in letras_adivinadas:
        print("Ya has adivinado esa letra.")
    elif letra in palabra:
        letras_adivinadas.append(letra)
        if palabra_mostrada == palabra:
            print("\n¡Felicidades! Has adivinado la palabra: " + palabra)
            break
    else:
        intentos_incorrectos += 1
        dibujar_ahorcado(intentos_incorrectos)
        if intentos_incorrectos == max_intentos:
            print("\n¡Has perdido! La palabra era: " + palabra)
            break
    
