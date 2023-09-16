import random

juego = random.randint(1, 30)  # Genera un número aleatorio entre 1 y 30
vidas = 5

print("Bienvenido")
print("La indicación de este juego es la siguiente:")
print("Tienes que adivinar el número que hemos pensado, está en un rango de 1 a 30")
print("Para ello tienes 5 vidas o 5 intentos")
print("¡Mucha suerte! :D\n")

while vidas > 0:
    try:
        intento = int(input("Ingresa tu adivinanza (1-30): "))
        if 1 <= intento <= 30:
            if intento == juego:
                print(f"¡Felicidades! Has adivinado el número {juego}. ¡Ganaste!")
                break
            else:
                vidas -= 1
                if vidas > 0:
                    if intento < juego:
                        print(f"El número es mayor. Te quedan {vidas} vidas.")
                        
                  