# 1) Realizar un programa que me diga si un numero es par o impar

def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."

print("\n--------------------\n")

numero_usuario = int(input("Introduce un número: "))
resultado = es_par_o_impar(numero_usuario)

print(resultado)

print("\n--------------------\n")