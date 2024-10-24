# 4) Realizar un programa donde el usuario ingrese una palabra y un numero e imprima por pantalla la palabra ingresa tantas veces como el numero ingresado

print("\n--------------------\n")

palabra = input("Introduce una palabra: ")

numero = int(input("\nIntroduce un número: "))

# _: Este es un nombre de variable convencional en Python que se utiliza cuando no necesitas utilizar la variable en el cuerpo del bucle. Aquí, _ indica que no estamos interesados en el valor actual de la iteración.
for _ in range(numero):
    print(f"\n{palabra}")

print("\n--------------------\n")