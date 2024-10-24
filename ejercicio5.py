# 5) Realizar un programa que sume los números ingresados por el usuario hasta que se ingrese un 0. Al finalizar nos debe mostrar la suma por pantalla.

print("\n--------------------\n")

# Inicializar la suma
suma_total = 0

while True:
    # Solicitar al usuario que ingrese un número
    numero = int(input("Introduce un número (0 para finalizar): "))
    
    # Verificar si el número es 0
    if numero == 0:
        break  # Salir del bucle si se ingresa 0
    
    # Sumar el número a la suma total
    suma_total += numero

# Mostrar la suma total
print(f"\nLa suma total es: {suma_total}")


print("\n--------------------\n")