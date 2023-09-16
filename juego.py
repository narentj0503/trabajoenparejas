import random

juegoo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

print("Bienvenido")
print("La indicación de este juego es la siguiente:")
print("Tienes que adivinar el número que hemos pensado, está en un rango de 1 a 30")
print("Para ello tienes 5 vidas o 5 intentos")
print("¡Mucha suerte! :D\n")

vidas = 5

juego = random.choice(juegoo)

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
                    print(f"¡Incorrecto! Te quedan {vidas} vidas.")
                else:
                    print(f"¡Incorrecto! ¡Perdiste! El número correcto era {juego}.")
        else:
            print("Debes ingresar un número dentro del rango 1-30.")
    except ValueError:
        print("Ingresa un número válido.")

print("Fin del juego. ¡Gracias por jugar!")