# calcula la ecuacion cuadratica
import os
os.system('cls' if os.name == 'nt' else 'clear')

import math
print("ECUACIONES CUADRADITAS")

a =int(input('ingrese el valor de a: '))
b =int(input('ingrese el valor de b:'))
c =int(input('ingrese el valor de c: '))





x0=(-b+math.sqrt(b*b-4*a*c))/(2*a)
x1=(-b-math.sqrt(b*b-4*a*c))/(2*a)


print("x0= ",x0)
print("x1= ",x1)

print(F"x0= {x0}      x1={x1}")