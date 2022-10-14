import math
A=int(input("Valor de A: "))
B=int(input("Valor de B: "))
C=int(input("Valor de C: "))
D=(B**2)-(4*A*C)
if D==0:
    x=x1=x2=-B/(2*A)
    print("Valor de x1 y x2: ",x)
if D>0:
    X1=(-B+math.sqrt((B**2)-(4*A*C)))/2*A 
    X2=(-B-math.sqrt((B**2)-(4*A*C)))/2*A
    print("Valor X1: ",X1)
    print("Valor X2: ",X2)
if D<0:
    print("No tiene solución en los reales: ")