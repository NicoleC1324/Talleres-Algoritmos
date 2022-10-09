x=int(input("Cantidad de naranjas: "))
y=int(input("Costo de la docena: "))
k=int(input("Venta de las naranjas: "))
pu=(x*y)/12
p=(k-pu)*100/pu
print("Las ganancias son: ",p,"%")