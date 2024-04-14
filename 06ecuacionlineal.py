#Ecuacion lineal
import os
os.system('cls' if os.name == 'nt' else 'clear')

for i in range(10):
    a = float(input('Ingrese el valor de a: '))
    b = float(input('Ingrese el valor de b: '))

    if a == 0:
        print("Error: El valor de 'a' no puede ser cero.")
    else:
        x = -b/a
        print(f"El valor de x es: {x}")
