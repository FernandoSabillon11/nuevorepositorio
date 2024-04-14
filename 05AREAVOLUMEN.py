#CALCULAR EL AREA Y VOLUMEN DE UNA ESFERA

import os
os.system('cls' if os.name == 'nt' else 'clear')

import math

print("PROGRAMA QUE CALCULA EL AREA Y VOLUMEN DE UNA ESFERA")
r=float(input("Radio: "))
area=4*math.pi*r*r
area=4*math.pi*math.pow

vol=(4/3)*math.pi*r*r*r


print(f"Area esfera={area}")
print(f"area")