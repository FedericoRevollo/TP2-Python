# 3) Realizar un programa que le pida al usuario su nombre y edad y nos diga si es mayor de edad

print("\n--------------------\n")

nombre = input("¿Cuál es tu nombre? ")

edad = int(input("\n¿Cuál es tu edad? "))

if edad >= 18:
    print(f"\n{nombre}, eres mayor de edad.")
else:
    print(f"\n{nombre}, eres menor de edad.")

print("\n--------------------\n")