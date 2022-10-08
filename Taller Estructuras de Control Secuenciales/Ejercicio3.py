s=int(input("Sueldo base: "))
v1=int(input("Venta 1: "))
v2=int(input("Venta 2: "))
v3=int(input("Venta 3: "))
c=(v1*0.10)+(v2*0.10)+(v3*0.10)
t=s+c
print("Total comisiones: ",c)
print("Sueldo total más comisiones: ",t)