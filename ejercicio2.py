# 2) Realizar un programa que genere la tabla de multiplicar de un numero ingresado por el usuario (del 1 al 10)

print("\n--------------------\n")

numero_usuario = int(input("Introduce un número para generar su tabla de multiplicar: "))

# Generar y mostrar la tabla de multiplicar
print(f"\nTabla de multiplicar del {numero_usuario}:")
for i in range(1, 11):
    resultado = numero_usuario * i
    print(f"\n{numero_usuario} x {i} = {resultado}")

print("\n--------------------\n")