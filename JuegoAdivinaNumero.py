import random

#### JUEGO ADIVINA EL NUMERO CONTRA LA COMPUTADORA ### 
numero_pensado = random.choice(list(range(1,50)))
numero = int(input("La computadora ha pensado un numero entre 1 y 50, eres capaz de adivinarlo. intentalo ingresa un numero: "))

while numero != numero_pensado:

    if numero > numero_pensado:
        print("El numero esta por encima del numero pensado")
        numero = int(input("Ingresa otro numero:"))
    elif numero < numero_pensado:
        print("El numero esta por debajo del numero pensado")
        numero = int(input("Ingresa otro numero: "))

if numero == numero_pensado:
        print("Perfecto haz adivinado el numero!!!")