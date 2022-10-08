import math
L1=float(input("Ingrese lado 1: "))
L2=float(input("Ingrese lado 2: "))
L3=float(input("Ingrese lado 3: "))
s=(L1+L2+L3)/2
a=math.sqrt(s*(s-L1)*(s-L2)*(s-L3))
print("El área es: "+str(a))