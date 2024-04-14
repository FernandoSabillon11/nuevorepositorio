
import os
os.system('cls' if os.name == 'nt' else 'clear')

import math
print("ECUACIONES CUADRADITAS")

a =int(input('ingrese el valor de a: '))
b =int(input('ingrese el valor de b:'))
c =int(input('ingrese el valor de c: '))

x0=(-b+math.sqrt(b*b-4*a*c))/(2*a)
x1=(-b-math.sqrt(b*b-4*a*c))/(2*a)

print("+" + "-" * 20 + "+")
print("| x0= {:<16} |".format(x0))
print("| x1= {:<16} |".format(x1))
print("+" + "-" * 20 + "+")
